import speech_recognition as sr
import pyttsx3

# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()

# Función para hablar un texto
def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

# Función para reconocer voz
def reconocer_voz():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        hablar("Te escucho")
        audio = r.listen(source)
    try:
        texto = r.recognize_google(audio, language='es-ES')
        print(f"Has dicho: {texto}")
        return texto.lower()
    except sr.UnknownValueError:
        print("No he entendido lo que dijiste.")
        hablar("No he entendido, por favor repite")
        return None
    except sr.RequestError as e:
        print(f"No se pudo obtener resultados de Google Speech Recognition; {e}")
        hablar("Ha ocurrido un error en el reconocimiento de voz")
        return None

diccionario = {
    "array": ("Estructura de datos que almacena múltiples valores.", "Array"),
    "asignar": ("Establecer un valor a una variable.", "To assign"),
    "algoritmo": ("Conjunto de instrucciones para resolver un problema.", "Algorithm"),
    "API": ("Interfaz de programación de aplicaciones que permite la interacción entre software.", "API"),
    "asíncrono": ("Ejecutar procesos de manera no secuencial.", "Asynchronous"),
    "atributo": ("Propiedad o característica de un objeto.", "Attribute"),
    "autenticación": ("Proceso de verificar la identidad de un usuario.", "Authentication"),
    "automatización": ("Uso de tecnología para realizar tareas sin intervención humana.", "Automation"),
    "agente": ("Programa que actúa en nombre de un usuario o sistema.", "Agent"),
    "análisis": ("Examen detallado de un sistema o programa.", "Analysis"),
    "aplicación": ("Software diseñado para realizar una función específica.", "Application"),
    "asistente": ("Software que ayuda al usuario en tareas específicas.", "Assistant"),
    "acceso": ("Posibilidad de utilizar recursos o datos.", "Access"),
    "anidación": ("Uso de estructuras dentro de otras, como bucles o condicionales.", "Nesting"),
    "archivo": ("Conjunto de datos almacenados en un dispositivo.", "File"),
    "adaptador": ("Componente que permite la compatibilidad entre diferentes sistemas.", "Adapter"),
    "algoritmo genético": ("Método de optimización inspirado en la evolución natural.", "Genetic algorithm"),
    "análisis de datos": ("Proceso de inspeccionar y modelar datos para extraer información útil.", "Data analysis"),
    "agregación": ("Combinación de múltiples elementos en uno solo.", "Aggregation"),
    "aplicación web": ("Software accesible a través de un navegador web.", "Web application"),
    "asociación": ("Relación entre diferentes elementos o entidades.", "Association"),
    "acuerdo de nivel de servicio": ("Contrato que define el nivel esperado de servicio.", "Service level agreement"),
    "algoritmo de búsqueda": ("Método para encontrar un elemento en una estructura de datos.", "Search algorithm"),
    "análisis estático": ("Evaluación de código sin ejecutarlo para identificar errores.", "Static analysis"),
    "análisis dinámico": ("Evaluación de código durante su ejecución para identificar errores.", "Dynamic analysis"),
    "agile": ("Metodología de desarrollo de software que promueve la flexibilidad y la colaboración.", "Agile"),
    "agregador": ("Aplicación que recopila información de diversas fuentes.", "Aggregator"),
    "asignación dinámica": ("Asignación de memoria durante la ejecución del programa.", "Dynamic allocation"),
    "análisis de requisitos": ("Proceso de determinar las necesidades del usuario para un sistema.", "Requirements analysis"),
    "adaptabilidad": ("Capacidad de un sistema para ajustarse a cambios.", "Adaptability"),
    "algoritmo de ordenamiento": ("Método para organizar elementos en un orden específico.", "Sorting algorithm"),
    "asignación estática": ("Asignación de memoria en tiempo de compilación.", "Static allocation"),
    "asociación de clases": ("Relación entre dos o más clases en programación orientada a objetos.", "Class association"),
    "aplicación móvil": ("Software diseñado para ser utilizado en dispositivos móviles.", "Mobile application"),
    "análisis de impacto": ("Evaluación de las consecuencias de un cambio en un sistema.", "Impact analysis"),
    
    # B
    "bucles": ("Estructura que permite repetir un bloque de código.", "Loops"),
    "bucles anidados": ("Bucle dentro de otro bucle.", "Nested loops"),
    "booleano": ("Tipo de dato que puede ser verdadero o falso.", "Boolean"),
    "backend": ("Parte de una aplicación que maneja la lógica del servidor y la base de datos.", "Backend"),
    "base de datos": ("Conjunto organizado de datos almacenados y accesibles.", "Database"),
    "bifurcación": ("División de un proceso en dos o más caminos.", "Branching"),
    "buffer": ("Área de memoria temporal utilizada para almacenar datos.", "Buffer"),
    "bug": ("Error o fallo en un programa.", "Bug"),
    "búsqueda binaria": ("Método eficiente para encontrar un elemento en una lista ordenada.", "Binary search"),
    "bucle for": ("Estructura de control que repite un bloque de código un número específico de veces.", "For loop"),
    "bucle while": ("Estructura de control que repite un bloque de código mientras una condición sea verdadera.", "While loop"),
    "break": ("Instrucción que termina un bucle antes de que se complete su ejecución.", "Break"),
    "branch": ("Una versión de un proyecto en un sistema de control de versiones.", "Branch"),
    "build": ("Proceso de compilar y enlazar el código fuente para crear un programa ejecutable.", "Build"),
    "byte": ("Unidad básica de almacenamiento de datos, generalmente compuesta por 8 bits.", "Byte"),
    
    # C
    "clase": ("Plantilla para crear objetos en programación orientada a objetos.", "Class"),
    "callback": ("Función que se pasa como argumento a otra función.", "Callback"),
    "código": ("Conjunto de instrucciones escritas en un lenguaje de programación.", "Code"),
    "código abierto": ("Software cuyo código fuente es accesible y puede ser modificado.", "Open source"),
    "condicional": ("Estructura que permite tomar decisiones en el flujo del programa.", "Conditional"),
    "concurrencia": ("Capacidad de ejecutar múltiples procesos al mismo tiempo.", "Concurrency"),
    "contenedor": ("Unidad estándar de software que empaqueta el código y todas sus dependencias.", "Container"),
    "cliente": ("Computadora que solicita servicios de un servidor.", "Client"),
    "ciberseguridad": ("Prácticas y tecnologías para proteger sistemas y datos de ataques maliciosos.", "Cybersecurity"),
    "caché": ("Almacenamiento temporal de datos para acelerar el acceso a ellos.", "Cache"),
    "compilador": ("Programa que traduce código fuente a código máquina.", "Compiler"),
    "complejidad algorítmica": ("Medida de la eficiencia de un algoritmo en función de su tiempo y espacio de ejecución.", "Algorithmic complexity"),
    "conexión": ("Establecimiento de un enlace entre dos sistemas o dispositivos.", "Connection"),
    "constructor": ("Método especial en una clase que se utiliza para crear objetos.", "Constructor"),
    "código fuente": ("Texto escrito en un lenguaje de programación que define un programa.", "Source code"),
    "ciclo de vida del software": ("Fases que atraviesa un software desde su concepción hasta su retiro.", "Software development lifecycle"),
    "copia de seguridad": ("Duplicado de datos para protegerlos contra pérdida o daño.", "Backup"),
    "código de estado": ("Número que indica el resultado de una solicitud HTTP.", "Status code"),
    "circuito": ("Conjunto de componentes electrónicos interconectados.", "Circuit"),
    "código limpio": ("Código que es fácil de leer y mantener.", "Clean code"),
    "ciclo de desarrollo": ("Fases repetitivas en el desarrollo de software, como planificación, diseño, implementación y pruebas.", "Development cycle"),
    
    # D
    "depurar": ("Eliminar errores en el código.", "To debug"),
    "depuración": ("Proceso de identificar y corregir errores en un programa.", "Debugging"),
    "docker": ("Plataforma para crear, desplegar y ejecutar aplicaciones en contenedores.", "Docker"),
    "data lake": ("Almacenamiento centralizado de datos en su formato original.", "Data lake"),
    "data warehouse": ("Sistema utilizado para el análisis y reporte de datos.", "Data warehouse"),
    "deserialización": ("Proceso de convertir un formato almacenado o transmitido de vuelta a un objeto.", "Deserialization"),
    "documentación": ("Descripción detallada de cómo utilizar un software.", "Documentation"),
    "debugger": ("Herramienta que permite depurar programas.", "Debugger"),
    "diseño de software": ("Proceso de definir la arquitectura y componentes de un sistema.", "Software design"),
    "distrib uido": ("Sistema que opera en múltiples computadoras que se comunican entre sí.", "Distributed"),
    "dominio": ("Área de conocimiento o aplicación específica en un sistema.", "Domain"),
    "despliegue": ("Proceso de poner un software en producción.", "Deployment"),
    "dependencia": ("Relación entre dos o más módulos, donde uno depende del otro.", "Dependency"),
    "directorio": ("Estructura que organiza archivos en un sistema de archivos.", "Directory"),
    "diseño orientado a objetos": ("Enfoque de diseño que utiliza objetos y clases para modelar sistemas.", "Object-oriented design"),
    "diferencial": ("Proceso de comparar dos versiones de un archivo para identificar cambios.", "Diff"),
    
    # E
    "encapsulamiento": ("Técnica que restringe el acceso a ciertos componentes de un objeto.", "Encapsulation"),
    "entidad": ("Elemento que tiene una existencia independiente en un sistema.", "Entity"),
    "estructura de datos": ("Método para organizar y almacenar datos de manera eficiente.", "Data structure"),
    "excepción": ("Evento que altera el flujo normal de un programa.", "Exception"),
    "ejecución": ("Proceso de llevar a cabo las instrucciones de un programa.", "Execution"),
    "entorno de desarrollo": ("Conjunto de herramientas y configuraciones para desarrollar software.", "Development environment"),
    
    # F
    "función": ("Bloque de código que realiza una tarea específica y puede ser reutilizado.", "Function"),
    "framework": ("Conjunto de herramientas y bibliotecas que facilitan el desarrollo de software.", "Framework"),
    "flujo de control": ("Orden en el que se ejecutan las instrucciones de un programa.", "Control flow"),
    "formato": ("Estructura o disposición de datos.", "Format"),
    "front-end": ("Parte de una aplicación que interactúa directamente con el usuario.", "Front-end"),
    
    # G
    "git": ("Sistema de control de versiones distribuido.", "Git"),
    "grupo de trabajo": ("Conjunto de personas que colaboran en un proyecto.", "Working group"),
    "gestión de proyectos": ("Proceso de planificar, ejecutar y supervisar proyectos.", "Project management"),
    "gráfico": ("Representación visual de datos.", "Graph"),
    
    # H
    "hash": ("Función que convierte datos de entrada en un valor de longitud fija.", "Hash"),
    "herencia": ("Mecanismo en programación orientada a objetos que permite a una clase adquirir propiedades de otra.", "Inheritance"),
    "hardware": ("Componentes físicos de una computadora.", "Hardware"),
    
    # I
    "interfaz": ("Punto de interacción entre diferentes sistemas o componentes.", "Interface"),
    "instancia": ("Objeto creado a partir de una clase.", "Instance"),
    "implementación": ("Proceso de llevar a cabo un diseño o plan.", "Implementation"),
    
    # J
    "JSON": ("Formato de intercambio de datos ligero y fácil de leer.", "JSON"),
    "Java": ("Lenguaje de programación orientado a objetos ampliamente utilizado.", "Java"),
    
    # K
    "Kubernetes": ("Sistema de orquestación para automatizar la implementación, escalado y gestión de aplicaciones en contenedores.", "Kubernetes"),
    
    # L
    "lenguaje de programación": ("Conjunto de reglas y sintaxis para escribir programas.", "Programming language"),
    "librería": ("Colección de funciones y procedimientos que pueden ser utilizados en un programa.", "Library"),
    
    # M
    "módulo": ("Unidad de código que encapsula funcionalidad específica.", "Module"),
    "metodología": ("Conjunto de métodos y prácticas para llevar a cabo un proyecto.", "Methodology"),
    
    # N
    "nube": ("Modelo de computación que permite el acceso a recursos y servicios a través de Internet.", "Cloud"),
    "navegador": ("Aplicación que permite acceder a información en la web.", "Browser"),
    
    # O
    "objeto": ("Instancia de una clase que contiene datos y métodos.", "Object"),
    "operador": ("Símbolo que representa una operación en programación.", "Operator"),
    
    # P
    "paradigma": ("Enfoque o estilo de programación.", "Paradigm"),
    "prototipo": ("Modelo inicial de un producto o sistema.", "Prototype"),
    
    # Q
    "query": ("Consulta a una base de datos para obtener información.", "Query"),
    
    # R
    "repositorio": ("Lugar donde se almacena y gestiona el código fuente.", "Repository"),
    "refactorización": ("Proceso de mejorar el código sin cambiar su funcionalidad.", "Refactoring"),
    
    # S
    "sistema operativo": ("Software que gestiona el hardware y software de una computadora.", "Operating system"),
    "seguridad informática": ("Prácticas para proteger sistemas y datos de accesos no autorizados.", "Information security"),
    
    # T
    "tipo de dato": ("Clasificación de datos que determina qué operaciones se pueden realizar sobre ellos.", "Data type"),
    "test": ("Prueba para verificar que un programa funciona como se espera.", "Test"),
    
    # U
    "usuario": ("Persona que utiliza un sistema o aplicación.", "User "),
    "unidad de prueba": ("Conjunto de pruebas que se realizan sobre una unidad de código.", "Test case"),
    
    # V
    "variable": ("Espacio de almacenamiento que tiene un nombre y puede contener un valor.", "Variable"),
    "versionado": ("Proceso de gestionar y controlar las diferentes versiones de un software.", "Versioning"),
    
    # W
    "web": ("Conjunto de páginas y recursos accesibles a través de Internet.", "Web"),
    "widget": ("Componente de interfaz gráfica que permite la interacción del usuario.", "Widget"),
    
    # X
    "XML": ("Lenguaje de marcado que define un conjunto de reglas para codificar documentos en un formato legible por humanos y máquinas.", "XML"),
    
    # Y
    "YAML": ("Formato de serialización de datos legible por humanos, utilizado comúnmente para archivos de configuración.", "YAML"),
    
    # Z
    "zócalo": ("Punto de conexión en un sistema que permite la comunicación entre diferentes componentes.", "Socket"),
}

