
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Animation_3 : MonoBehaviour
{
    // Start is called before the first frame update

    public Transform Object;
    public float move_ = Mathf.Sin(0);
    public float RangeFactor_ = 1f;
    public float initial_offset = 0f;
    public float speed = 1f; 

    // Update is called once per frame
    void Update()
    {

        float move_ = 0.8f * speed * Mathf.Sin((Time.time + initial_offset) * 1.5f);

        Object.Translate(Vector3.up * move_ * Time.deltaTime * RangeFactor_);



    }
}
