using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Camera_Bob : MonoBehaviour
{

    public Transform Camera;
    public float move = Mathf.Sin(0);
    public float RangeFactor = 1f;
    public GameObject cam;
    public float Downslide = 0f; 


    // Update is called once per frame
    void Update()
    {
        float move = 0.15f * Mathf.Sin(Time.time * 2f);

        Camera.Translate(Vector3.up * move * Time.deltaTime * RangeFactor);

        float Downslide = (cam.transform.position.y - 6.5f) / 60; 

        Camera.Translate(Vector3.down * Downslide);


    }
}
