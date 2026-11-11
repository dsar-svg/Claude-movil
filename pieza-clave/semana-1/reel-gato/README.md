# Reel con anuncio: gato hidráulico 2 t

| Archivo | Qué es |
|---|---|
| `reel-gato-A.mp4` | Versión A, 17,0 s, 1080 × 1920, con voz. Gancho: "¿Todavía cambiando el caucho con el gato de tijera?" |
| `reel-gato-B.mp4` | Versión B, 17,7 s. Gancho: "¿Se te espichó un caucho y el gato de tijera no sube?" |
| `tomas/` | Las tomas sin texto: gancho girando la manivela del gato de tijera (Veo 3.1), plano de producto, el hombre empuja el gato bajo el carro (Veo 3.1), bombeo de perfil (Veo 3.1), maleta (Kling 3.0 Pro). |
| `fotogramas/` | Fotogramas clave fieles al producto (GPT Image 2.6) desde los que se animó cada toma. |
| `audio/` | Voz en off (ElevenLabs v4, voz "Memo M", español latino neutro), música, efectos y `tiempos-voz.json` con el tiempo de cada palabra. `muestras-voz-neutra.mp3` trae el mismo texto con cuatro voces neutras en este orden: Memo M, Eduardo, Claus, Pedro Alejandro. `voz-anterior/` guarda las voces "Fernando" y "Máximo" y las muestras venezolanas. |
| `editor.py` | Compositor cuadro a cuadro (Python + ffmpeg): subtítulos palabra por palabra, sello ✕, insignia 2 t, barra de altura animada, check, cierre con botón de WhatsApp, música que baja bajo la voz. |
| `v1-sin-voz/` | Versiones y tomas descartadas (bombeo frontal, gato de tijera "bombeado", empuje con reencuadre). |

Antes de publicar: activa la etiqueta "Información de IA" en Instagram y revisa que el gato se vea igual al que entregas.
