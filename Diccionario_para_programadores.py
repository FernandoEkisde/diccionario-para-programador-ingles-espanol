import speech_recognition as sr
import pyttsx3

# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()

# Idioma actual
idioma_actual = "español"

# Título
print("🪓 El Vocabulario del Berserker ⚔️")

# Diccionario de términos de programación
diccionario_programacion = {
    "abstracción": ("Concepto de simplificar problemas complejos ocultando detalles innecesarios.", "Abstraction"),
    "algoritmo": ("Conjunto de instrucciones o reglas bien definidas para resolver un problema.", "Algorithm"),
    "argumento": ("Valor que se pasa a una función cuando es llamada.", "Argument"),
    "booleano": ("Tipo de dato que puede tener solo dos valores: verdadero o falso.", "Boolean"),
    "bucle": ("Estructura de control que permite repetir un bloque de código múltiples veces.", "Loop"),
    "clase": ("Plantilla para crear objetos que define sus propiedades y métodos.", "Class"),
    "condicional": ("Estructura que permite ejecutar código basado en una condición.", "Conditional"),
    "función": ("Bloque de código reutilizable que realiza una tarea específica.", "Function"),
    "if": ("Palabra clave para crear una condición condicional.", "If Statement"),
    "for": ("Bucle que se usa para iterar sobre una secuencia.", "For Loop"),
    "while": ("Bucle que se ejecuta mientras una condición sea verdadera.", "While Loop"),
    "variable": ("Espacio de almacenamiento que tiene un nombre y puede contener un valor.", "Variable"),
    "return": ("Palabra clave que devuelve un valor de una función.", "Return"),
    "tipo de dato": ("Clasificación de los datos que determina qué tipo de valores puede contener.", "Data Type"),
    "string": ("Tipo de dato que representa una secuencia de caracteres.", "String"),
    "número": ("Tipo de dato que representa valores numéricos.", "Number"),
    "carácter": ("Tipo de dato que representa un solo símbolo.", "Character"),
    "lista": ("Colección ordenada de elementos que puede contener diferentes tipos de datos.", "List"),
    "diccionario": ("Estructura de datos que almacena pares clave-valor.", "Dictionary"),
    "tupla": ("Colección ordenada e inmutable de elementos.", "Tuple"),
    "conjunto": ("Colección no ordenada de elementos únicos.", "Set"),
    "excepción": ("Evento que ocurre durante la ejecución de un programa y altera su flujo normal.", "Exception"),
    "módulo": ("Archivo que contiene definiciones de funciones y variables que se pueden reutilizar.", "Module"),
    "paquete": ("Colección de módulos relacionados que se pueden distribuir y usar juntos.", "Package"),
    "importar": ("Instrucción que permite utilizar un módulo o paquete en un programa.", "Import"),
    "comentario": ("Texto en el código que no se ejecuta y se utiliza para explicar el código.", "Comment"),
    "indentación": ("Uso de espacios o tabulaciones para definir la estructura del código.", "Indentation"),
    "sintaxis": ("Conjunto de reglas que define la estructura de un lenguaje de programación.", "Syntax"),
    "compilador": ("Programa que traduce el código fuente a código máquina.", "Compiler"),
    "intérprete": ("Programa que ejecuta el código fuente línea por línea.", "Interpreter"),
    "debugging": ("Proceso de encontrar y corregir errores en el código.", "Debugging"),
    "bucle anidado": ("Bucle dentro de otro bucle.", "Nested Loop"),
    "función anónima": ("Función que no tiene un nombre definido.", "Anonymous Function"),
    "callback": ("Función que se pasa como argumento a otra función y se ejecuta después.", "Callback"),
    "recursión": ("Cuando una función se llama a sí misma para resolver un problema.", "Recursion"),
    "algoritmo de búsqueda": ("Método para encontrar un elemento en una colección de datos.", "Search Algorithm"),
    "algoritmo de ordenamiento": ("Método para reorganizar elementos en un orden específico.", "Sorting Algorithm"),
    "estructura de datos": ("Forma de organizar y almacenar datos para su uso eficiente.", "Data Structure"),
    "entrada": ("Datos que se proporcionan a un programa.", "Input"),
    "salida": ("Datos que un programa produce como resultado.", "Output"),
    "prototipo": ("Modelo inicial de un objeto o función.", "Prototype"),
    "interfaz": ("Conjunto de métodos que una clase debe implementar.", "Interface"),
    "herencia": (" Mecanismo que permite a una clase heredar propiedades de otra clase.", "Inheritance"),
    "instancia": ("Objeto creado a partir de una clase.", "Instance"),
    "método": ("Función que pertenece a una clase.", "Method"),
    "atributo": ("Variable que pertenece a una clase o instancia.", "Attribute"),
    "constructor": ("Método especial que se llama al crear un objeto.", "Constructor"),
    "destructor": ("Método que se llama al destruir un objeto.", "Destructor"),
    "polimorfismo": ("Capacidad de una función de comportarse diferente según el contexto.", "Polymorphism"),
    "encapsulamiento": ("Principio de ocultar los detalles internos de una clase.", "Encapsulation"),
    "namespace": ("Espacio que contiene un conjunto de identificadores únicos.", "Namespace"),
    "operador": ("Símbolo que indica una operación a realizar.", "Operator"),
    "parámetro": ("Variable que se utiliza en la definición de una función para recibir un argumento.", "Parameter"),
    "sistema de control de versiones": ("Herramienta que permite gestionar cambios en el código fuente.", "Version Control System"),
    "API": ("Interfaz de Programación de Aplicaciones, permite la comunicación entre diferentes sistemas.", "API"),
    "microservicios": ("Arquitectura que estructura una aplicación como una colección de servicios pequeños y autónomos.", "Microservices"),
    "sistemas distribuidos": ("Conjunto de computadoras que trabajan juntas para lograr un objetivo común.", "Distributed Systems"),
    "programación funcional": ("Paradigma que trata la computación como la evaluación de funciones matemáticas.", "Functional Programming"),
    "programación orientada a objetos": ("Paradigma de programación que utiliza objetos y clases.", "Object-Oriented Programming"),
    "patrones de diseño": ("Soluciones reutilizables a problemas comunes en el diseño de software.", "Design Patterns"),
    "multihilo": ("Técnica que permite la ejecución concurrente de múltiples hilos de ejecución.", "Multithreading"),
    "base de datos": ("Sistema que permite almacenar, modificar y extraer información de manera estructurada.", "Database"),
    "SQL": ("Lenguaje de consulta estructurado utilizado para interactuar con bases de datos.", "SQL"),
    "noSQL": ("Tipo de base de datos que no utiliza el modelo relacional.", "NoSQL"),
    "caché": ("Almacenamiento temporal de datos para acelerar el acceso a información frecuentemente utilizada.", "Cache"),
    "servidor": ("Computadora o programa que proporciona servicios a otros programas o dispositivos.", "Server"),
    "cliente": ("Programa o dispositivo que solicita servicios a un servidor.", "Client"),
    "red": ("Conjunto de computadoras interconectadas que pueden comunicarse entre sí.", "Network"),
    "protocolo": ("Conjunto de reglas que determinan cómo se comunican los dispositivos en una red.", "Protocol"),
    "cifrado": ("Proceso de convertir información en un formato seguro para protegerla.", "Encryption"),
    "desarrollo ágil": ("Metodología de desarrollo de software que promueve la flexibilidad y la colaboración.", "Agile Development"),
    "metodología": ("Conjunto de métodos y técnicas utilizadas en un proceso de desarrollo.", "Methodology"),
    "pruebas unitarias": ("Pruebas que verifican el funcionamiento de componentes individuales del código.", "Unit Testing"),
    "integración continua": ("Práctica de fusionar cambios de código frecuentemente para detectar errores rápidamente.", "Continuous Integration"),
    "despliegue continuo": ("Práctica de automatizar el despliegue de aplicaciones en producción.", "Continuous Deployment"),
    "devops": ("Conjunto de prácticas que combinan el desarrollo de software y las operaciones de TI.", "DevOps"),
    "contenedor": ("Unidad estándar de software que empaqueta el código y todas sus dependencias.", "Container"),
    "Docker": ("Plataforma que permite crear, desplegar y ejecutar aplicaciones en contenedores.", "Docker"),
    "Kubernetes": ("Sistema de orquestación para automatizar la implementación, escalado y gestión de aplicaciones en contenedores.", "Kubernetes"),
    "inteligencia artificial": ("Simulación de procesos de inteligencia humana por parte de sistemas computacionales.", "Artificial Intelligence"),
    "aprendizaje automático": ("Subcampo de la inteligencia artificial que utiliza algoritmos para aprender de datos.", "Machine Learning"),
    "red neuronal": ("Modelo computacional inspirado en el cerebro humano, utilizado en aprendizaje automático.", "Neural Network"),
    "big data": ("Conjunto de datos tan grandes y complejos que requieren herramientas especiales para su procesamiento.", "Big Data"),
    "análisis de datos": ("Proceso de inspeccionar, limpiar y modelar datos para descubrir información útil.", "Data Analysis"),
    "visualización de datos": ("Representación gráfica de datos para facilitar su comprensión.", "Data Visualization"),
    "minería de datos": ("Proceso de descubrir patrones y conocimientos a partir de grandes conjuntos de datos.", "Data Mining"),
    "computación en la nube": ("Modelo de entrega de servicios de computación a través de Internet.", "Cloud Computing"),
    "servicio web": ("Método de comunicación entre dispositivos a través de la web.", "Web Service"),
    "REST": ("Estilo arquitectónico para diseñar servicios web que utilizan HTTP.", "REST"),
    "SOAP": ("Protocolo para intercambiar información estructurada en la implementación de servicios web.", "SOAP"),
    "microservicio": ("Arquitectura que estructura una aplicación como un conjunto de servicios pequeños e independientes.", "Microservice"),
    "arquitectura de software": ("Estructura y organización de un sistema de software.", "Software Architecture"),
    "código abierto": ("Software cuyo código fuente es accesible y puede ser modificado por cualquier persona.", "Open Source"),
    "licencia": ("Condiciones bajo las cuales se puede usar, modificar y distribuir un software.", "License"),
    "sistema operativo": ("Software que gestiona el hardware y software de una computadora.", "Operating System"),
    "interfaz gráfica de usuario": ("Sistema que permite a los usuarios interactuar con dispositivos a través de elementos visuales.", "GUI"),
    "terminal": ("Interfaz de línea de comandos para interactuar con el sistema operativo.", "Terminal"),
    "shell": ("Programa que proporciona una interfaz para interactuar con el sistema operativo.", "Shell"),
    "script": ("Conjunto de instrucciones que se ejecutan en un entorno de programación.", "Script"),
    "framework": ("Conjunto de herramientas y bibliotecas que facilitan el desarrollo de aplicaciones.", "Framework"),
    "biblioteca": ("Colección de funciones y procedimientos que pueden ser utilizados por otros programas.", "Library"),
    "API RESTful": ("API que sigue los principios de REST para la comunicación entre sistemas.", "RESTful API"),
    "código de estado HTTP": ("Código que indica el resultado de una solicitud HTTP.", "HTTP Status Code"),
    "caché de navegador": ("Almacenamiento temporal de recursos web en el navegador para mejorar la velocidad de carga.", "Browser Cache"),
    "optimización": ("Proceso de hacer que un sistema funcione de la manera más eficiente posible.", "Optimization"),
    "seguridad informática": ("Prácticas y tecnologías para proteger sistemas y datos de ataques y accesos no autorizados.", "Cybersecurity"),
    "firewall": ("Sistema que controla el tráfico de red y protege contra accesos no autorizados.", "Firewall"),
    "antivirus": ("Software diseñado para detectar y eliminar virus y malware.", "Antivirus"),
    "phishing": ("Técnica de fraude en línea que busca obtener información confidencial de los usuarios.", "Phishing"),
    "criptografía": ("Práctica de proteger información mediante técnicas de codificación.", "Cryptography"),
    "token": ("Elemento de seguridad que se utiliza para autenticar a un usuario o dispositivo.", "Token"),
    "autenticación": ("Proceso de verificar la identidad de un usuario o sistema.", "Authentication"),
    "autorización": ("Proceso de determinar si un usuario tiene permiso para realizar una acción.", "Authorization"),
    "sesión": ("Conjunto de interacciones entre un usuario y un sistema durante un período de tiempo.", "Session"),
    "ciberataque": ("Intento malicioso de acceder, dañar o robar información de un sistema.", "Cyber Attack"),
    "red privada virtual": ("Tecnología que crea una conexión segura a través de una red pública.", "VPN"),
    "sistema de gestión de contenido": ("Software que permite crear, gestionar y modificar contenido digital.", "CMS"),
    "blog": ("Sitio web que se actualiza regularmente con contenido nuevo, generalmente en formato de artículos.", "Blog"),
    "e-commerce": ("Comercio electrónico, compra y venta de bienes y servicios a través de Internet.", "E-commerce"),
    "SEO": ("Optimización para motores de búsqueda, práctica de mejorar la visibilidad de un sitio web en los resultados de búsqueda.", "SEO"),
    "marketing digital": ("Promoción de productos o servicios a través de plataformas digitales.", "Digital Marketing"),
    "redes sociales": ("Plataformas en línea que permiten la interacción y el intercambio de contenido entre usuarios.", "Social Media"),
    "contenido viral": ("Contenido que se comparte rápidamente en Internet, alcanzando una gran audiencia.", "Viral Content"),
    "influencer": ("Persona que tiene la capacidad de influir en las decisiones de compra de otros debido a su autoridad, conocimiento, posición o relación con su audiencia.", "Influencer"),
    "algoritmo de recomendación": ("Sistema que sugiere productos o contenido a los usuarios basado en sus preferencias y comportamientos anteriores.", "Recommendation Algorithm"),
    "big data": ("Conjunto de datos tan grandes y complejos que requieren herramientas especiales para su procesamiento.", "Big Data"),
    "análisis predictivo": ("Uso de datos, algoritmos y técnicas de machine learning para identificar la probabilidad de resultados futuros.", "Predictive Analytics"),
    "inteligencia de negocios": ("Conjunto de estrategias y tecnologías para analizar datos de negocios y ayudar en la toma de decisiones.", "Business Intelligence"),
    "data warehouse": ("Sistema utilizado para almacenar y analizar grandes volúmenes de datos de diferentes fuentes.", "Data Warehouse"),
    "data lake": ("Almacenamiento de datos en su formato original, permitiendo el análisis posterior.", "Data Lake"),
    "ETL": ("Proceso de Extracción, Transformación y Carga de datos en un sistema de almacenamiento.", "ETL"),
    "machine learning": ("Subcampo de la inteligencia artificial que utiliza algoritmos para aprender de datos.", "Machine Learning"),
    "deep learning": ("Subcampo de machine learning que utiliza redes neuronales profundas para el análisis de datos.", "Deep Learning"),
    "redes neuronales": ("Modelo computacional inspirado en el cerebro humano, utilizado en aprendizaje automático.", "Neural Networks"),
    "procesamiento del lenguaje natural": ("Área de la inteligencia artificial que se ocupa de la interacción entre computadoras y humanos a través del lenguaje natural.", "Natural Language Processing"),
    "chatbot": ("Programa que simula una conversación con usuarios a través de texto o voz.", "Chatbot"),
    "realidad aumentada": ("Tecnología que superpone información digital sobre el mundo real.", "Augmented Reality"),
    "realidad virtual": ("Simulación de un entorno tridimensional que puede ser explorado e interactuado por un usuario.", "Virtual Reality"),
    "internet de las cosas": ("Red de dispositivos físicos conectados a Internet que pueden recopilar y compartir datos.", "Internet of Things"),
    "blockchain": ("Tecnología de registro distribuido que asegura la integridad y transparencia de las transacciones.", "Blockchain"),
    "criptomoneda": ("Moneda digital que utiliza criptografía para asegurar transacciones y controlar la creación de nuevas unidades.", "Cryptocurrency"),
    "smart contract": ("Contrato autoejecutable con los términos del acuerdo directamente escritos en código.", "Smart Contract"),
    "fintech": ("Tecnología que busca mejorar y automatizar la entrega y uso de servicios financieros.", "Fintech"),
    "edtech": ("Tecnología educativa que utiliza herramientas digitales para mejorar el aprendizaje y la enseñanza.", "Edtech"),
    "healthtech": ("Tecnología que busca mejorar la atención médica y la salud a través de soluciones digitales.", "Healthtech"),
    "agrotech": ("Tecnología que busca mejorar la agricultura y la producción de alimentos.", "Agrotech"),
    "proptech": ("Tecnología que busca mejorar la compra, venta y gestión de propiedades inmobiliarias.", "Proptech"),
    "insurtech": ("Tecnología que busca mejorar y modernizar la industria de seguros.", "Insurtech"),
    "mobility": ("Tecnología que busca mejorar el transporte y la movilidad urbana.", "Mobility"),
    "smart city": ("Ciudad que utiliza tecnología para mejorar la calidad de vida de sus habitantes y la eficiencia de sus servicios.", "Smart City"),
    "sostenibilidad": ("Práctica de utilizar recursos de manera que se satisfagan las necesidades actuales sin comprometer la capacidad de las futuras generaciones.", "Sustainability"),
    "energía renovable": ("Energía que se obtiene de fuentes naturales que se reponen a sí mismas.", "Renewable Energy"),
    "cambio climático": ("Alteraciones a largo plazo en las temperaturas y patrones climáticos de la Tierra.", "Climate Change"),
    "economía circular": ("Modelo económico que busca minimizar el desperdicio y hacer un uso más eficiente de los recursos.", "Circular Economy"),
    "responsabilidad social corporativa": ("Práctica de las empresas de tener en cuenta el impacto social y ambiental de sus actividades.", "Corporate Social Responsibility"),
    "ética en la tecnología": ("Estudio de los principios morales que guían el desarrollo y uso de la tecnología.", "Ethics in Technology"),
    "privacidad de datos": ("Derecho de los individuos a controlar cómo se recopilan y utilizan sus datos personales.", "Data Privacy"),
    "protección de datos": ("Conjunto de leyes y regulaciones que protegen la información personal de los individuos.", "Data Protection"),
    "GDPR": ("Reglamento General de Protección de Datos, legislación de la UE que protege la privacidad de los datos de los ciudadanos.", "GDPR"),
    "ciberseguridad": ("Prácticas y tecnologías para proteger sistemas y datos de ataques y accesos no autorizados.", "Cybersecurity"),
    "análisis forense digital": ("Proceso de recuperación y análisis de datos de dispositivos digitales para investigaciones legales.", "Digital Forensics"),
    "redes neuronales convolucionales": ("Tipo de red neuronal utilizada principalmente en el procesamiento de imágenes.", "Convolutional Neural Networks"),
    "redes neuronales recurrentes": ("Tipo de red neuronal que se utiliza para procesar secuencias de datos.", "Recurrent Neural Networks"),
    "algoritmo genético": ("Método de optimización que simula el proceso de selección natural.", "Genetic Algorithm"),
    "optimización de hiperparámetros": ("Proceso de ajustar los parámetros de un modelo para mejorar su rendimiento.", "Hyperparameter Optimization"),
    "transfer learning": ("Técnica de machine learning donde un modelo entrenado en una tarea se reutiliza en otra tarea relacionada.", "Transfer Learning"),
    "análisis de sentimientos": ("Uso de técnicas de procesamiento de lenguaje natural para determinar la actitud de un hablante o escritor.", "Sentiment Analysis"),
    "reconocimiento de voz": ("Tecnología que permite a las computadoras interpretar y procesar el habla humana.", "Speech Recognition"),
    "visión por computadora": ("Campo de la inteligencia artificial que permite a las computadoras interpretar y entender imágenes y videos.", "Computer Vision"),
    "realidad mixta": ("Combinación de elementos de realidad aumentada y realidad virtual.", "Mixed Reality"),
    "tecnología de reconocimiento facial": ("Sistema que identifica o verifica la identidad de una persona a partir de su rostro.", "Facial Recognition Technology"),
    "drones": ("Vehículos aéreos no tripulados que pueden ser controlados de forma remota o volar de manera autónoma.", "Drones"),
    "robótica": ("Campo de la ingeniería que se ocupa del diseño, construcción y operación de robots.", "Robotics"),
    "automación": ("Uso de tecnología para realizar tareas con mínima intervención humana.", "Automation"),
    "internet de las cosas industrial": ("Aplicación del IoT en entornos industriales para mejorar la eficiencia y la productividad.", "Industrial IoT"),
    "ciudades inteligentes": ("Áreas urbanas que utilizan tecnología para mejorar la calidad de vida y la eficiencia de los servicios.", "Smart Cities"),
    "tecnología de cadena de bloques": ("Sistema de registro digital que asegura la integridad y transparencia de las transacciones.", "Blockchain Technology"),
    "sistemas de gestión de relaciones con clientes": ("Software que ayuda a las empresas a gestionar interacciones con clientes y datos relacionados.", "CRM Systems"),
    "sistemas de gestión de recursos empresariales": ("Software que integra todas las facetas de una operación empresarial, incluyendo planificación, fabricación, ventas y marketing.", "ERP Systems"),
    "inteligencia artificial explicativa": ("Área de la inteligencia artificial que busca hacer que los modelos sean más comprensibles para los humanos.", "Explainable AI"),
    "tecnología de asistencia": ("Tecnología diseñada para ayudar a las personas con discapacidades a realizar tareas diarias.", "Assistive Technology"),
    "tecnología de seguimiento ocular": ("Sistema que utiliza cámaras para rastrear el movimiento de los ojos y permitir la interacción con dispositivos.", "Eye Tracking Technology"),
    "tecnología de impresión 3D": ("Proceso de crear objetos tridimensionales a partir de un modelo digital.", "3D Printing Technology"),
    "tecnología de realidad virtual": ("Simulación de un entorno tridimensional que puede ser explorado e interactuado por un usuario.", "Virtual Reality Technology"),
    "tecnología de realidad aumentada": ("Superposición de información digital sobre el mundo real.", "Augmented Reality Technology"),
    "tecnología de gamificación": ("Uso de elementos de diseño de juegos en contextos no lúdicos para mejorar la participación y el aprendizaje.", "Gamification Technology"),
    "tecnología de aprendizaje adaptativo": ("Método de enseñanza que personaliza el contenido y el ritmo de aprendizaje según las necesidades del estudiante.", "Adaptive Learning Technology"),
    "tecnología de análisis de datos": ("Herramientas y técnicas utilizadas para analizar y extraer información de grandes conjuntos de datos.", "Data Analytics Technology"),
    "tecnología de automatización de procesos robóticos": ("Uso de software para automatizar tareas repetitivas y basadas en reglas.", "Robotic Process Automation"),
    "tecnología de gestión de proyectos ": ("Herramientas y técnicas utilizadas para planificar, ejecutar y supervisar proyectos.", "Project Management Technology"),
    "tecnología de colaboración": ("Herramientas que facilitan la comunicación y el trabajo en equipo entre individuos y grupos.", "Collaboration Technology"),
    "tecnología de análisis de redes sociales": ("Herramientas que analizan datos de redes sociales para obtener información sobre tendencias y comportamientos.", "Social Media Analytics Technology"),
    "tecnología de marketing automatizado": ("Uso de software para automatizar tareas de marketing y mejorar la eficiencia.", "Marketing Automation Technology"),
    "tecnología de gestión de contenido": ("Herramientas que permiten crear, gestionar y modificar contenido digital.", "Content Management Technology"),
    "tecnología de análisis de mercado": ("Herramientas y técnicas utilizadas para estudiar y analizar el mercado y la competencia.", "Market Analysis Technology"),
    "tecnología de gestión de la cadena de suministro": ("Software que ayuda a gestionar el flujo de bienes y servicios desde el proveedor hasta el cliente.", "Supply Chain Management Technology"),
    "tecnología de gestión de inventarios": ("Herramientas que permiten controlar y gestionar el inventario de productos.", "Inventory Management Technology"),
    "tecnología de gestión de recursos humanos": ("Software que ayuda a gestionar procesos relacionados con el personal y los empleados.", "Human Resource Management Technology"),
    "tecnología de análisis de rendimiento": ("Herramientas que evalúan el rendimiento de empleados, productos o servicios.", "Performance Analysis Technology"),
    "tecnología de gestión de riesgos": ("Herramientas y técnicas utilizadas para identificar, evaluar y mitigar riesgos en proyectos y negocios.", "Risk Management Technology"),
    "tecnología de gestión de calidad": ("Herramientas que aseguran que los productos y servicios cumplan con los estándares de calidad.", "Quality Management Technology"),
    "tecnología de gestión de relaciones con proveedores": ("Software que ayuda a gestionar las relaciones y comunicaciones con proveedores.", "Supplier Relationship Management Technology"),
    "tecnología de gestión de activos": ("Herramientas que permiten gestionar y optimizar el uso de activos de una organización.", "Asset Management Technology"),
    "tecnología de gestión de datos": ("Herramientas y técnicas utilizadas para almacenar, organizar y analizar datos.", "Data Management Technology"),
    "tecnología de gestión de la experiencia del cliente": ("Herramientas que ayudan a mejorar la experiencia del cliente a través de la personalización y el análisis.", "Customer Experience Management Technology"),
    "tecnología de gestión de la innovación": ("Herramientas que facilitan la creación y desarrollo de nuevas ideas y productos.", "Innovation Management Technology"),
    "tecnología de gestión de la sostenibilidad": ("Herramientas que ayudan a las organizaciones a implementar prácticas sostenibles.", "Sustainability Management Technology"),
    "tecnología de gestión de la diversidad": ("Herramientas que promueven la diversidad e inclusión en el lugar de trabajo.", "Diversity Management Technology"),
    "tecnología de gestión de la comunicación": ("Herramientas que facilitan la comunicación interna y externa de una organización.", "Communication Management Technology"),
    "tecnología de gestión de la reputación": ("Herramientas que ayudan a gestionar y mejorar la reputación de una marca o empresa.", "Reputation Management Technology"),
    "tecnología de gestión de la marca": ("Herramientas que ayudan a construir y gestionar la identidad de una marca.", "Brand Management Technology"),
    "tecnología de gestión de la experiencia del empleado": ("Herramientas que mejoran la experiencia de los empleados en el lugar de trabajo.", "Employee Experience Management Technology"),
    "tecnología de gestión de la formación": ("Herramientas que facilitan la capacitación y el desarrollo de habilidades de los empleados.", "Training Management Technology"),
    "tecnología de gestión de la salud y seguridad": ("Herramientas que ayudan a gestionar la salud y seguridad en el lugar de trabajo.", "Health and Safety Management Technology"),
    "tecnología de gestión de la cadena de valor": ("Herramientas que optimizan cada etapa de la cadena de valor de un producto o servicio.", "Value Chain Management Technology"),
    "tecnología de gestión de la logística": ("Herramientas que ayudan a gestionar el transporte y almacenamiento de productos.", "Logistics Management Technology"),
    "tecnología de gestión de la producción": ("Herramientas que optimizan los procesos de producción en una organización.", "Production Management Technology"),
    "tecnología de gestión de la distribución": ("Herramientas que ayudan a gestionar la distribución de productos a los clientes.", "Distribution Management Technology"),
}
miembros_equipo = [
    {
        "Nombre": "Gabriel Pedreros",
        "Edad": 17,
        "Rol": "Líder técnico y creador de código",
        "Alias": ["El arquitecto del código", "El visionario técnico"]
    },
    {
        "Nombre": "Jesús Vidal",
        "Edad": 16,
        "Rol": "Integrante de desarrollo",
        "Alias": ["El ejecutor del código", "El constructor ágil"]
    },
    {
        "Nombre": "Maximiliano Veliz",
        "Edad": 17,
        "Rol": "Coordinador de pruebas y desarrollador",
        "Alias": ["El evaluador", "El crítico del código"]
    },
    {
        "Nombre": "Fernando Ibañez",
        "Edad": 16,
        "Rol": "Experto en GitHub",
        "Alias": ["El maestro de repositorios", "El guardián del repositorio"]
    },
    {
        "Nombre": "Matías Lara",
        "Edad": 17,
        "Rol": "Especialista en diseño de interfaces",
        "Alias": ["El artista del código", "El escultor digital"]
    },
    {
        "Nombre": "Valentina San Martín",
        "Edad": 16,
        "Rol": "Gestora de documentación y comunicación",
        "Alias": ["La estratega digital", "La narradora de datos"]
    }
]

