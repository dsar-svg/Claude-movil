# Prompt 2 · Editar los reels

Pégalo en una sesión de **Claude Code** con este repositorio (`dsar-svg/Claude-movil`, rama `claude/mechanical-store-instagram-branding-hipeeb`) y con ElevenLabs conectado. Agrega al final la tabla de enlaces que te dio el chat de Higgsfield.

---

Eres el editor de video de **Pieza Clave** (herramientas para el carro, el taller y el patio; Calle 181, Naguanagua, Valencia, Venezuela). Monta los reels verticales a partir de las tomas de Higgsfield que pego al final y déjalos listos para la publicación automática.

## Material del repositorio
- Referencia de estilo: `pieza-clave/semana-1/reel-gato/reel-gato-A.mp4` y su editor `pieza-clave/semana-1/reel-gato/editor.py`. Este último usa rutas de otra sesión: cámbialas por las del repositorio.
- Fuentes: `pieza-clave/marca/fuentes/`. Títulos en Archivo 125 Black (`Archivo_wdth_wght_125_900.ttf`), subtítulos en Barlow Condensed 800 y textos en Barlow.
- Logos: `pieza-clave/logo-v2/` (usa `logo-horizontal-negativo.svg` sobre fondo oscuro).
- Colores: azul acero #12343b, naranja #f26a1b, grafito #161b1d, gris claro #eef1f1.
- Música y efectos: `pieza-clave/semana-1/reel-gato/audio/` (musica.mp3, whoosh.mp3, pop.mp3).

## Cada reel
- **Formato:** 9:16, 1080 × 1920, 30 fps, H.264 + AAC, entre 12 y 18 s.
- **Estructura:** gancho (0–3 s) → producto en acción → cierre de 3 s.
- **Voz en off:** ElevenLabs, voz **"José Manuel"** (búscala con la lista de voces), modelo `eleven_multilingual_v2`, **sin etiquetas** de emoción. Español venezolano natural. Normaliza la voz y baja la música mientras habla.
- **Subtítulos** palabra por palabra en mayúsculas, de 2 a 3 palabras a la vez, con la palabra que suena en naranja. Ponlos en la zona segura: lejos de los 250 px de abajo y de la franja derecha.
- **Cierre:** fondo azul acero con el logo, el nombre del producto, la etiqueta naranja inclinada de precio ("PRECIO 45$"), "Escríbenos por mensaje", "@piezaclave.valencia" y "Lun a sáb · 8 a. m. a 5 p. m.". Abajo, en pequeño: "Imágenes generadas con IA". **No pongas WhatsApp.**
- **Portada:** un JPG 1080 × 1920 con el gancho grande y el producto.
- Revisa cada reel viendo fotogramas sueltos (al inicio, al medio, en el cierre) antes de darlo por bueno.

## Guiones (ajústalos a la duración de las tomas)
- **R1 · Mini UPS (45$):** "¿Se fue la luz y te quedaste sin internet? Con este mini UPS tu router sigue prendido de seis a ocho horas. Lo conectas y listo. Pieza Clave, escríbenos y te lo llevamos." Gancho en pantalla: "¿SE FUE LA LUZ?"
- **R2 · Cargador de batería 12 V (20$):** "¿Tu carro amaneció sin batería? Este cargador de doce voltios y seis amperios carga baterías de carro, de moto y de gel. Lo conectas y en un rato vuelves a arrancar. Pieza Clave." Gancho: "¿AMANECIÓ SIN BATERÍA?"
- **R3 · Pistola de impacto 3/4" 2000 Nm (155$):** "Ese tornillo que no sale ni brincándole encima a la llave… con esta pistola de impacto de dos mil newton metro sale en un segundo. Trae dos baterías, cargador y dado. Pieza Clave." Gancho: "¿NO SALE NI BRINCÁNDOLE?"
- **R4 · Kit repara rosca (40$):** "¿Se te barrió la rosca? No cambies la pieza. Con este kit de helicoides le haces una rosca nueva: del cárter, de la bujía o del bloque. Pieza Clave, escríbenos y te decimos cuál medida te sirve." Gancho: "¿SE TE BARRIÓ LA ROSCA?"
- **R5 · Caja de dados 32 piezas (30$):** "Abre la caja conmigo. Treinta y dos piezas: dados, matraca, extensiones y cardán, todo en su maletín. Lo básico para tu carro. Pieza Clave." Gancho: "ABRE LA CAJA CONMIGO"

## Entrega y publicación
1. Guarda cada reel en `pieza-clave/reels/<slug>/reel.mp4` y su portada en `pieza-clave/reels/<slug>/portada.jpg`. Slugs: `mini-ups`, `cargador-bateria`, `pistola-2000nm`, `repara-rosca`, `caja-dados-32`.
2. Agrega cada reel a `pieza-clave/automatizacion/calendario.json` con `"tipo": "reel"`, `"archivos": ["reels/<slug>/reel.mp4"]`, `"portada": "reels/<slug>/portada.jpg"` y las dos plataformas. Prográmalos a las 19:30 (-04:00) en días que estén libres en el calendario, uno cada dos días, a partir de mañana. El texto debe tener 3 líneas: el gancho, el precio y "Escríbenos por mensaje", más "📍 Calle 181, Naguanagua · 🕗 Lun a sáb, 8 a. m. a 5 p. m.", "🚚 Delivery según la zona" y los hashtags que usa el calendario.
3. Corre `python3 pieza-clave/automatizacion/publicador.py preparar` y `python3 pieza-clave/automatizacion/publicador.py estado`.
4. Haz commit y push a la rama. Después corre `python3 pieza-clave/automatizacion/publicador.py probar <id>` en cada reel: crea el contenedor en Instagram sin publicarlo y confirma que Meta acepta el video.
5. Dame una tabla con: reel, duración, fecha programada y si pasó la prueba.

## Tomas de Higgsfield
(pega aquí la tabla con los enlaces)
