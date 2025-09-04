import speech_recognition as sr
import pyttsx3
import json
import tkinter as tk
import webbrowser

# Diccionario de términos de programación
engine = pyttsx3.init()

# Idioma actual
idioma_actual = "español"

# Cargar miembros del equipo desde el archivo JSON
with open('equipo.json', 'r', encoding='utf-8') as f:
    miembros_equipo = json.load(f)

# Cargar diccionario de programación desde el archivo JSON
with open('diccionario.json', 'r', encoding='utf-8') as f:
    diccionario_programacion = json.load(f)

# Mensajes en español
mensajes_es = {
    "bienvenida": "¡Bienvenido/a al Manual de Términos de Programación Nuestro programa te ofrece las siguientes funciones: Explorar el catálogo de palabras, opciones multilingües, búsqueda avanzada, contribuir con nuevos términos y conocer a nuestro equipo. ¿Qué te gustaría explorar primero?",
    "opciones": [
        "1. Ver la Lista Completa de Palabras ",
        "2. Cambiar Idioma ",
        "3. Agregar Palabra Nueva ",
        "4. Información de los integrantes",
        "5. Buscar por letra ",
        "6. Ver definición de un término específico",
        "7. Escuchar definición de un término específico"
    ],
    "salir": "¡Hasta Luego!",
    "no_entendido": "No he entendido, por favor repite",
    "palabra_no_encontrada": "Palabra no encontrada.",
    "opcion_no_reconocida": "Opción no reconocida, intenta nuevamente.",
}

# Mensajes en inglés
mensajes_en = {
    "bienvenida": "Welcome to the Viking Code Dictionary! Our program offers you the following features: Explore the word catalog, multilingual options, advanced search, contribute new terms, and learn about our team. What would you like to explore first?",
    "opciones": [
        "1. View the Complete List of Words ",
        "2. Change Language ",
        "3. Add New Word ",
        "4. Team Member Information",
        "5. Search by Letter ",
        "6. View Definition of a Specific Term",
        "7. Listen to the Definition of a Specific Term"
    ],
    "salir": "See you later!",
    "no_entendido": "I didn't understand, please repeat.",
    "palabra_no_encontrada": "Word not found.",
    "opcion_no_reconocida": "Unrecognized option, please try again.",
}

def hablar(texto):
    """Convierte texto a voz."""
    engine.say(texto)
    engine.runAndWait()

def reconocer_voz():
    """Reconoce comandos de voz."""
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            hablar("Te escucho" if idioma_actual == "español" else "I'm listening")
            audio = r.listen(source)
            texto = r.recognize_google(audio, language='es-ES' if idioma_actual == "español" else 'en-US')
            print(f"Has dicho: {texto}")
            return texto.lower()
    except sr.UnknownValueError:
        print(mensajes_es["no_entendido"] if idioma_actual == "español" else mensajes_en["no_entendido"])
        hablar(mensajes_es["no_entendido"] if idioma_actual == "español" else mensajes_en["no_entendido"])
        return None
    except sr.RequestError as e:
        print(f"No se pudo obtener resultados de Google Speech Recognition; {e}")
        hablar("Ha ocurrido un error en el reconocimiento de voz" if idioma_actual == "español" else "An error occurred in voice recognition")
        return None

def ver_lista_completa():
    """Muestra la lista completa de palabras y sus definiciones."""
    print("\n--- Lista Completa de Palabras ---" if idioma_actual == "español" else "\n--- Complete List of Words ---")
    for palabra, contenido in diccionario_programacion.items():
        definicion = contenido["definicion"]
        traduccion = contenido["ejemplo"]
        print(f"{palabra}: {definicion[0]} ({traduccion[0]})")
        hablar(f"{palabra}: {definicion[0]}")

def cambiar_idioma():
    """Cambia el idioma del programa."""
    global idioma_actual
    if idioma_actual == "español":
        idioma_actual = "inglés"
        print("Idioma cambiado a inglés.")
        hablar("Language changed to English.")
    else:
        idioma_actual = "español"
        print("Idioma cambiado a español.")
        hablar("Idioma cambiado a español.")

def agregar_palabra():
    """Agrega una nueva palabra al diccionario."""
    palabra = input("Introduce la nueva palabra: " if idioma_actual == "español" else "Enter the new word: ")
    definicion = input("Introduce la definición: " if idioma_actual == "español" else "Enter the definition: ")
    traduccion = input("Introduce la traducción: " if idioma_actual == "español" else "Enter the translation: ")
    
    diccionario_programacion[palabra] = {
        "definicion": [definicion, traduccion],
        "ejemplo": [traduccion, definicion]  # Invertir para mantener la estructura
    }
    mensaje_exito = f"Palabra '{palabra}' añadida exitosamente." if idioma_actual == "español" else f"Word '{palabra}' added successfully."
    print(mensaje_exito)
    hablar(mensaje_exito)