def hablar(texto):
    """Convierte texto a voz."""
    engine.say(texto)
    engine.runAndWait()

def reconocer_voz():
    """Reconoce comandos de voz."""
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("🎤 Escuchando...")
            hablar("Te escucho")
            audio = r.listen(source)
            texto = r.recognize_google(audio, language='es-ES' if idioma_actual == "español" else 'en-US')
            print(f"🗣️ Has dicho: {texto}")
            return texto.lower()
    except sr.UnknownValueError:
        print("❌ No he entendido lo que dijiste.")
        hablar("No he entendido, por favor repite")
        return None
    except sr.RequestError as e:
        print(f"⚠️ No se pudo obtener resultados de Google Speech Recognition; {e}")
        hablar("Ha ocurrido un error en el reconocimiento de voz")
        return None

def ver_lista_completa():
    """Muestra la lista completa de palabras y sus definiciones."""
    print("\n--- Lista Completa de Palabras ---")
    for palabra, (definicion, traduccion) in diccionario_programacion.items():
        print(f"{palabra}: {definicion} ({traduccion})")
        hablar(f"{palabra}: {definicion}")

def cambiar_idioma():
    """Cambia el idioma del programa."""
    global idioma_actual
    if idioma_actual == "español":
        idioma_actual = "inglés"
        print("🌐 Idioma cambiado a inglés.")
        hablar("Language changed to English.")
    else:
        idioma_actual = "español"
        print("🌐 Idioma cambiado a español.")
        hablar("Idioma cambiado a español.")

