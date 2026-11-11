# Reel con anuncio: gato hidráulico 2 t

| Archivo | Qué es |
|---|---|
| `reel-gato-A.mp4` | Versión A, 15,5 s, 1080 × 1920. Gancho: "¿Todavía con el gato de tijera?" |
| `reel-gato-B.mp4` | Versión B, igual pero con el gancho "¿Se te espichó un caucho?" |
| `tomas/` | Las 4 tomas de video sin texto (Kling 3.0 Pro en ElevenLabs), por si quieres reeditar en CapCut. |
| `fotogramas/` | Los fotogramas clave (GPT Image 2.6) desde los que se animaron las tomas. |
| `musica.mp3`, `sfx-bombeo.mp3` | Música instrumental y efecto del bombeo (ElevenLabs). |
| `edit_reel.py` | Script de ffmpeg que arma el reel: espera `clips/v1..v4.mp4`, `ov/*.png` y `audio/` junto a él. |

Cómo se hizo: el gato y su estuche salen de la foto real del producto. Primero se generaron fotogramas fieles al producto en el mismo garaje y luego Kling animó entre ellos (inicio y final fijos), para que el gato no cambie durante el movimiento.

Antes de publicar: activa la etiqueta "Información de IA" en Instagram y revisa que el gato se vea igual al que entregas.
