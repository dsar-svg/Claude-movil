# Equipo de agentes de Pieza Clave

| Agente | Dónde vive | Cuándo corre | Qué hace | Manual |
|---|---|---|---|---|
| **Director** | La conversación principal con el dueño | Cuando el dueño escribe | Coordina, revisa lo que hacen los otros, aplica cambios, aprueba con el dueño | — |
| **Cuentas** | Sesión "Pieza Clave · Agente de Cuentas" | Lun–sáb cada 2 h (8, 10, 12, 14, 16, 18) + publicación diaria 12:33 y 19:33 | Publica el calendario, responde comentarios y mensajes factuales, oculta spam, pasa ventas al dueño con aviso push | `agente-cuentas.md` |
| **Contenido** | Sesión "Pieza Clave · Agente de Contenido" | Jueves 10:17 (plan) y domingo 18:41 (reporte) | Planifica y produce la semana siguiente como **propuesta**, manda vista previa; reporte semanal | `agente-contenido.md` |
| **Marketplace** | Chat de Claude in Chrome en la PC del dueño | Sus tareas programadas | Publica tandas de 8 y renueva publicaciones | `../cuentas/prompt-publicar-marketplace.md` |

Horarios en hora de Venezuela. Base de conocimiento común: `conocimiento.md`.

## Aprobación de contenido
1. El jueves, el Agente de Contenido deja la semana siguiente en `automatizacion/calendario.json` con `"propuesta": true` (el publicador no las publica) y te manda la vista previa.
2. Respondes "ok" (o pides cambios) en esa conversación o al director.
3. Se quita `propuesta` y queda programado.

## Privacidad
El repositorio es público: ningún agente guarda textos ni nombres de clientes en archivos. `estado/comunidad.json` solo tiene huellas de los IDs atendidos.
