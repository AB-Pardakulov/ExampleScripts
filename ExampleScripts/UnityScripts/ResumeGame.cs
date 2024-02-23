using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using static PauseGame;
public class ResumeGame : MonoBehaviour
{
    public void ResumeGameButton()
    {
        IsPaused = false;
        Time.timeScale = 1;
    }
}