def agregar_palabra():
    """Agrega una nueva palabra al diccionario."""
    palabra = input("✍️ Introduce la nueva palabra: ")
    definicion = input("📖 Introduce la definición: ")
    traduccion = input("🌍 Introduce la traducción: ")
    diccionario_programacion[palabra] = (definicion, traduccion)
    print(f"✅ Palabra '{palabra}' añadida exitosamente.")
    hablar(f"Palabra '{palabra}' añadida exitosamente.")

def mostrar_la_informacion_de_los_integrantes():
    """Muestra la información de los integrantes del equipo."""
    print("\n--- Información de los Integrantes ---")
    for miembro in miembros_equipo:
        print(f"Nombre: {miembro['Nombre']}, Edad: {miembro['Edad']}, Rol: {miembro['Rol']}, Alias: {', '.join(miembro['Alias'])}")
        hablar(f"Nombre: {miembro['Nombre']}, Edad: {miembro['Edad']}, Rol: {miembro['Rol']}, Alias: {', '.join(miembro['Alias'])}")

def buscar_palabra(diccionario, letra):
    """Busca palabras que comienzan con una letra específica."""
    print(f"\n--- Palabras que comienzan con '{letra}' ---")
    for palabra in diccionario.keys():
        if palabra.startswith(letra):
            print(palabra)
            hablar(palabra)

