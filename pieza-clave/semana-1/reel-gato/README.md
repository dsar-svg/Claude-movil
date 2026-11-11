# Reel con anuncio: gato hidráulico 2 t

| Archivo | Qué es |
|---|---|
| `reel-gato-A.mp4` | Versión A, 17,7 s, 1080 × 1920, con voz. Gancho: "¿Todavía cambiando el caucho con el gato de tijera?" |
| `reel-gato-B.mp4` | Versión B, 18,2 s. Gancho: "¿Se te espichó un caucho y el gato de tijera no sube?" |
| `tomas/` | Las tomas sin texto: gancho girando la manivela del gato de tijera (Veo 3.1), plano de producto, el hombre empuja el gato bajo el carro (Veo 3.1), bombeo de perfil (Veo 3.1), maleta (Kling 3.0 Pro). |
| `fotogramas/` | Fotogramas clave fieles al producto (GPT Image 2.6) desde los que se animó cada toma. |
| `audio/` | Voz en off (ElevenLabs v4, voz "Máximo", venezolano neutro), música, efectos y `tiempos-voz.json` con el tiempo de cada palabra. `muestras-voz.mp3` trae el mismo texto con tres voces venezolanas en este orden: Máximo, José Manuel, Juan. `voz-anterior/` guarda la voz "Fernando". |
| `editor.py` | Compositor cuadro a cuadro (Python + ffmpeg): subtítulos palabra por palabra, sello ✕, insignia 2 t, barra de altura animada, check, cierre con botón de WhatsApp, música que baja bajo la voz. |
| `v1-sin-voz/` | Versiones y tomas descartadas (bombeo frontal, gato de tijera "bombeado", empuje con reencuadre). |

Antes de publicar: activa la etiqueta "Información de IA" en Instagram y revisa que el gato se vea igual al que entregas.
