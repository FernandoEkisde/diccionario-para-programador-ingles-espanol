# TODO: Convertir Tkinter a Flask

## Información Recopilada

- Aplicación actual: Diccionario de programación con Tkinter GUI, voz, datos en JSON
- Funciones: Ver lista, cambiar idioma, agregar palabra, info equipo, buscar por letra, ver definición, escuchar definición
- Datos: diccionario.json, equipo.json

## Plan de Conversión

1. Instalar Flask
2. Reescribir main.py con Flask
3. Crear templates HTML para la interfaz
4. Crear archivos estáticos (JS para voz, CSS para estilos)
5. Actualizar carga y guardado de datos
6. Probar la aplicación web

## Pasos Detallados

- [x] Instalar Flask
- [x] Crear estructura de directorios (templates/, static/)
- [x] Reescribir main.py: importar Flask, crear app, rutas
- [x] Crear templates/index.html con botones y formularios
- [x] Crear templates/list.html para mostrar lista completa
- [x] Crear templates/team.html para info del equipo
- [x] Crear templates/search.html para búsqueda
- [x] Crear static/js/voice.js para reconocimiento y síntesis de voz
- [x] Crear static/css/style.css para estilos
- [x] Actualizar funciones para web (sin Tkinter)
- [x] Probar todas las rutas y funciones
- [x] Ejecutar la app con flask run

## Seguimiento

- Actualizar este archivo a medida que se completen tareas.
- Probar voz y navegación después de cambios.
