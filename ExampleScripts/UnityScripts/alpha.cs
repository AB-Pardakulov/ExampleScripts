using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class alpha : MonoBehaviour
{
    public Transform A;
    public Transform Glass; 
    private bool Step = false;
    float GoingUpVar;
    float GoingDownVar;
    float GoingUpGlass;
    float GoingDownGlass;

    void Update()
    {
        GoingDownVar = (A.position.y - 12.521f + 10.420f) / 1f;
        GoingUpVar = (A.position.y - 12.35f + 9.88f) / 1f;

        GoingUpGlass = (Glass.position.y - 12.67f);
        GoingDownGlass = (Glass.position.y - 28f);


        if (Step == true)
        {
            A.Translate(Vector3.back * GoingDownVar * Time.deltaTime);
            Glass.Translate(Vector3.down * GoingDownGlass * Time.deltaTime);
        }
       
        if (Step == false)
        {
            A.Translate(Vector3.back * GoingUpVar * Time.deltaTime);
            Glass.Translate(Vector3.down * GoingUpGlass * Time.deltaTime);
        }
    }

    
    
    private void OnTriggerExit(Collider other)
    {
        Step = false; 
    }

    private void OnTriggerEnter(Collider other)
    {
        Step = true;
    }

    

}