def mostrar_informacion_integrantes():
    """Muestra la información de los integrantes del equipo."""
    encabezado = "\n--- Información de los Integrantes ---" if idioma_actual == "español" else "\n--- Team Member Information ---"
    print(encabezado)
    
    for miembro in miembros_equipo:
        info = f"Nombre: {miembro['Nombre']}, Edad: {miembro['Edad']}, Rol: {miembro['Rol']}, Alias: {', '.join(miembro['Alias'])}"
        print(info)
        hablar(info)

def buscar_palabra(diccionario, letra):
    """Busca palabras que comienzan con una letra específica."""
    encabezado = f"\n--- Palabras que comienzan con '{letra}' ---" if idioma_actual == "español" else f"\n--- Words that start with '{letra}' ---"
    print(encabezado)
    
    palabras_encontradas = [palabra for palabra in diccionario.keys() if palabra.startswith(letra)]
    
    if palabras_encontradas:
        for palabra in palabras_encontradas:
            print(palabra)
            hablar(palabra)
    else:
        mensaje_no_encontrado = "No se encontraron palabras." if idioma_actual == "español" else "No words found."
        print(mensaje_no_encontrado)
        hablar(mensaje_no_encontrado)

def ver_definicion():
    """Muestra la definición de un término específico."""
    palabra = input("Introduce la palabra de la que deseas ver la definición: " if idioma_actual == "español" else "Enter the word you want to see the definition of: ")
    
    if palabra in diccionario_programacion:
        definicion = diccionario_programacion[palabra]["definicion"]
        traduccion = diccionario_programacion[palabra]["ejemplo"]
        mensaje_definicion = f"{palabra}: {definicion[0]} ({traduccion[0]})"
        print(mensaje_definicion)
        hablar(mensaje_definicion)
    else:
        mensaje_no_encontrada = mensajes_es["palabra_no_encontrada"] if idioma_actual == "español" else mensajes_en["palabra_no_encontrada"]
        print(mensaje_no_encontrada)
        hablar(mensaje_no_encontrada)

def escuchar_definicion():
    """Escucha la definición de un término específico."""
    palabra = input("Introduce la palabra de la que deseas escuchar la definición: " if idioma_actual == "español" else "Enter the word you want to listen to the definition of: ")
    
    if palabra in diccionario_programacion:
        definicion = diccionario_programacion[palabra]["definicion"]
        hablar(definicion[0])
    else:
        mensaje_no_encontrada = mensajes_es["palabra_no_encontrada"] if idioma_actual == "español" else mensajes_en["palabra_no_encontrada"]
        print(mensaje_no_encontrada)
        hablar(mensaje_no_encontrada)

# GUI Functions
def ver_lista_completa_gui():
    output_text.delete(1.0, tk.END)
    header = "\n--- Lista Completa de Palabras ---" if idioma_actual == "español" else "\n--- Complete List of Words ---"
    output_text.insert(tk.END, header + '\n')
    for palabra, contenido in diccionario_programacion.items():
        definicion = contenido["definicion"]
        traduccion = contenido["ejemplo"]
        line = f"{palabra}: {definicion[0]} ({traduccion[0]})"
        output_text.insert(tk.END, line + '\n')
        hablar(f"{palabra}: {definicion[0]}")

def cambiar_idioma_gui():
    global idioma_actual
    if idioma_actual == "español":
        idioma_actual = "inglés"
        msg = "Idioma cambiado a inglés."
        speak = "Language changed to English."
    else:
        idioma_actual = "español"
        msg = "Idioma cambiado a español."
        speak = "Idioma cambiado a español."
    output_text.insert(tk.END, msg + '\n')
    hablar(speak)

def mostrar_informacion_integrantes_gui():
    header = "\n--- Información de los Integrantes ---" if idioma_actual == "español" else "\n--- Team Member Information ---"
    output_text.insert(tk.END, header + '\n')
    for miembro in miembros_equipo:
        info = f"Nombre: {miembro['Nombre']}, Edad: {miembro['Edad']}, Rol: {miembro['Rol']}, Alias: {', '.join(miembro['Alias'])}"
        output_text.insert(tk.END, info + '\n')
        hablar(info)

