# Prompt para Claude in Chrome: configurar Meta para automatizar

Pégalo en un chat de Claude con la extensión Claude in Chrome conectada (el mismo con el que creaste las cuentas).

---

Ya creamos la Página de Facebook "Pieza Clave" y el Instagram @piezaclave.valencia. Ahora ayúdame a dejar configurado todo Meta para automatizar la tienda. Tú navegas y llenas; yo me encargo de contraseñas, códigos de verificación, captchas, datos de pago y de aceptar términos. Cuando llegues a uno de esos pasos, detente y avísame.

REGLAS
- No publiques nada, no lances anuncios y no gastes dinero. Todo lo que tenga "Publicar" o "Activar campaña" lo dejas en borrador y me avisas.
- No cambies nada de mi perfil personal.
- Antes de cada paso dime en una línea qué vas a hacer. Si algo no existe en mi cuenta o en Venezuela, dímelo y sigue con lo siguiente, sin inventar un rodeo.
- Nunca copies tokens, contraseñas ni códigos en el chat.

DATOS DE LA TIENDA (úsalos en todas las respuestas automáticas)
- Pieza Clave: herramientas para el carro, el taller y el patio.
- Local: Calle 181, Naguanagua, Carabobo (en Google Maps: Multitienda JM) https://maps.app.goo.gl/8KeBiwpumrtoUD416
- Delivery en Valencia con costo según la zona.
- Pago: efectivo, transferencia o pago móvil.
- Garantía: 1 mes en casi todos los productos.
- Precios confirmados: gato hidráulico 2 t 42$, kit de adaptadores de impacto 20$, llaves combinadas 8–24 mm 20$, reloj de refrigeración con mangueras 38$. Para lo demás: "te confirmo el precio por aquí".
- Horario y número de WhatsApp: pregúntamelos al empezar.

PASOS
1. Portafolio comercial (business.facebook.com): crea o revisa el portafolio "Pieza Clave" y agrega la Página, el Instagram y (si lo tengo) el WhatsApp Business. Verifica que yo sea administrador con control total.

2. Meta Business Suite → Planificador: confirma que puedo programar publicaciones, reels e historias para Facebook e Instagram a la vez. Si las historias no se pueden programar en Instagram desde mi cuenta, dímelo.

3. Bandeja de entrada → Respuestas automáticas, para Messenger e Instagram:
   - Mensaje de bienvenida: "¡Hola! Gracias por escribir a Pieza Clave 🔧 Cuéntanos qué herramienta buscas o qué carro tienes y te decimos cuál te sirve."
   - Preguntas frecuentes con respuesta, usando los datos de arriba: ¿Precio?, ¿Dónde están?, ¿Hacen delivery?, ¿Formas de pago?, ¿Garantía?, ¿Horario?
   - Respuestas por palabra clave: "precio", "delivery", "dirección/ubicación", "pago", "garantía".
   - Mensaje de ausencia fuera del horario.
   - Si existe la opción "comentario a mensaje privado", configúrala: cuando alguien comente PRECIO o INFO en un post o reel, que reciba por mensaje privado el precio (si está confirmado) y el enlace de WhatsApp. Muéstrame el texto antes de activarlo.

4. Moderación de comentarios: en Facebook e Instagram activa el filtro de palabras ocultas y el de groserías. Agrega a la lista de bloqueo palabras de spam típicas ("gana dinero", "inversión", "crypto", "link en mi perfil", "promoción gratis").

5. Administrador de anuncios:
   - Revisa que exista una cuenta publicitaria a nombre de Pieza Clave, con moneda USD y zona horaria de Caracas. El método de pago lo cargo yo.
   - Crea un público guardado: personas de 20 a 60 años en un radio de 15 km alrededor de Naguanagua/Valencia, con intereses en automóviles, mecánica, herramientas y bricolaje.
   - Deja en BORRADOR una campaña de tráfico a mensajes (WhatsApp o Instagram Direct) llamada "Gato hidráulico – reel A", con ese público, presupuesto de 3$ por día durante 7 días y ubicaciones en Reels e historias de Instagram y Facebook. El video lo subo yo después. No la publiques.

6. Commerce Manager (catálogo): revisa si puedo crear un catálogo para la Página y el Instagram desde Venezuela. Si se puede, crea el catálogo "Pieza Clave" vacío y dime cómo cargar productos. Si no está disponible, dímelo. Nota: Marketplace no tiene herramienta oficial para publicar automáticamente; esas publicaciones las hago yo a mano. No intentes automatizarlo.

7. Acceso para publicar por API (para que otro asistente publique automáticamente):
   - En developers.facebook.com crea una app tipo "Empresa" llamada "Pieza Clave Publicador", conectada al portafolio.
   - Agrega los productos "Instagram" (API de Instagram con inicio de sesión de Facebook) y "Facebook Login para empresas".
   - Pide los permisos: instagram_basic, instagram_content_publish, instagram_manage_comments, instagram_manage_messages, pages_show_list, pages_read_engagement, pages_manage_posts, pages_manage_engagement, pages_messaging, business_management.
   - En el portafolio crea un **usuario del sistema** con rol de administrador, asígnale la Página, el Instagram y la app, y genera un token con esos permisos y sin vencimiento. Cuando aparezca el token, NO lo leas ni lo copies: dime que lo guarde yo en un lugar seguro.

8. Al final dame un resumen con:
   - Qué quedó listo y qué falta.
   - Los identificadores (no son secretos): ID del portafolio, ID de la Página, ID de la cuenta de Instagram, ID de la cuenta publicitaria, ID del catálogo (si se creó) e ID de la app.
   - Cualquier aviso o restricción que haya mostrado Meta.
