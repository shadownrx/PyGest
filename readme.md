<<<<<<< HEAD
# Pygest

# 1. Introducción

El presente proyecto describe las tareas de análisis, especificación de requerimientos, diseño, implementación y testing del sistema denominado Pygest.
Pygest es un sistema que permite controlar tu computadora con gestos de la mano usando visión por computadora, a través de la cámara web, se detectan posiciones de los dedos para mover el mouse, hacer click y abrir aplicaciones como el bloc de notas o el navegador.

# 2. Problématica

Actualmente no existe un sistema de gestor de movimientos con funcionalidades desarrolladas de manera completa, no obstante a través de información recopilada se pretende que el usuario pueda llevar a cabo la apertura del navegador Google con un gesto de me gusta ( pulgar arriba), abrir un bloc de notas con la palma abierta o mostrar Fotogramas por segundo (FPS) en nuestras pantallas por segundo entre otras funcionalidades.
Ante la evidente necesidad de concretar y otorgar soluciones, se tomó la decisión de diseñar el módulo de apertura de navegadores, los módulos de apertura de bloc de notas, modulo de clickeos con índice y pulgar y el módulo de movimiento del mouse con el dedo índice.

# 3. Objetivos

# 3.1 Objetivo General

El objetivo general del Sistema Pygest es adquirir la experiencia necesaria donde se pueda mejorar el realismo visual en cualquier contexto tales como en videojuegos, cinemáticas, animación ofreciendo al usuario un entorno mas agradable y prolongada.

# 3.2 Objetivo Específico

1. Recopilar información a través de entrevistas para tener un panorama visible de aquellos elementos que son importantes para un contenido más específico.
2. Obtener la información para el análisis y la redacción de los requisitos funcionales y no funcionales necesarios para el Sistema de Ayuda Virtual.
3. Diseñar la arquitectura del sistema para una definición de una estructura, el comportamiento y las demás vistas que puedan tener. Con esto se debe tener en cuenta que debe ser adaptable a nuevas necesidades que puedan surgir.
4. Diseñar los prototipos o el módulo solución que cumpla lo solicitado con lo redactado en los requerimientos.
5. Realizar pruebas manuales sobre los diferentes módulos para verificar que los resultados obtenidos sean lo que se esperan documentando.



=======
# Control por Gestos – V1.1
>>>>>>> af6dd424b9b0bda2226d98d2027d643940fbc7c4

¡Bienvenido a **Control por Gestos**!  
Esta aplicación permite **controlar el mouse, abrir aplicaciones y manejar presentaciones** usando gestos de la mano capturados con la cámara.

## 🔹 Características principales

- Detección de manos con **MediaPipe**.
- Control del **mouse**:
  - Mover cursor con el **índice**.
  - **Clic izquierdo** con gesto “pinch” (índice + pulgar).
  - **Clic derecho** con gesto ✌️ (índice + medio levantados).
  - **Arrastrar** con puño cerrado ✊.
  - **Scroll** vertical con índice + medio levantados y moviéndose.
- Abrir aplicaciones configurables desde `gestos_config.json`:
  - Ej: Bloc de notas, navegador Chrome, Spotify.
- Control de presentaciones:
  - Avanzar y retroceder diapositivas (PowerPoint, PDF).
- **FPS en pantalla** para monitorear rendimiento.
- Gestos y cooldowns configurables mediante JSON.
- Estructura modular: `main.py`, `gestos.py`, `acciones.py`, `detector_manos.py`, `utils.py`.

---

## 🔹 Gestos disponibles (V1.1)

| Gesto | Acción | Descripción |
|-------|--------|-------------|
| Índice levantado | Mover mouse | Control del cursor con el dedo índice |
| Pinch (índice+pulgar) | Clic izquierdo | Hace un clic |
| ✌️ Índice + medio | Clic derecho | Hace clic derecho |
| Puño cerrado ✊ | Drag | Mantiene el clic para arrastrar |
| Índice + medio moviéndose | Scroll | Desplaza hacia arriba/abajo |
| Palma abierta | Abrir aplicación | Configurable en `gestos_config.json` |
| Pulgar arriba 👍 | Abrir aplicación | Configurable en JSON |
| Mano derecha | Avanzar presentación | PowerPoint / PDF |
| Mano izquierda | Retroceder presentación | PowerPoint / PDF |

---

## 🔹 Configuración de gestos

El archivo `gestos_config.json` permite **personalizar qué gesto hace qué acción**:

```json
{
  "gestos": {
    "palma_abierta": { "accion": "abrir_app", "programa": "notepad" },
    "like": { "accion": "abrir_app", "programa": "chrome" },
    "mano_derecha": { "accion": "presentacion", "direccion": "siguiente" },
    "mano_izquierda": { "accion": "presentacion", "direccion": "anterior" }
  },
  "cooldowns": { "clic": 0.5, "abrir_app": 1.0, "presen_