def buscar_palabra_gui(diccionario, letra):
    header = f"\n--- Palabras que comienzan con '{letra}' ---" if idioma_actual == "español" else f"\n--- Words that start with '{letra}' ---"
    output_text.insert(tk.END, header + '\n')
    palabras_encontradas = [palabra for palabra in diccionario.keys() if palabra.startswith(letra)]
    if palabras_encontradas:
        for palabra in palabras_encontradas:
            output_text.insert(tk.END, palabra + '\n')
            hablar(palabra)
    else:
        msg = "No se encontraron palabras." if idioma_actual == "español" else "No words found."
        output_text.insert(tk.END, msg + '\n')
        hablar(msg)

def ver_definicion_gui(palabra):
    if palabra in diccionario_programacion:
        definicion = diccionario_programacion[palabra]["definicion"]
        traduccion = diccionario_programacion[palabra]["ejemplo"]
        mensaje_definicion = f"{palabra}: {definicion[0]} ({traduccion[0]})"
        output_text.insert(tk.END, mensaje_definicion + '\n')
        hablar(mensaje_definicion)
    else:
        mensaje_no_encontrada = mensajes_es["palabra_no_encontrada"] if idioma_actual == "español" else mensajes_en["palabra_no_encontrada"]
        output_text.insert(tk.END, mensaje_no_encontrada + '\n')
        hablar(mensaje_no_encontrada)

def escuchar_definicion_gui(palabra):
    if palabra in diccionario_programacion:
        definicion = diccionario_programacion[palabra]["definicion"]
        hablar(definicion[0])
    else:
        mensaje_no_encontrada = mensajes_es["palabra_no_encontrada"] if idioma_actual == "español" else mensajes_en["palabra_no_encontrada"]
        output_text.insert(tk.END, mensaje_no_encontrada + '\n')
        hablar(mensaje_no_encontrada)

def agregar_palabra_gui(palabra, definicion, traduccion):
    diccionario_programacion[palabra] = {
        "definicion": [definicion, traduccion],
        "ejemplo": [traduccion, definicion]
    }
    mensaje_exito = f"Palabra '{palabra}' añadida exitosamente." if idioma_actual == "español" else f"Word '{palabra}' added successfully."
    output_text.insert(tk.END, mensaje_exito + '\n')
    hablar(mensaje_exito)

def menu():
    """ Muestra el menú principal y gestiona las opciones del usuario."""
    mensaje_bienvenida = mensajes_es["bienvenida"] if idioma_actual == "español" else mensajes_en["bienvenida"]
    print(mensaje_bienvenida)
    hablar(mensaje_bienvenida)

    while True:
        print("\n--- Menú ---" if idioma_actual == "español" else "\n--- Menu ---")
        opciones = mensajes_es["opciones"] if idioma_actual == "español" else mensajes_en["opciones"]

        for opcion in opciones:
            print(opcion)

        usar_voz = input("¿Quieres usar voz para seleccionar una opción? (s/n): " if idioma_actual == "español" else "Do you want to use voice to select an option? (y/n): ")

        if usar_voz.lower() in ['s', 'y']:
            opcion = reconocer_voz()
            if opcion is None:
                continue  # Si no se entendió, vuelve a preguntar
            if "ver la lista" in opcion or "view the complete list" in opcion:
                ver_lista_completa()
            elif "cambiar idioma" in opcion or "change language" in opcion:
                cambiar_idioma()
            elif "agregar" in opcion or "add" in opcion:
                agregar_palabra()
            elif "información" in opcion or "information" in opcion:
                mostrar_informacion_integrantes()
            elif "buscar" in opcion or "search" in opcion:
                letra = input("Ingrese la letra a buscar: " if idioma_actual == "español" else "Enter the letter to search: ")
                buscar_palabra(diccionario_programacion, letra)
            elif "definición" in opcion or "definition" in opcion:
                ver_definicion()
            elif "escuchar definición" in opcion or "listen to definition" in opcion:
                escuchar_definicion()
            elif "salir" in opcion or "exit" in opcion:
                print(mensajes_es["salir"] if idioma_actual == "español" else mensajes_en["salir"])
                hablar(mensajes_es["salir"] if idioma_actual == "español" else mensajes_en["salir"])
                break
            else:
                print(mensajes_es["opcion_no_reconocida"] if idioma_actual == "español" else mensajes_en["opcion_no_reconocida"])
                hablar(mensajes_es["opcion_no_reconocida"] if idioma_actual == "español" else mensajes_en["opcion_no_reconocida"])
        else:
            opcion = input("Seleccione una opción: " if idioma_actual == "español" else "Select an option: ")
            if opcion == "1":
                ver_lista_completa()
            elif opcion == "2":
                cambiar_idioma()
            elif opcion == "3":
                agregar_palabra()
            elif opcion == "4":
                mostrar_informacion_integrantes()
            elif opcion == "5":
                letra = input("Ingrese la letra a buscar: " if idioma_actual == "español" else "Enter the letter to search: ")
                buscar_palabra(diccionario_programacion, letra)
            elif opcion == "6":
                ver_definicion()
            elif opcion == "7":
                escuchar_definicion()
            elif opcion.lower() == "salir":
                print(mensajes_es["salir"] if idioma_actual == "español" else mensajes_en["salir"])
                hablar(mensajes_es["salir"] if idioma_actual == "español" else mensajes_en["salir"])
                break
            else:
                print("Opción inválida. Intenta Nuevamente." if idioma_actual == "español" else "Invalid option. Please try again.")