integrantes = [
    {
        "Nombre": "Gabriel Pedreros",
        "Edad": 17,
        "Rol": "Desarrollador En Jefe",
        "Email": "Gabriel.pedreros.becerra@alumnos.cmch.maristas.cl",
        "Alias": "El Manco para el Futbol, Cantante estrella, milhouse, king of fights"
    },
    {
        "Nombre": "Maximiliano Veliz",
        "Edad": 17,
        "Rol": "Desarrollador",
        "Email": "maximiliano.veliz.aguilar@alumnos.cmch.maristas.cl",
        "Alias": "El cafe, esclavo, color humilde, carton mojado, carbon de parrilla, milhouse quemado, sin cuerpo, humor negro."
    },
    {
        "Nombre": "Jesus Vidal",
        "Edad": 16,
        "Rol": "Desarrollador",
        "Email": "jesus.vidal.carrasco@alumnos.cmch.maristas.cl",
        "Alias": "El mesias, el mascapito, el traga pitos 3000, la mano de dios (para agarrar el pico)"
    },
    {
        "Nombre": "Angel Zuñiga",
        "Edad": 17,
        "Rol": "Diseñador En Jefe",
        "Email": "angel.zuniga.villalobos@alumnos.cmch.maristas.cl",
        "Alias": "El mensajero del diablo, el compañero de el diablo, cerbero (por perro), Stephen Hawking,Professor X/Charles Xavier, rayo mqueen, el cojo, el manco, el sin espalda"
    },
    {
        "Nombre": "Valentina San Martin",
        "Edad": 16,
        "Rol": "Diseñadora",
        "Email": "valentina.sanmartin.roman@alumnos.cmch.maristas.cl",
        "Alias": "la otaku, la lesbiana,el gusto de la concha, enferma, rarita"
    },
    {
        "Nombre": "Matias Lara",
        "Edad": 17,
        "Rol": "Diseñador",
        "Email": "matias.lara.valenzuela@alumnos.cmch.maristas.cl",
        "Alias": "Transformer, hombre con vagina, el ciego, el sordo, el sueño imposible (poner el pico)"
    },
    {
        "Nombre": "Fernando Ibañez",
        "Edad": 16,
        "Rol": "Líder de este trabajo",
        "Email": "fernando.ibañez.moreno@alumnos.cmch.maristas.cl",
        "Alias": ("El cabeza de bello pubico, el pinguino de linux, don pinpon, barnie, bob patiño, "
                  "necesitado (de pico), autista conchetumare, poo de kung fu panda, los tres chanchitos en uno, "
                  "la vaca lola, winnie pooh, el hombre topo grande, pie grande, el mano de pajero, "
                  "el mas cayos que manos, el compra terreno, "
                  "el loco de los gatos, don barriga, ñoño, troncha toro, rasputia, el que dejo manco a su madre, devuelvame el dinero que lloro")
    }
]

