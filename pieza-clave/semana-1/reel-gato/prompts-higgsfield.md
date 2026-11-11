# Prompts para generar el reel del gato en Higgsfield

## Opción A: todo de una vez (Marketing Studio)
- Herramienta: **Marketing Studio → Video**. Formato 9:16, 1080p, duración 15 s.
- Producto: sube `../../productos-estudio/gato-pack.png` (foto de estudio del gato).
- Prompt:

```
Vertical 9:16 product ad for a red hydraulic floor jack (2 ton) sold by a tool store in Valencia, Venezuela. Fast-paced, realistic, warm late-afternoon light, handheld documentary feel.
Shot 1 (0-3s): sunny street, a sweaty man kneels by a silver compact car with a flat tire and slowly turns the crank of a small black scissor jack in circles, frustrated, wiping his forehead.
Shot 2 (3-6s): hard cut to a clean home garage; the red hydraulic floor jack rolls into frame on its wheels, camera orbits around it, glossy red paint, yellow carry handle.
Shot 3 (6-10s): side view, the man kneels and pumps the long straight red handle up and down with both hands, three full strokes; the front of the car rises clearly, the tire lifts off the floor.
Shot 4 (10-12s): he slides a metal jack stand under the car next to the jack.
Shot 5 (12-15s): he puts the jack into its grey plastic carrying case and closes it inside a car trunk, smiles at camera.
Keep the jack exactly like the product image: red body, yellow carry handle, black wheels, round black saddle, long red handle that never bends or changes length. No text, no logos, no subtitles.
```

## Opción B: toma por toma (más control, recomendado)
- Modelo: **Seedance 2.0** (o Kling 3.0 para gastar menos). 9:16, 720p, 5 s, sin audio.
- En cada toma sube las imágenes indicadas como **fotograma inicial** y **fotograma final** (están en `fotogramas/` y `../../productos-estudio/`).
- Negativo para todas (si el modelo lo acepta):
```
handle bending, handle stretching, jack changing shape or color, jack moving by itself, frozen hands, camera shake, extra fingers, text, logos, subtitles
```

### Toma 1: gancho, gato de tijera (3 s)
Fotograma inicial: `fotogramas/f1_b.jpg`
```
Handheld documentary shot on a hot sunny street. The sweaty, tired man keeps kneeling by the silver car and turns the bent crank of the small scissor jack round and round in continuous circles with his right hand, like winding a hand crank, the screw turning slowly. He breathes hard, shakes his head and wipes sweat from his forehead with his forearm, then keeps cranking. The scissor jack barely rises. Realistic motion.
```

### Toma 2: presentación del producto (4 s)
Fotograma inicial: `../../productos-estudio/gato-pack.png` (o `../escenas-ia/gato916a.jpg`)
```
Slow cinematic orbit around the red hydraulic floor jack standing on the concrete floor of a clean home garage, warm late-afternoon light through a roll-up door, glossy red paint reflecting the light, shallow depth of field. The jack stays completely still and identical; only the camera moves. Premium product commercial look.
```

### Toma 3: lo mete bajo el carro (4 s)
Fotograma inicial: `fotogramas/e1_b.jpg`
```
Tripod shot, the camera is completely static, no pan and no zoom. The man stays kneeling on both knees, holding the end of the long straight red handle low with both hands. He leans forward and pushes in one steady motion; the jack rolls forward on its black wheels in a straight line, in under the side of the silver car, until its round saddle sits below the jack point. The jack only moves while he pushes it. The handle stays straight and the same length.
```

### Toma 4: bombea y el carro sube (5 s)
Fotograma inicial: `fotogramas/p1_b.jpg` · Fotograma final: `fotogramas/p2_b.jpg`
```
Static side view. The kneeling man pumps the long straight red jack handle with both hands: three full strokes, each pushing it down toward the floor and lifting it back up, his arms and shoulders visibly working. The rigid steel handle stays perfectly straight and keeps the same length. With every stroke the jack's lifting arm rises and the front of the silver car goes up, until the front tire is clearly off the ground. Realistic weight and motion.
```

### Toma 5: los burros (3 s)
Fotograma inicial: `fotogramas/p2_b.jpg`
```
Static side view. With the car already lifted on the red hydraulic jack, the man takes a grey metal jack stand from the floor and places it under the car's frame next to the jack, adjusting its height until it touches the car. The jack stays still under the car. Calm, careful, realistic.
```

### Toma 6: cabe en la maleta (4 s)
Fotograma inicial: `fotogramas/f4_b.jpg`
```
Close shot of an open car trunk. Two hands lower the grey plastic carrying case of the hydraulic jack into the trunk, slide it into place and pat it once; it fits perfectly with room to spare. Warm natural light, realistic, slight handheld movement.
```

## Después de generar
Descarga los videos y pásamelos (o súbelos a la carpeta `tomas/`). Yo los monto con la voz de José Manuel, subtítulos, la ✕ sobre la tijera, la barra de centímetros, el precio de 42$ y el cierre con WhatsApp, igual que la versión actual. La pantalla dividida "tijera vs. caimán" la armo en la edición con las tomas 1 y 4.
