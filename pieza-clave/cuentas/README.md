# Cuentas de Pieza Clave: qué crear y cómo automatizar

## 1. Lo que creas tú (15 minutos, una sola vez)

Meta exige que una persona real cree y verifique las cuentas (correo, teléfono, código y control anti-robot), así que este paso no se puede automatizar. Tenlo a mano: un correo de la tienda, tu teléfono y esta carpeta.

### a) Página de Facebook "Pieza Clave"
1. Desde tu perfil personal: **Menú → Páginas → Crear página**.
2. Nombre: `Pieza Clave` · Categoría: `Tienda de herramientas` (o "Ferretería").
3. Descripción: `Herramientas para el carro, el taller y el patio. Valencia, Carabobo. Escríbenos y te decimos cuál te sirve. Entregas en Valencia.`
4. Foto de perfil: `../logo-v2/foto-perfil.png` · Portada: `portada-facebook.png` (esta carpeta).
5. Botón de acción: **Enviar mensaje de WhatsApp** con el número de la tienda.
6. Ubicación: `Calle 181, Naguanagua, Carabobo` (en Google Maps aparece como *Multitienda JM*: https://maps.app.goo.gl/8KeBiwpumrtoUD416). Delivery: costo según la zona.

### b) Instagram @piezaclave.valencia
1. Crea la cuenta con el correo de la tienda; usuario `piezaclave.valencia`.
2. **Configuración → Tipo de cuenta → Cuenta profesional → Empresa**, categoría "Tienda de herramientas".
3. Foto: `../logo-v2/foto-perfil.png`.
4. Biografía (cópiala tal cual, 125 caracteres):
   ```
   🔧 Taller · Taller pro · 🌱 Exterior · ⚡ Eléctricas
   📍 Valencia, Carabobo · 🚚 Entregas
   💬 Escríbenos y te decimos cuál te sirve 👇
   ```
5. Enlace: `https://wa.me/58XXXXXXXXXX` (tu número sin el 0 inicial).
6. **Conecta Instagram con la página de Facebook** (Configuración → Centro de cuentas). Esto es lo que permite programar y automatizar las dos a la vez.
7. Destacadas: portadas en `../destacadas/` (Taller, Exterior, Energía/Eléctricas, Entregas, Clientes).

### c) WhatsApp Business (recomendado)
Con el mismo número: perfil de empresa con el logo y la descripción de arriba, y un **catálogo** con los productos usando las imágenes `../marketplace/<producto>/1-principal.png`.

### d) Marketplace
Las publicaciones de Marketplace salen de **tu perfil personal** (Meta no deja publicar ahí desde una página ni con programas automáticos). Con el kit ya hecho son unos 3 minutos por producto:
1. **Marketplace → Crear publicación → Artículo en venta**.
2. Sube las 3 imágenes de `../marketplace/<producto>/` en orden (1, 2, 3).
3. Pega título, precio, categoría y descripción de `../marketplace/textos-marketplace.md`.
4. Ubicación: Naguanagua, Carabobo. Publica.

## 2. Lo que se automatiza

| Qué | Cómo | Quién |
|---|---|---|
| Posts y reels de Instagram y Facebook | **Nivel 1 (hoy, sin código):** en Meta Business Suite → Planificador, subes la semana entera y queda programada. **Nivel 2 (automático):** un programa publica cada post a su hora directo desde la carpeta del proyecto, por la API oficial de Meta. | Nivel 1: tú, ~20 min por semana. Nivel 2: lo monto yo |
| Diseño de posts, fichas, imágenes de Marketplace, reels | Ya está automatizado con los generadores de esta carpeta | Yo |
| Textos y descripciones | Generados por producto | Yo |
| Marketplace | Manual con el kit (no hay API oficial para particulares) | Tú, ~3 min por producto |

### Para el nivel 2 necesito, una sola vez
1. Instagram profesional conectado a la página (paso 1b.6).
2. Una app en **developers.facebook.com** (tipo "Empresa") con los permisos `instagram_content_publish`, `instagram_basic`, `pages_manage_posts` y `pages_read_engagement`, y un **token de acceso de larga duración**.
3. Me pasas el token por el **formulario seguro** que te aparece cuando te lo pida (nunca por el chat).

Con eso preparo el programa que lee el calendario de la semana, publica posts, carruseles y reels en Instagram y Facebook a la hora indicada, y te avisa cuando sale cada uno.