idioma_actual = "español"
diccionario_por_letras = {}

def actualizar_diccionario_por_letras():
    global diccionario_por_letras
    diccionario_por_letras = {}
    for palabra in diccionario.keys():
        letra_inicial = palabra[0].lower()
        if letra_inicial not in diccionario_por_letras:
            diccionario_por_letras[letra_inicial] = []
        diccionario_por_letras[letra_inicial].append(palabra)

actualizar_diccionario_por_letras()

def mostrar_la_informacion_de_los_integrantes():
    if not integrantes:
        print("No hay integrantes para mostrar.")
        hablar("No hay integrantes para mostrar.")
        return
    for integrante in integrantes:
        info = f"Nombre: {integrante['Nombre']}, Edad: {integrante['Edad']}, Rol: {integrante['Rol']}, Email: {integrante['Email']}, Alias: {integrante['Alias']}"
        print(info)
        hablar(info)
        print("-" * 50)

def ver_lista_completa():
    print("\nLista de Palabras 📜:" if idioma_actual == "español" else "\nWord List 📜:")
    hablar("Mostrando lista de palabras")
    for letra, palabras in sorted(diccionario_por_letras.items()):
        print(f"\nPalabras que comienzan con '{letra.upper()}':")
        for palabra in palabras:
            definicion, traduccion = diccionario[palabra]
            info = f"{palabra}: {definicion} ({traduccion})"
            print(info)
            hablar(info)