def ver_definicion():
    """Muestra la definición de un término específico."""
    palabra = input("🔍 Introduce la palabra de la que deseas ver la definición: ")
    if palabra in diccionario_programacion:
        definicion, traduccion = diccionario_programacion[palabra]
        print(f"{palabra}: {definicion} ({traduccion})")
        hablar(f"{palabra}: {definicion}")
    else:
        print("❌ Palabra no encontrada.")
        hablar("Palabra no encontrada.")

def escuchar_definicion():
    """Escucha la definición de un término específico."""
    palabra = input("🔊 Introduce la palabra de la que deseas escuchar la definición: ")
    if palabra in diccionario_programacion:
        definicion, _ = diccionario_programacion[palabra]
        hablar(definicion)
    else:
        print("❌ Palabra no encontrada.")
        hablar("Palabra no encontrada.")

def menu():
    """Muestra el menú principal y gestiona las opciones del usuario."""
    mensaje_bienvenida = "¡Bienvenido/a al Diccionario de Código Viking! 🪓 Nuestro programa te ofrece las siguientes funciones: Explorar el catálogo de palabras, opciones multilingües, búsqueda avanzada, contribuir con nuevos términos y conocer a nuestro equipo. ¿Qué te gustaría explorar primero?"

    print(mensaje_bienvenida)
    hablar(mensaje_bienvenida)

    while True:
        print("\n--- Menú ---")
        opciones = [
            "1. Ver la Lista Completa de Palabras ",  
            "2. Cambiar Idioma ",                       
            "3. Agregar Palabra Nueva ",                
            "4. Información de los integrantes",          
            "5. Buscar por letra ",                     
            "6. Ver definición de un término específico", 
            "7. Escuchar definición de un término específico",
            "8. Salir"
        ]
        for opcion in opciones:
            print(opcion)

        usar_voz = input("¿Quieres usar voz para seleccionar una opción? (s/n): ")
        if usar_voz.lower() == 's':
            opcion = reconocer_voz()
            if opcion is None:
                continue  # Si no se entendió, vuelve a preguntar
            if "ver la lista" in opcion:
                ver_lista_completa()
            elif "cambiar idioma" in opcion:
                cambiar_idioma()
            elif "agregar" in opcion:
                agregar_palabra()
            elif "información" in opcion:
                mostrar_la_informacion_de_los_integrantes()
            elif "buscar" in opcion:
                letra = input("Ingrese la letra a buscar: ")
                buscar_palabra(diccionario_programacion, letra)
            elif "definición" in opcion:
                ver_definicion()
            elif "escuchar definición" in opcion:
                escuchar_definicion()
            elif "salir" in opcion:
                print("¡Hasta Luego! 👋")
                hablar("¡Hasta Luego!")
                break
            else:
                print("❌ Opción no reconocida, intenta nuevamente.")
                hablar("Opción no reconocida, intenta nuevamente.")
        else:
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                ver_lista_completa()
            elif opcion == "2":
                cambiar_idioma()
            elif opcion == "3":
                agregar_palabra()
            elif opcion == "4":
                mostrar_la_informacion_de_los_integrantes()
            elif opcion == "5":
                letra = input("Ingrese la letra a buscar: ")
                buscar_palabra(diccionario_programacion, letra)
            elif opcion == "6":
                ver_definicion()
            elif opcion == "7":
                escuchar_definicion()
            elif opcion == "8":
                print("¡Hasta Luego! 👋")
                hablar("¡Hasta Luego!")
                break 
            else:
                print("❌ Opción inválida. Intenta Nuevamente.")

if __name__ == "__main__":
    menu()
