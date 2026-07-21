# Gesture3D ✋🗡️

Proyecto de visión por computadora para controlar objetos 3D mediante el seguimiento de las manos en tiempo real.

Actualmente utiliza **Python**, **OpenCV** y **MediaPipe** para detectar las manos, y posteriormente se integrará con **Unity** para controlar objetos 3D mediante gestos.

---

# Objetivo

Desarrollar un sistema capaz de controlar un objeto 3D, utilizando únicamente los movimientos de las manos capturados por una webcam.

El proyecto está diseñado con una arquitectura modular para separar la visión por computadora, el reconocimiento de gestos y el motor gráfico.

---

# Tecnologías

- Python 3.10
- OpenCV
- MediaPipe
- NumPy
- Unity 6 (URP)

# Arquitectura

```
Gesture3D/

├── src/
│   ├── vision/
│   ├── gestures/
│   ├── communication/
│   ├── experiments/
│   └── main.py
│
├── assets/
├── docs/
├── unity/
│
├── requirements.txt
└── README.md

Objetivos:

- Crear el proyecto en Unity.
- Establecer comunicación Python ↔ Unity.
- Controlar un cubo 3D mediante la posición de la mano.

---

# Próximos objetivos

- Reconocimiento de gestos.
- Control de un cubo 3D.
- Rotación de objetos.
- Interacción con objetos mediante gestos.