def cambiar_idioma():
    global idioma_actual
    idioma_actual = "inglés" if idioma_actual == "español" else "español"
    mensaje = "¡Palabras de poder en inglés activadas!" if idioma_actual == "inglés" else "¡Palabras de poder en español activadas!"
    print(f"\n{mensaje}")
    hablar(mensaje)

def buscar_palabra(letra):
    if not letra:
        mensaje = "Por favor, ingrese una letra válida." if idioma_actual == "español" else "Please enter a valid letter."
        print(mensaje)
        hablar(mensaje)
        return
    letra = letra.lower()
    print(f"\nBuscando palabras que comienzan con '{letra}' 🔍:" if idioma_actual == "español" else f"\nSearching for words starting with '{letra}' 🔍:")
    hablar(f"Buscando palabras que comienzan con {letra}")
    if letra in diccionario_por_letras:
        for palabra in diccionario_por_letras[letra]:
            definicion, traduccion = diccionario[palabra]
            info = f"{palabra}: {definicion} ({traduccion})"
            print(info)
            hablar(info)
    else:
        mensaje = "No se encontraron palabras." if idioma_actual == "español" else "No words found."
        print(mensaje)
        hablar(mensaje)

def agregar_palabra():
    nueva_palabra = input("Ingrese la nueva palabra: ").strip()
    if not nueva_palabra:
        print("Por favor, ingrese una palabra válida.")
        hablar("Por favor, ingrese una palabra válida.")
        return
    if nueva_palabra in diccionario:
        print("La palabra ya existe en el diccionario.")
        hablar("La palabra ya existe en el diccionario.")
        return
    definicion = input("Ingrese la definición: ").strip()
    traduccion = input("Ingrese la traducción al inglés: ").strip()
    if not definicion or not traduccion:
        print("Por favor, ingrese una definición y traducción válidas.")
        hablar("Por favor, ingrese una definición y traducción válidas.")
        return
    diccionario[nueva_palabra] = (definicion, traduccion)
    actualizar_diccionario_por_letras()
    print("Palabra agregada exitosamente.")
    hablar("Palabra agregada exitosamente.")

