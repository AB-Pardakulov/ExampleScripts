using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using static MenuController; 

public class PickUpController : MonoBehaviour
{
    [Header("Pickup Settings")]
    [SerializeField] Transform HoldArea;
    public static GameObject heldObj;
    private Rigidbody heldObjRB;
    


    [Header("Physics Parameters")]
    [SerializeField] private float pickupRange = 5.0f;
    [SerializeField] private float pickupForce = 150.0f;

    private void Update()
    {
        if(Input.GetMouseButtonDown(0))
        {
            if (heldObj == null)
            { 
                RaycastHit hit;
                if(Physics.Raycast(transform.position, transform.TransformDirection(Vector3.forward), out hit, pickupRange))
                {
                    //Pickup Object
                    PickupObject(hit.transform.gameObject);

                }

            }
            else
            {
                //Drop the Object
                DropObject();
            }
        }
        if (heldObj != null)
        {
            //Moveobject
            MoveObject(); 

        }
            
    }

    void MoveObject()
    {
        if(Vector3.Distance(heldObj.transform.position, HoldArea.position) > 0.1f)
        {
            Vector3 moveDirection = (HoldArea.position - heldObj.transform.position);
            heldObjRB.AddForce(moveDirection * pickupForce);
        }
    }
    
    void PickupObject(GameObject pickObj)
    {
        if(pickObj.GetComponent<Rigidbody>())
        {
            heldObjRB = pickObj.GetComponent<Rigidbody>();
            heldObjRB.useGravity = false;
            heldObjRB.drag = 10;
            heldObjRB.constraints = RigidbodyConstraints.FreezeRotation;

            heldObjRB.transform.parent = HoldArea;
            heldObj = pickObj;
        }

    }
    void DropObject()
    {

        heldObjRB.useGravity = true;
        heldObjRB.drag = 1;
        heldObjRB.constraints = RigidbodyConstraints.None; 
        heldObj.transform.parent = null;
        heldObj = null;
        
    }

}
