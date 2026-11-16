# Herramientas de producción (para los agentes)

Todo corre desde esta carpeta, sin rutas fijas de sesión.

| Archivo | Para qué | Uso |
|---|---|---|
| `posts5.py` | Posts, carruseles e historias por categoría (semanas 1 y 2 como ejemplo de plantillas: `portada`, `ficha`, `comparar`, `lista`, `cta`) | `python3 posts5.py && node render_posts5.js posts5.json salida` |
| `market.py` | 3 imágenes cuadradas por producto para Marketplace (principal, ficha, cómo comprar). Lista de productos `P`/`NEW`, precios `PRICE` | `ONLY=ups,gato python3 market.py && node render_posts5.js market.json salida` |
| `textos_mk.py` | Regenera `../marketplace/textos-marketplace.md` | `python3 textos_mk.py` |
| `render_posts5.js` | Renderiza el JSON de páginas a PNG con Playwright | `node render_posts5.js <json> <carpeta>` |
| `reels/editor.py` | Reel 9:16 con tomas, voz, subtítulos por palabra, dato, etiqueta verde y cierre con precio. Config por reel en el diccionario `C` | Poner tomas en `reels/clips/`, voz en `reels/vo/<key>.mp3`, tiempos en `reels/words.json` (faster-whisper `small`, con audio decodificado por ffmpeg), luego `python3 reels/editor.py <key>` → `reels/out/` |
| `fonts/`, `cut/`, `fotos/`, `reel/ov/`, `reel/audio/` | Tipografías, recortes, fotos, logos y música/efectos | — |

Salidas (`salida/`, `*.json`, `reels/out/`…) están en `.gitignore`: copia a su carpeta final solo lo aprobado.
