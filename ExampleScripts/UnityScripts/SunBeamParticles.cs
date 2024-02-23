using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SunBeamParticles : MonoBehaviour
{
    public ParticleSystem particleSystem;
    public float radius = 5.0f;
    public float speed = 5.0f;
    public float jitter = 0.1f;

    private ParticleSystem.Particle[] particles;
    private Vector3 center;
    private float angle;

    void Start()
    {
        center = transform.position;
        particles = new ParticleSystem.Particle[particleSystem.main.maxParticles];
    }

    void Update()
    {
        int numParticles = particleSystem.GetParticles(particles);

        for (int i = 0; i < numParticles; i++)
        {
            angle += Random.Range(-jitter, jitter);
            Vector3 offset = new Vector3(Mathf.Cos(angle), Mathf.Sin(angle), 0.0f) * radius;
            particles[i].position = center + offset;
            particles[i].velocity = offset.normalized * speed;
        }

        particleSystem.SetParticles(particles, numParticles);
    }
}
