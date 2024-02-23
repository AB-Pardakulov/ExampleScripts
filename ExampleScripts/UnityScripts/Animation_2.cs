using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Animation_2 : MonoBehaviour
{
    // Start is called before the first frame update

    public Transform Log;
    public float move = Mathf.Sin(0);
    public float RangeFactor = 1f;

    // Update is called once per frame
    void Update()
    {

        float move = 0.8f * Mathf.Sin(Time.time * 1.5f);

        Log.Translate(Vector3.forward * move * Time.deltaTime * RangeFactor);



    }
}
