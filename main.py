from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import pyttsx3
import speech_recognition as sr
import webbrowser
import os

app = Flask(__name__)

# Load data from JSON files
def load_data():
    with open('diccionario.json', 'r', encoding='utf-8') as f:
        diccionario_programacion = json.load(f)
    with open('equipo.json', 'r', encoding='utf-8') as f:
        miembros_equipo = json.load(f)
    return diccionario_programacion, miembros_equipo

diccionario_programacion, miembros_equipo = load_data()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Current language
idioma_actual = "español"

# Messages
mensajes = {
    "español": {
        "bienvenida": "¡Bienvenido/a al Manual de Términos de Programación! Nuestro programa te ofrece las siguientes funciones: Explorar el catálogo de palabras, opciones multilingües, búsqueda avanzada, contribuir con nuevos términos y conocer a nuestro equipo. ¿Qué te gustaría explorar primero?",
        "salir": "¡Hasta Luego!",
        "no_entendido": "No he entendido, por favor repite",
        "palabra_no_encontrada": "Palabra no encontrada.",
        "opcion_no_reconocida": "Opción no reconocida, intenta nuevamente.",
    },
    "inglés": {
        "bienvenida": "Welcome to the Viking Code Dictionary! Our program offers you the following features: Explore the word catalog, multilingual options, advanced search, contribute new terms, and learn about our team. What would you like to explore first?",
        "salir": "See you later!",
        "no_entendido": "I didn't understand, please repeat.",
        "palabra_no_encontrada": "Word not found.",
        "opcion_no_reconocida": "Unrecognized option, please try again.",
    }
}

def hablar(texto):
    """Convert text to speech."""
    try:
        engine.say(texto)
        engine.runAndWait()
    except RuntimeError:
        # Handle the error when run loop is already started
        pass

@app.route('/')
def index():
    bienvenida = mensajes[idioma_actual]["bienvenida"]
    return render_template('index.html', bienvenida=bienvenida, idioma=idioma_actual)

@app.route('/lista')
def lista():
    return render_template('list.html', diccionario=diccionario_programacion, idioma=idioma_actual)

@app.route('/equipo')
def equipo():
    return render_template('team.html', miembros=miembros_equipo, idioma=idioma_actual)

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    resultado = None
    letra = ''
    if request.method == 'POST':
        letra = request.form.get('letra', '').lower()
    elif request.method == 'GET':
        letra = request.args.get('letra', '').lower()
    if letra:
        resultado = {k: v for k, v in diccionario_programacion.items() if k.lower().startswith(letra)}
    return render_template('search.html', resultado=resultado, letra=letra, idioma=idioma_actual)

@app.route('/definicion/<palabra>')
def definicion(palabra):
    palabra_lower = palabra.lower()
    if palabra_lower in diccionario_programacion:
        definicion = diccionario_programacion[palabra_lower]["definicion"][0]
        traduccion = diccionario_programacion[palabra_lower]["ejemplo"][0]
        return render_template('definition.html', palabra=palabra, definicion=definicion, traduccion=traduccion, idioma=idioma_actual)
    else:
        mensaje = mensajes[idioma_actual]["palabra_no_encontrada"]
        return render_template('definition.html', palabra=palabra, mensaje=mensaje, idioma=idioma_actual)

@app.route('/escuchar/<palabra>')
def escuchar(palabra):
    palabra_lower = palabra.lower()
    if palabra_lower in diccionario_programacion:
        definicion = diccionario_programacion[palabra_lower]["definicion"][0]
        hablar(definicion)
        return jsonify({"status": "success", "message": f"Escuchando definición de {palabra}"})
    else:
        mensaje = mensajes[idioma_actual]["palabra_no_encontrada"]
        hablar(mensaje)
        return jsonify({"status": "error", "message": mensaje})

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        palabra = request.form.get('palabra', '').strip()
        definicion = request.form.get('definicion', '').strip()
        traduccion = request.form.get('traduccion', '').strip()
        if palabra and definicion and traduccion:
            diccionario_programacion[palabra] = {
                "definicion": [definicion, traduccion],
                "ejemplo": [traduccion, definicion]
            }
            # Save to JSON file
            with open('diccionario.json', 'w', encoding='utf-8') as f:
                json.dump(diccionario_programacion, f, ensure_ascii=False, indent=2)
            mensaje_exito = f"Palabra '{palabra}' añadida exitosamente." if idioma_actual == "español" else f"Word '{palabra}' added successfully."
            return render_template('add.html', mensaje=mensaje_exito, idioma=idioma_actual)
        else:
            mensaje_error = "Por favor complete todos los campos." if idioma_actual == "español" else "Please fill all fields."
            return render_template('add.html', mensaje=mensaje_error, idioma=idioma_actual)
    return render_template('add.html', idioma=idioma_actual)

@app.route('/cambiar_idioma')
def cambiar_idioma():
    global idioma_actual
    if idioma_actual == "español":
        idioma_actual = "inglés"
    else:
        idioma_actual = "español"
    return redirect(url_for('index'))

@app.route('/habbo')
def habbo():
    url = request.args.get('url', 'https://www.habbo.com')
    return redirect(url)

@app.route('/api/definicion/<palabra>')
def api_definicion(palabra):
    palabra_lower = palabra.lower()
    if palabra_lower in diccionario_programacion:
        definicion = diccionario_programacion[palabra_lower]["definicion"][0]
        traduccion = diccionario_programacion[palabra_lower]["ejemplo"][0]
        return jsonify({
            "palabra": palabra,
            "definicion": definicion,
            "traduccion": traduccion,
            "encontrada": True
        })
    else:
        return jsonify({
            "palabra": palabra,
            "mensaje": mensajes[idioma_actual]["palabra_no_encontrada"],
            "encontrada": False
        })

if __name__ == '__main__':
    app.run(debug=True)
