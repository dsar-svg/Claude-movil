# Prompt para un chat de Claude con Higgsfield conectado

Adjunta solo la foto del gato y pega el texto de abajo.

---

Eres mi director creativo y editor de video. Usa Higgsfield (el conector) para hacer, de principio a fin, un **reel publicitario vertical 9:16 de 15 a 20 segundos** para Instagram y Facebook, listo para pautar. Te adjunto la foto real del producto: es la única referencia del producto y debe salir idéntico en todas las tomas.

## Contexto
- Tienda: **Pieza Clave**, herramientas para el carro, el taller y el patio. Local en Calle 181, Naguanagua (Valencia, Carabobo, Venezuela). Delivery con costo según la zona.
- Producto: **gato hidráulico tipo caimán de 2 toneladas** (rojo, asa amarilla, ruedas negras, asiento redondo negro, palanca larga roja recta). Sube de 12,5 a 30 cm. Trae estuche plástico gris y cabe en la maleta del carro.
- Precio: **42$**. Pago en efectivo, transferencia o pago móvil. Garantía de 1 mes.
- Público: conductores venezolanos que hoy cambian cauchos con el gato de tijera que trae el carro.
- Colores de marca: azul acero #12343b, naranja #f26a1b, grafito #161b1d, gris claro #eef1f1. Tipografía de títulos: una sans muy gruesa y ancha (tipo Archivo Black), en mayúsculas. No inventes un logo: escribe "PIEZA CLAVE" en texto.

## Estructura (problema → solución → prueba → oferta)
1. **Gancho (0-3 s):** calle soleada, un hombre sudado de rodillas junto a un carro plateado con un caucho espichado gira la manivela del gato de tijera en círculos, sin avanzar. Texto: "¿Todavía con el gato de tijera?"
2. **Presentación (3-5 s):** corte seco al garaje; giro de cámara alrededor del gato hidráulico. Texto: "Gato hidráulico 2 toneladas".
3. **Lo mete (5-8 s):** de perfil, cámara fija; él empuja la palanca con los brazos y el gato rueda en línea recta hasta quedar bajo el punto de apoyo.
4. **Prueba (8-12 s):** de perfil, cámara fija; bombea la palanca tres veces y el carro sube de forma claramente visible, la rueda se despega del piso. Texto con contador: "12,5 → 30 cm".
5. **Seguridad (12-14 s):** coloca un burro (soporte metálico) bajo el carro. Texto: "Y siempre con burros".
6. **Oferta (14-18 s):** guarda el gato en su estuche dentro de la maleta. Cierre sobre fondo azul acero: "Gato hidráulico 2 t · 42$", "Escríbenos por WhatsApp", "Entregas en Valencia".

## Cómo producirlo
1. **Fotogramas primero:** con la foto adjunta genera un fotograma clave por toma con gpt_image_2_6, en 9:16, editando o componiendo a partir de la foto para que el gato no cambie. Para la toma 4 haz dos fotogramas: el carro abajo (inicio) y el carro ya levantado con la palanca abajo (final). Muéstrame los fotogramas antes de animar.
2. **Animar:** imagen a video con Seedance 2.0 (o Kling 3.0 si es más barato), 9:16, 720p, 5 s, sin audio, usando el fotograma como `start_image` (y `end_image` en la toma 4). Prompts de video en inglés.
3. **Reglas de física (son las que fallaron en versiones anteriores, revísalas en cada toma):**
   - El gato de tijera se sube **girando la manivela en círculos**, nunca bombeando.
   - El gato hidráulico **solo se mueve cuando la persona lo empuja**; las manos van pegadas a la palanca y se mueven con ella.
   - La palanca es rígida: **no se dobla, no se estira, no cambia de largo**.
   - En las tomas 3 a 5, **cámara fija**: sin paneos, sin zoom, sin que el gato se desplace hacia los lados.
   - El carro tiene que subir de forma evidente en la toma 4.
   - Si una toma rompe alguna regla, descártala y vuelve a generar solo esa.
4. **Voz en off:** español latinoamericano **neutro y natural**, hombre de unos 35 años, tono cercano, como un amigo que recomienda algo. Nada de voz de locutor exagerada ni acento argentino, colombiano o mexicano marcado. Muéstrame 2 o 3 voces antes de elegir. Guion (unos 17 s):
   > "¿Todavía cambiando el caucho con el gato de tijera? Con este gato hidráulico de dos toneladas, lo metes debajo del carro, bombeas, y sube de doce y medio a treinta centímetros. Trae su estuche y cabe en la maleta. Pieza Clave: escríbenos por WhatsApp y te lo llevamos en Valencia."
5. **Música y sonido:** instrumental moderna con ritmo, sin letra, que baje cuando habla la voz. Efecto "whoosh" en los cortes y sonido hidráulico al bombear.
6. **Montaje (usa el flujo video-montage de Higgsfield):** corta al ritmo de la voz; subtítulos en mayúsculas de 2 a 3 palabras, con la palabra que se dice resaltada en naranja #f26a1b, en el tercio inferior. Una ✕ roja sobre el gato de tijera al decir "tijera". Textos en pantalla dentro de la zona segura de Reels (lejos de los 250 px de abajo y de la columna derecha). Cierre de 3 segundos con precio y WhatsApp.

## Presupuesto y control
- Antes de gastar, calcula y muéstrame el costo total en créditos (fotogramas + tomas + voz + música) y espera mi visto bueno.
- Genera de a una toma y revísala contra las reglas antes de seguir.
- Si te quedas sin créditos o algo falla, dime en qué paso quedaste.

## Entrega
- El MP4 final (1080 × 1920) con voz, música y subtítulos.
- Las tomas sueltas sin texto.
- Una portada 9:16 con "¿Todavía con el gato de tijera?".
- El texto del anuncio para Instagram (máximo 3 líneas, con precio y llamado a WhatsApp).
