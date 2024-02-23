using System.Collections;
using System.Collections.Generic;
using UnityEngine; 

public class CameraShake : MonoBehaviour
{
    public float duration = 0.5f;
    public float magnitude = 1.0f;
    public bool StartS = false;
    public float delay = 0.05f;

    private IEnumerator shakeCoroutine;
    
    void Update()
    {
        CheckButtonPress();
        if (StartS)
        {
            StartCoroutine(DelayAndShake());
           
        }
    }

    public void CheckButtonPress()
    {
        RaycastHit hit;
        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);

        if (Physics.Raycast(ray, out hit))
        {
            if (hit.transform.gameObject.CompareTag("Button1") && Input.GetMouseButtonDown(0))
            {
                StartS = true; 
            }
        }
    }
    public void StartShake()
    {
        if (shakeCoroutine != null)
        {
            StopCoroutine(shakeCoroutine);
        }

        shakeCoroutine = Shake();
        StartCoroutine(shakeCoroutine);
    }
    IEnumerator DelayAndShake()
    {
        Vector3 originalPosition = transform.localPosition;
        yield return new WaitForSeconds(delay);
        Debug.Log("Delay finished!");
        StartShake();
        StartS = false;
        yield return new WaitForSeconds(duration*1.01f);
        transform.localPosition = originalPosition;
    }
    IEnumerator Shake()
    {
        float elapsedTime = 0.0f;
        Vector3 originalPosition = transform.localPosition;

        while (elapsedTime < duration)
        {
            float x = Random.Range(-1.0f, 1.0f) * magnitude;
            float y = Random.Range(-1.0f, 1.0f) * magnitude;

            transform.localPosition = new Vector3(x, y, originalPosition.z);

            elapsedTime += Time.deltaTime;

            yield return null;
        }

        transform.localPosition = originalPosition;
       
    }
}