if __name__ == "__main__":
    # GUI
    root = tk.Tk()
    root.title("Programming Dictionary")

    output_text = tk.Text(root, height=20, width=80)
    output_text.pack()

    # Welcome message
    output_text.insert(tk.END, mensajes_es["bienvenida"] if idioma_actual == "español" else mensajes_en["bienvenida"] + '\n')
    hablar(mensajes_es["bienvenida"] if idioma_actual == "español" else mensajes_en["bienvenida"])

    # Buttons frame
    buttons_frame = tk.Frame(root)
    buttons_frame.pack()

    btn1 = tk.Button(buttons_frame, text="Ver Lista Completa", command=ver_lista_completa_gui)
    btn1.pack(side=tk.LEFT)

    btn2 = tk.Button(buttons_frame, text="Cambiar Idioma", command=cambiar_idioma_gui)
    btn2.pack(side=tk.LEFT)

    btn4 = tk.Button(buttons_frame, text="Información Integrantes", command=mostrar_informacion_integrantes_gui)
    btn4.pack(side=tk.LEFT)

    # Input frame
    input_frame = tk.Frame(root)
    input_frame.pack()

    tk.Label(input_frame, text="Palabra:").pack(side=tk.LEFT)
    entry_palabra = tk.Entry(input_frame)
    entry_palabra.pack(side=tk.LEFT)

    btn6 = tk.Button(input_frame, text="Ver Definición", command=lambda: ver_definicion_gui(entry_palabra.get()))
    btn6.pack(side=tk.LEFT)

    btn7 = tk.Button(input_frame, text="Escuchar Definición", command=lambda: escuchar_definicion_gui(entry_palabra.get()))
    btn7.pack(side=tk.LEFT)

    # Search frame
    search_frame = tk.Frame(root)
    search_frame.pack()

    tk.Label(search_frame, text="Letra:").pack(side=tk.LEFT)
    entry_letra = tk.Entry(search_frame, width=5)
    entry_letra.pack(side=tk.LEFT)

    btn5 = tk.Button(search_frame, text="Buscar por Letra", command=lambda: buscar_palabra_gui(diccionario_programacion, entry_letra.get()))
    btn5.pack(side=tk.LEFT)

    # Add frame
    add_frame = tk.Frame(root)
    add_frame.pack()

    tk.Label(add_frame, text="Nueva Palabra:").pack(side=tk.LEFT)
    entry_palabra_add = tk.Entry(add_frame)
    entry_palabra_add.pack(side=tk.LEFT)

    tk.Label(add_frame, text="Definición:").pack(side=tk.LEFT)
    entry_def_add = tk.Entry(add_frame)
    entry_def_add.pack(side=tk.LEFT)

    tk.Label(add_frame, text="Traducción:").pack(side=tk.LEFT)
    entry_trad_add = tk.Entry(add_frame)
    entry_trad_add.pack(side=tk.LEFT)

    btn3 = tk.Button(add_frame, text="Agregar", command=lambda: agregar_palabra_gui(entry_palabra_add.get(), entry_def_add.get(), entry_trad_add.get()))
    btn3.pack(side=tk.LEFT)

    # Habbo frame
    habbo_frame = tk.Frame(root)
    habbo_frame.pack()

    tk.Label(habbo_frame, text="Habbo Retro Client URL:").pack(side=tk.LEFT)
    entry_habbo_url = tk.Entry(habbo_frame, width=50)
    entry_habbo_url.pack(side=tk.LEFT)
    entry_habbo_url.insert(0, "https://www.habbo.com")

    btn_habbo = tk.Button(habbo_frame, text="Connect to Habbo", command=lambda: webbrowser.open(entry_habbo_url.get()))
    btn_habbo.pack(side=tk.LEFT)

    root.mainloop()
