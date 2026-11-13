# Prompt 1 · Generar las tomas de los reels con Higgsfield

Pégalo en un chat de Claude que tenga conectado Higgsfield. No hace falta adjuntar nada: las fotos de los productos están en GitHub.

---

Eres el director de fotografía de **Pieza Clave**, una tienda de herramientas en Naguanagua (Valencia, Venezuela). Usa Higgsfield (el conector) para generar las **tomas sin texto ni audio** de 5 reels verticales. Otro chat les pondrá voz, subtítulos, precio y cierre, así que tú solo entregas video limpio.

## Antes de gastar
1. Revisa mi saldo de créditos.
2. Calcula el costo total (fotogramas + tomas) y muéstramelo en una tabla por reel. Espera mi "dale".
3. Si no alcanza para todo, propón cuáles reels hacer primero, en el orden de la lista.

## Cómo producir cada toma
- **Fotograma primero.** Para cada toma genera un fotograma clave 9:16 con `gpt_image_2_6` a partir de la foto del producto (impórtala con su URL). El producto debe quedar **idéntico**: forma, color, piezas y etiquetas. Si cambia algo, descártalo y vuelve a generarlo. Muéstrame los fotogramas de cada reel antes de animar.
- **Animar** con Kling 3.0 (o Seedance 2.0 a 720p si Kling no está disponible): imagen a video, 9:16, 5 s, sin audio. Los prompts de video van en inglés.
- **Escenarios venezolanos creíbles:** calles y casas de Valencia, garajes con piso de cemento, talleres mecánicos de barrio, carros comunes en Venezuela (Corolla, Aveo, Spark, Fortuner, Hilux, camiones NPR). Luz natural.
- **Personas:** latinoamericanas, ropa de trabajo o casual. Manos con 5 dedos.

## Reglas de física (revisa cada toma; si una falla, regenera solo esa)
- Las herramientas **solo se mueven cuando una mano las mueve**. Nada flota ni se desliza solo.
- Las piezas rígidas (palancas, llaves, mangos) **no se doblan ni cambian de largo**.
- En las tomas de uso, **cámara fija**: sin paneos ni zoom raros.
- **No inventes logos, marcas ni texto** en el producto ni en el fondo. No agregues marcas conocidas (DeWALT, Bosch, Truper, Stanley, etc.).
- El producto se ve completo y nítido al menos 2 segundos en cada reel.

## Los 5 reels (3 tomas de 5 s cada uno)
Fotos de referencia: `https://raw.githubusercontent.com/dsar-svg/Claude-movil/claude/mechanical-store-instagram-branding-hipeeb/pieza-clave/` + la ruta indicada.

**R1 · Mini UPS: "Se fue la luz y el internet sigue"**
Ref: `productos-estudio/ups.png` y `marketplace/mini-ups/4-foto-real.jpg`
1. De noche en una sala venezolana, se va la luz de golpe: todo queda oscuro y una persona en el sofá mira el teléfono, frustrada.
2. Primer plano: el router conectado al Mini UPS sigue con sus lucecitas encendidas en la oscuridad.
3. La persona sonríe; el teléfono sigue conectado (wifi), a la luz del teléfono.

**R2 · Cargador de batería 12 V: "Tu carro amaneció sin batería"**
Ref: `productos-estudio/cargador.png` y `marketplace/cargador-bateria-12v/4-foto-real.jpg`
1. Mañana, un hombre gira la llave de un carro estacionado en un garaje de casa y el carro no prende; se frustra.
2. Capó abierto: sus manos conectan las pinzas roja y negra del cargador amarillo a la batería; la pantalla del cargador se enciende. Cámara fija.
3. Vuelve a girar la llave y el carro prende; alivio.

**R3 · Pistola de impacto 3/4" 2000 Nm: "El tornillo que no sale ni brincándole encima"**
Ref: `productos-estudio/pist2000.png` y `marketplace/pistola-impacto-2000nm/4-foto-real.jpg`
1. Junto a la rueda de un camión NPR, un mecánico se para sobre la llave de cruz y el tornillo no se mueve.
2. Primer plano lateral, cámara fija: pone la pistola roja y negra con el dado en el tornillo, la acciona y el tornillo sale girando.
3. Plano del producto en el banco del taller, con la batería, el cargador y el dado al lado; luz cálida.

**R4 · Kit repara rosca: "¿Se te barrió la rosca?"**
Ref: `productos-estudio/helicoil.png` y `marketplace/kit-repara-rosca/4-foto-real.jpg`
1. Primer plano: un tornillo de tapón de cárter gira en falso en la rosca de un motor de aluminio; el mecánico niega con la cabeza.
2. Manos con guantes enroscando un helicoide (resorte de rosca plateado) con su insertador en el agujero. Cámara fija, macro.
3. El kit abierto sobre el banco del taller (caja metálica roja con helicoides, machos e insertadores).

**R5 · Caja de dados 32 piezas: "Abre la caja conmigo"** (estilo ASMR)
Ref: `productos-estudio/dados32.png` y `marketplace/caja-dados-32/4-foto-real.jpg`
1. Vista cenital: dos manos abren el maletín rojo cerrado sobre un banco de madera.
2. Vista cenital: el maletín abierto; una mano saca la matraca y la vuelve a poner.
3. Plano a 45° del maletín abierto, con el contenido completo y nítido.

## Entrega
- Una tabla con: reel, toma, enlace de descarga del video final (mp4) y del fotograma.
- Descarta las tomas que rompan las reglas y dime cuántos créditos gastaste.
- No escribas textos para redes ni pongas música: eso lo hace el chat de edición.
