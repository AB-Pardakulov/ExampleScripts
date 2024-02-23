using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RespawnScroll : MonoBehaviour
{
    public Transform spawnPoint;//Add empty gameobject as spawnPoint
    public GameObject Scroll; //Add your player
    public float MinHeight = -20;
   

    void Update()
    {
        if (Scroll.transform.position.y < MinHeight)
            Scroll.transform.position = spawnPoint.position;
    }


}

