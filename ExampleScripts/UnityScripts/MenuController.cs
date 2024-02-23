using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using static PickUpController;
public class MenuController : MonoBehaviour
{
    // The camera that will be used for panning
    public Camera panningCamera;

    // The game object that will be panned around
    public GameObject panningObject;

    // The first person controller script that will be disabled during panning
    public MonoBehaviour firstPersonController;
    public Canvas ScrollMenu;

    // The speed at which the camera will pan around the object
    public float panningSpeed = 1.0f;

    // A flag that indicates whether the panning is currently active
    private bool isPanning = false;

    // The current panning angle
    private float panningAngle = 0.0f;

    void Update()
    {
        OnInteract();
        // If the panning is active, update the camera's position and orientation
        if (isPanning == true)
        {
            // Get the mouse position and use it to determine the panning angle
            Vector3 mousePos = Input.mousePosition;
            panningAngle = (mousePos.x / Screen.width) * 360.0f;

            panningCamera.transform.position = panningObject.transform.position + Quaternion.Euler(0.0f, panningAngle, 0.0f) * Vector3.forward * 5.0f;
            panningCamera.transform.LookAt(panningObject.transform);
        }
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            heldObj = null;
        }
    }

    // Called when the player interacts with the game object
    public void OnInteract()
    {
        // If the panning is already active, stop the panning and enable the first person controller
        if (heldObj == panningObject)
        {
            isPanning = true;
            firstPersonController.enabled = false;
            ScrollMenu.enabled = true;
            //panningCamera.enabled = true;
        }
        // If the panning is not active, start the panning and disable the first person controller
        else
        {
            isPanning = false;
            firstPersonController.enabled = true;
            ScrollMenu.enabled = false;
            panningAngle = 0.0f;
            //panningCamera.enabled = false;
        }
    }
}
