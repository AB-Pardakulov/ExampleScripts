using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ButtonEvent : MonoBehaviour
{
    public Transform buttonTransform;
    public float movementDistance = 0.1f;
    public float movementDuration = 0.5f;

    public bool buttonPressed = false;
    private float elapsedTime = 0.0f;
    private Vector3 startPosition;
    private Vector3 endPosition;

    void Start()
    {
        startPosition = buttonTransform.position;
        endPosition = startPosition + Vector3.down * movementDistance;
    }

    void Update()
    {
        CheckButtonPress();

        if (buttonPressed)
        {
            elapsedTime += Time.deltaTime;

            float t = elapsedTime / movementDuration;
            buttonTransform.position = Vector3.Lerp(startPosition, endPosition, t);

            if (t >= 1.0f)
            {
                buttonPressed = false;
                elapsedTime = 0.0f;
            }
        }
        if (!buttonPressed)
        {
            elapsedTime += Time.deltaTime;
            float t = elapsedTime / movementDuration;
            buttonTransform.position = Vector3.Lerp(endPosition, startPosition, t);
        }
    }

    void CheckButtonPress()
    {
        RaycastHit hit;
        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);

        if (Physics.Raycast(ray, out hit))
        {
            if (hit.transform.gameObject.CompareTag("Button1") && Input.GetMouseButtonDown(0))
            {
                buttonPressed = true;
            }
        }
    }
}
