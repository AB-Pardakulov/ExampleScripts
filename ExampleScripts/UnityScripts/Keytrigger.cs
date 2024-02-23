using Microsoft.Unity.VisualStudio.Editor;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Keytrigger : MonoBehaviour
{
    private bool IsKeyClose = false;
    public Canvas key;
    public GameObject KeyOne;
    public bool GotKey = false;
    public Canvas HasKeyUI;

    void Update()
    {
        if (IsKeyClose)
        {
            if (Input.GetKeyDown(KeyCode.E))
            {
                Destroy(KeyOne);
                GotKey = true;
                key.enabled = false;
                HasKeyUI.enabled = true;

            }
        }
       
    }
    private void OnTriggerEnter(Collider other)
    {
        IsKeyClose = true; 
        if (!GotKey)
        {
            key.enabled = true;
        }
        
    }

    private void OnTriggerExit(Collider other)
    {
        IsKeyClose = false;
        if (!GotKey)
        {
            key.enabled = false;
        }
    }
}
