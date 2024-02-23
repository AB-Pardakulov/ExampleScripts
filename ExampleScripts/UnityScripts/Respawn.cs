using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Respawn : MonoBehaviour
{
    public Transform spawnPoint;
    public GameObject player; 
    public float MinHeight = -40;

    void Update()
    {
        if (player.transform.position.y < MinHeight)
            player.transform.position = spawnPoint.position;

       
    }
}
