# Control por Gestos – V1.1

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
