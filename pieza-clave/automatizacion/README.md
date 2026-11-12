# Publicación automática en Instagram y Facebook

`publicador.py` publica posts, carruseles, reels e historias en **@piezaclave.valencia** y en la **Página Pieza Clave** por la API oficial de Meta, a la hora que dice `calendario.json`.

| Archivo | Qué es |
|---|---|
| `meta.json` | IDs de la cuenta (portafolio, página, Instagram, anuncios, catálogo, app). No son secretos. |
| `calendario.json` | Qué sale y cuándo (hora de Venezuela), con el texto de cada publicación. |
| `media/` | Las imágenes en JPG (Instagram no acepta PNG). Se crean con `python3 publicador.py preparar`. |
| `estado/publicados.json` | Lo que ya salió, con el enlace. Evita publicar dos veces. |

## Cómo funciona
- Una tarea programada corre todos los días a las **12:33 y 19:33** (hora de Venezuela): publica lo que toque y guarda el estado en el repositorio.
- El token del usuario del sistema **no está en el repositorio**: lo guarda el entorno de Claude y se agrega solo a cada llamada a Meta.
- Si algo no sale a su hora (más de 12 h de retraso), queda como **VENCIDO** y no se publica solo, para que no salga fuera de contexto.

## Lo que sigue siendo manual
- **Marketplace:** Meta no permite publicarlo por programa. Usa el kit de `../marketplace/`.
- **Imágenes nuevas:** súbelas al repositorio (push) antes de su hora; el publicador usa el último commit publicado en la rama.
- **Historias con stickers** (encuestas, enlaces, preguntas): la API no los pone. Están marcadas `"manual": true`.
- **Reels sin video todavía:** el del local (lunes) y el del multiplicador (viernes).

## Comandos
```
python3 publicador.py estado               # qué salió, qué falta
python3 publicador.py verificar            # revisa token, cuentas y archivos (no publica)
python3 publicador.py probar <id>          # prepara en Instagram sin publicar
python3 publicador.py publicar --prueba    # muestra lo que publicaría ahora
python3 publicador.py publicar --id <id> --forzar   # publica una entrada ya mismo
```

## Para agregar una publicación
Agrega una entrada a `calendario.json` (`imagen`, `carrusel`, `reel` o `historia`), con los archivos relativos a `pieza-clave/`, corre `preparar` y sube los cambios a la rama.