def menu():
    mensaje_bienvenida = "¡Bienvenido/a al Diccionario Digital Interactivo! Nuestro programa te ofrece las siguientes funciones: Explorar el extenso catálogo de palabras, Opciones multilingües, Búsqueda avanzada por categorías y letras, Contribuir con nuevos términos, Conocer a nuestro equipo. ¿Qué te gustaría explorar primero?"

    print(mensaje_bienvenida)
    hablar(mensaje_bienvenida)
    
    while True:
        print("\n--- Menú ---" if idioma_actual == "español" else "\n--- Menu ---")
        opciones = [
            "Ver la Lista Completa de Palabras  📜",  
            "Cambiar Idioma 🌍",                       
            "Buscar por letra 🔍",                     
            "Agregar Palabra Nueva ✨",                
            "Información de los integrantes",          
            "Salir 🕯️"                               
        ]
        for i, opcion in enumerate(opciones, start=1):
            print(f"{i}. {opcion}")

        usar_voz = input("¿Quieres usar voz para seleccionar una opción? (s/n): ")
        if usar_voz.lower() == 's':
            opcion = reconocer_voz()
            if opcion is None:
                continue  # Si no se entendió, vuelve a preguntar
            if "ver la lista" in opcion:
                ver_lista_completa()
            elif "cambiar idioma" in opcion:
                cambiar_idioma()
            elif "buscar" in opcion:
                letra = input("Ingrese la letra a buscar: " if idioma_actual == "español" else "Enter the letter to search: ")
                buscar_palabra(letra)
            elif "agregar" in opcion:
                agregar_palabra()
            elif "información" in opcion:
                mostrar_la_informacion_de_los_integrantes()
            elif "salir" in opcion:
                print("¡Hasta Luego! 👋 " if idioma_actual == "español" else "Goodbye! 👋")
                hablar("¡Hasta Luego!" if idioma_actual == "español" else "Goodbye!")
                break
            else:
                print("Opción no reconocida, intenta nuevamente.")
                hablar("Opción no reconocida, intenta nuevamente.")
        else:
            opcion = input("Seleccione una opción: " if idioma_actual == "español" else "Select an option: ")
            if opcion == "1":
                ver_lista_completa()
            elif opcion == "2":
                cambiar_idioma()
            elif opcion == "3":
                letra = input("Ingrese la letra a buscar: " if idioma_actual == "español" else "Enter the letter to search: ")
                buscar_palabra(letra)
            elif opcion == "4":
                agregar_palabra()
            elif opcion == "5":
                mostrar_la_informacion_de_los_integrantes()
            elif opcion == "6":
                print("¡Hasta Luego! 👋 " if idioma_actual == "español" else "Goodbye! 👋")
                hablar("¡Hasta Luego!" if idioma_actual == "español" else "Goodbye!")
                break 
            else:
                print("Opción inválida. Intenta Nuevamente." if idioma_actual == "español" else "Invalid Option. Please try again.")
                hablar("Opción inválida. Intenta Nuevamente." if idioma_actual == "español" else "Invalid Option. Please try again.")

if __name__ == "__main__":
    menu()
