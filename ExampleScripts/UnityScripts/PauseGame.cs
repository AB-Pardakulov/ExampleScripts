using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PauseGame : MonoBehaviour
{
    public GameObject menuPanel;
    public static bool IsPaused = false;
    public MonoBehaviour playerscript;

    // Update is called once per frame
    void Update()
    {
        if (!IsPaused)
        {
            menuPanel.SetActive(false);
            playerscript.enabled = true;
        }

        if (Input.GetKeyDown(KeyCode.Escape))
        {
            if (Time.timeScale == 1)
            {
              StopGame();
            }
            else
            {
              ResumeGame();
            } 
        }
        
    }

    public void ResumeGame()
    {
        Time.timeScale = 1;
        menuPanel.SetActive(false);
        IsPaused = false;
        playerscript.enabled = true;
    }
    public void StopGame()
    {
        Time.timeScale = 0;
        menuPanel.SetActive(true);
        IsPaused = true;
        playerscript.enabled = false;
    }
    public class GlobalVariable : MonoBehaviour
    {
       
        void Update()
        {
            Debug.Log(IsPaused);
        }
    }


}
