using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NoclipCamera : MonoBehaviour
{
    public GameObject player;
    public GameObject alt_camera;

    private bool noclipEnabled = false;

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.N))
        {
            noclipEnabled = !noclipEnabled;

            if (noclipEnabled)
            {
                player.SetActive(false);
                alt_camera.SetActive(true);
            }
            else
            {
                player.SetActive(true);
                alt_camera.SetActive(false);
            }
        }

       
    }
}
