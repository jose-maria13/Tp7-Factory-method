# Proyecto: Ejemplo sencillo de Factory Method (Helados)

## ¿Qué resuelve?
Permite pedir distintos tipos de helados (chocolate o vainilla) usando el patrón Factory Method. El cliente no necesita saber cómo se crean los helados, solo los consume.

## ¿Cómo ejecutarlo?
1. Tener Python instalado.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar:

```bash
python factory_helados.py
  

#explicacion 
Hay un producto general llamado Helado.

Cada fábrica (FabricaChocolate y FabricaVainilla) sabe cómo crear su propio tipo de helado.

El cliente no sabe qué helado está recibiendo, solo pide uno y lo come.

Si mañana queremos agregar HeladoFrutilla, solo hacemos una nueva fábrica, sin tocar el resto del código.

#   T p 7 - F a c t o r y - m e t h o d  
 