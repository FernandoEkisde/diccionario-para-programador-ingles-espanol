import speech_recognition as sr
import pyttsx3

# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()

# Idioma actual
idioma_actual = "español"

# Diccionario de términos de programación
diccionario_programacion = {

    "abstracción": {
        "definicion": ("Concepto de simplificar problemas complejos ocultando detalles innecesarios.", 
                       "Concept of simplifying complex problems by hiding unnecessary details."),
        "ejemplo": ("La abstracción permite a los programadores enfocarse en los aspectos más importantes de un problema.", 
                    "Abstraction allows programmers to focus on the most important aspects of a problem.")
    },
    "algoritmo": {
        "definicion": ("Conjunto de instrucciones o reglas bien definidas para resolver un problema.", 
                       "Set of well-defined instructions or rules to solve a problem."),
        "ejemplo": ("Un algoritmo de búsqueda permite encontrar un elemento específico dentro de una lista de datos.", 
                    "A search algorithm allows finding a specific element within a list of data.")
    },
    "bucle": {
        "definicion": ("Estructura de control que permite repetir un bloque de código múltiples veces.", 
                       "Control structure that allows repeating a block of code multiple times."),
        "ejemplo": ("Un bucle 'for' se utiliza para iterar sobre una lista de elementos.", 
                    "A 'for' loop is used to iterate over a list of elements.")
    },
    "clase": {
        "definicion": ("Plantilla para crear objetos que define sus propiedades y métodos.", 
                       "Template for creating objects that defines their properties and methods."),
        "ejemplo": ("Una clase 'Coche' puede tener propiedades como 'color' y 'modelo'.", 
                    "A 'Car' class can have properties like 'color' and 'model'.")
    },
    "condicional": {
        "definicion": ("Estructura que permite ejecutar código basado en una condición.", 
                       "Structure that allows executing code based on a condition."),
        "ejemplo": ("Un condicional 'if' se utiliza para ejecutar código solo si se cumple una condición.", 
                    "An 'if' conditional is used to execute code only if a condition is met.")
    },
    "función": {
        "definicion": ("Bloque de código reutilizable que realiza una tarea específica.", 
                       "Reusable block of code that performs a specific task."),
        "ejemplo": ("Una función puede calcular la suma de dos números y devolver el resultado.", 
                    "A function can calculate the sum of two numbers and return the result.")
    },
    "variable": {
        "definicion": ("Espacio de almacenamiento que tiene un nombre y puede contener un valor.", 
                       "Storage space that has a name and can contain a value."),
        "ejemplo": ("Una variable 'edad' puede almacenar la edad de una persona.", 
                    "A variable 'age' can store a person's age.")
    },
    "sintaxis": {
        "definicion": ("Conjunto de reglas que define la estructura de un lenguaje de programación.", 
                       "Set of rules that defines the structure of a programming language."),
        "ejemplo": ("Cada lenguaje de programación tiene su propia sintaxis que debe seguirse.", 
                    "Each programming language has its own syntax that must be followed.")
    },
    "excepción": {
        "definicion": ("Evento que ocurre durante la ejecución de un programa y altera su flujo normal.", 
                       "Event that occurs during the execution of a program and alters its normal flow."),
        "ejemplo": ("Las excepciones se pueden manejar con bloques 'try' y 'except'.", 
                    "Exceptions can be handled with 'try' and 'except' blocks.")
    },
    "módulo": {
        "definicion": ("Archivo que contiene definiciones de funciones y variables que se pueden reutilizar.", 
                       "File that contains definitions of functions and variables that can be reused."),
        "ejemplo": ("Un módulo puede contener funciones matemáticas que se pueden importar en otros programas.", 
                    "A module can contain mathematical functions that can be imported into other programs.")
    },
    "bucle anidado": {
        "definicion": ("Bucle dentro de otro bucle.", 
                       "Loop inside another loop."),
        "ejemplo": ("Los bucles anidados se utilizan para iterar sobre estructuras de datos multidimensionales.", 
                    "Nested loops are used to iterate over multidimensional data structures.")
    },
    "recursión": {
        "definicion": ("Cuando una función se llama a sí misma para resolver un problema.", 
                       "When a function calls itself to solve a problem."),
        "ejemplo": ("La recursión se utiliza a menudo en algoritmos de búsqueda y ordenamiento.", 
                    "Recursion is often used in search and sorting algorithms.")
    },
    "parámetro": {
        "definicion": ("Variable que se utiliza en la definición de una función para recibir un argumento.", 
                       "Variable used in the definition of a function to receive an argument."),
        "ejemplo": ("Una función puede tener parámetros que permiten personalizar su comportamiento.", 
                    "A function can have parameters that allow customizing its behavior.")
    },
    "tipo de dato": {
        "definicion": ("Clasificación de los datos que determina qué tipo de valores puede contener.", 
                       "Classification of data that determines what type of values it can hold."),
        "ejemplo": ("Los tipos de datos incluyen enteros, flotantes y cadenas.", 
                    "Data types include integers, floats, and strings.")
    },
    "booleano": {
        "definicion": ("Tipo de dato que puede tener solo dos valores: verdadero o falso.", 
                       "Data type that can have only two values: true or false."),
        "ejemplo": ("Una variable booleana puede usarse para controlar el flujo de un programa.", 
                    "A boolean variable can be used to control the flow of a program.")
    },
    "string": {
        "definicion": ("Tipo de dato que representa una secuencia de caracteres.", 
                       "Data type that represents a sequence of characters."),
        "ejemplo": ("Una cadena puede contener texto como 'Hola, mundo!'.", 
                    "A string can contain text like 'Hello, world!'.")
    },
    "lista": {
        "definicion": ("Colección ordenada de elementos que puede contener diferentes tipos de datos.", 
                       "Ordered collection of elements that can contain different data types."),
        "ejemplo": ("Una lista puede contener números, cadenas y otros objetos.", 
                    "A list can contain numbers, strings, and other objects.")
    },
    "diccionario": {
        "definicion": ("Estructura de datos que almacena pares clave-valor.", 
                       "Data structure that stores key-value pairs."),
        "ejemplo": ("Un diccionario puede almacenar información como {'nombre': 'Juan', 'edad': 30}.", 
                    "A dictionary can store information like {'name': 'John', 'age': 30}.")
    },
    "tupla": {
        "definicion": ("Colección ordenada e inmutable de elementos.", 
                       "Ordered and immutable collection of elements."),
        "ejemplo": ("Una tupla puede contener coordenadas como (10, 20).", 
                    "A tuple can contain coordinates like (10, 20).")
    },
    "conjunto": {
        "definicion": ("Colección no ordenada de elementos únicos.", 
                       "Unordered collection of unique elements."),
        "ejemplo": ("Un conjunto puede contener elementos como {1, 2, 3}.", 
                    "A set can contain elements like {1, 2, 3}.")
    },
    "función anónima": {
        "definicion": ("Función que no tiene un nombre definido.", 
                       "Function that does not have a defined name."),
        "ejemplo": ("Las funciones anónimas se pueden crear usando la palabra clave 'lambda'.", 
                    "Anonymous functions can be created using the 'lambda' keyword.")
    },
    "callback": {
        "definicion": ("Función que se pasa como argumento a otra función y se ejecuta después.", 
                       "Function that is passed as an argument to another function and is executed later."),
        "ejemplo": ("Las funciones de callback son comunes en programación asíncrona.", 
                    "Callback functions are common in asynchronous programming.")
    },
    "debugging": {
        "definicion": ("Proceso de encontrar y corregir errores en el código.", 
                       "Process of finding and fixing errors in the code."),
        "ejemplo": ("El debugging es esencial para asegurar que el programa funcione correctamente.", 
                    "Debugging is essential to ensure that the program works correctly.")
    },
    "sistema de control de versiones": {
        "definicion": ("Herramienta que permite gestionar cambios en el código fuente.", 
                       "Tool that allows managing changes in source code."),
        "ejemplo": ("Git es un sistema de control de versiones muy utilizado en el desarrollo de software.", 
                    "Git is a widely used version control system in software development.")
    },
    "API": {
        "definicion": ("Interfaz de Programación de Aplicaciones, permite la comunicación entre diferentes sistemas.", 
                       "Application Programming Interface, allows communication between different systems."),
        "ejemplo": ("Las APIs permiten que diferentes aplicaciones se comuniquen entre sí.", 
                    "APIs Is allow different applications to communicate with each other.")
    },
    "microservicios": {
        "definicion": ("Arquitectura que estructura una aplicación como una colección de servicios pequeños y autónomos.", 
                       "Architecture that structures an application as a collection of small, autonomous services."),
        "ejemplo": ("Los microservicios permiten desarrollar y desplegar componentes de forma independiente.", 
                    "Microservices allow developing and deploying components independently.")
    },
    "programación orientada a objetos": {
        "definicion": ("Paradigma de programación que utiliza objetos y clases.", 
                       "Programming paradigm that uses objects and classes."),
        "ejemplo": ("La programación orientada a objetos permite modelar el mundo real en código.", 
                    "Object-oriented programming allows modeling the real world in code.")
    },
    "patrones de diseño": {
        "definicion": ("Soluciones reutilizables a problemas comunes en el diseño de software.", 
                       "Reusable solutions to common problems in software design."),
        "ejemplo": ("El patrón de diseño Singleton asegura que una clase tenga una única instancia.", 
                    "The Singleton design pattern ensures that a class has a single instance.")
    },
    "multihilo": {
        "definicion": ("Técnica que permite la ejecución concurrente de múltiples hilos de ejecución.", 
                       "Technique that allows concurrent execution of multiple threads."),
        "ejemplo": ("La programación multihilo mejora la eficiencia de las aplicaciones al realizar tareas simultáneamente.", 
                    "Multithreading improves application efficiency by performing tasks simultaneously.")
    },
    "caché": {
        "definicion": ("Almacenamiento temporal de datos para acelerar el acceso a información frecuentemente utilizada.", 
                       "Temporary storage of data to speed up access to frequently used information."),
        "ejemplo": ("Los navegadores web utilizan caché para almacenar recursos y mejorar la velocidad de carga.", 
                    "Web browsers use cache to store resources and improve loading speed.")
    },
    "servidor": {
        "definicion": ("Computadora o programa que proporciona servicios a otros programas o dispositivos.", 
                       "Computer or program that provides services to other programs or devices."),
        "ejemplo": ("Un servidor web entrega páginas web a los navegadores de los usuarios.", 
                    "A web server delivers web pages to users' browsers.")
    },
    "cliente": {
        "definicion": ("Programa o dispositivo que solicita servicios a un servidor.", 
                       "Program or device that requests services from a server."),
        "ejemplo": ("El navegador web actúa como un cliente al solicitar páginas web de un servidor.", 
                    "The web browser acts as a client by requesting web pages from a server.")
    },
    "red": {
        "definicion": ("Conjunto de computadoras interconectadas que pueden comunicarse entre sí.", 
                       "Set of interconnected computers that can communicate with each other."),
        "ejemplo": ("Las redes permiten compartir recursos como impresoras y archivos entre computadoras.", 
                    "Networks allow sharing resources like printers and files between computers.")
    },
    "protocolo": {
        "definicion": ("Conjunto de reglas que determinan cómo se comunican los dispositivos en una red.", 
                       "Set of rules that determine how devices communicate over a network."),
        "ejemplo": ("HTTP es un protocolo utilizado para la transferencia de datos en la web.", 
                    "HTTP is a protocol used for data transfer on the web.")
    },
    "cifrado": {
        "definicion": ("Proceso de convertir información en un formato seguro para protegerla.", 
                       "Process of converting information into a secure format to protect it."),
        "ejemplo": ("El cifrado se utiliza para proteger datos sensibles durante la transmisión.", 
                    "Encryption is used to protect sensitive data during transmission.")
    },
    "desarrollo ágil": {
        "definicion": ("Metodología de desarrollo de software que promueve la flexibilidad y la colaboración.", 
                       "Software development methodology that promotes flexibility and collaboration."),
        "ejemplo": ("El desarrollo ágil permite adaptarse rápidamente a los cambios en los requisitos del cliente.", 
                    "Agile development allows quickly adapting to changes in customer requirements.")
    },
    "pruebas unitarias": {
        "definicion": ("Pruebas que verifican el funcionamiento de componentes individuales del código.", 
                       "Tests that verify the functioning of individual components of the code."),
        "ejemplo": ("Las pruebas unitarias ayudan a detectar errores en etapas tempranas del desarrollo.", 
                    "Unit tests help detect errors in the early stages of development.")
    },
    "despliegue continuo": {
        "definicion": ("Práctica de automatizar el despliegue de aplicaciones en producción.", 
                       "Practice of automating the deployment of applications in production."),
        "ejemplo": ("El despliegue continuo reduce el tiempo necesario para llevar nuevas características al mercado.", 
                    "Continuous deployment reduces the time needed to bring new features to market.")
    },
    "contenedor": {
        "definicion": ("Unidad estándar de software que empaqueta el código y todas sus dependencias.", 
                       "Standard unit of software that packages code and all its dependencies."),
        "ejemplo": ("Los contenedores permiten ejecutar aplicaciones de manera consistente en diferentes entornos.", 
                    "Containers allow running applications consistently across different environments.")
    },
    "framework": {
        "definicion": ("Conjunto de herramientas y bibliotecas que facilitan el desarrollo de aplicaciones.", 
                       "Set of tools and libraries that facilitate application development."),
        "ejemplo": ("Un framework como Django facilita el desarrollo de aplicaciones web en Python.", 
                    "A framework like Django facilitates web application development in Python.")
    },
    "biblioteca": {
        "definicion": ("Colección de funciones y procedimientos que pueden ser utilizados por otros programas.", 
                       "Collection of functions and procedures that can be used by other programs."),
        "ejemplo": ("Una biblioteca de matemáticas puede proporcionar funciones para realizar cálculos complejos.", 
                    "A math library can provide functions for performing complex calculations.")
    },
    "script": {
        "definicion": ("Conjunto de instrucciones que se ejecutan en un entorno de programación.", 
                       "Set of instructions that are executed in a programming environment."),
        "ejemplo": ("Un script puede automatizar tareas repetitivas en un sistema.", 
                    "A script can automate repetitive tasks on a system.")
    },
    "sistema operativo": {
        "definicion": ("Software que gestiona el hardware y software de una computadora.", 
                       "Software that manages the hardware and software of a computer."),
        "ejemplo": ("Windows y Linux son ejemplos de sistemas operativos populares.", 
                    "Windows and Linux are examples of popular operating systems.")
    },
    "interfaz gráfica de usuario": {
        "definicion": ("Sistema que permite a los usuarios interactuar con dispositivos a través de elementos visuales.", 
                       "System that allows users to interact with devices through visual elements."),
        "ejemplo": ("Las interfaces gráficas de usuario facilitan la interacción con aplicaciones de software.", 
                    "Graphical user interfaces facilitate interaction with software applications.")
    },
    "terminal": {
        "definicion": ("Interfaz de línea de comandos para interactuar con el sistema operativo.", 
                       "Command line interface to interact with the operating system."),
        "ejemplo": ("La terminal permite ejecutar comandos y scripts directamente en el sistema operativo.", 
                    "The terminal allows executing commands and scripts directly in the operating system.")
    },
    "shell": {
        "definicion": ("Programa que proporciona una interfaz para interactuar con el sistema operativo.", 
                       "Program that provides an interface to interact with the operating system."),
        "ejemplo": ("El shell permite a los usuarios ejecutar comandos y scripts en el sistema.", 
                    "The shell allows users to execute commands and scripts on the system.")
    },
    "código de estado HTTP": {
        "definicion": ("Código que indica el resultado de una solicitud HTTP.", 
                       "Code that indicates the result of an HTTP request."),
        "ejemplo": ("El código 404 indica que la página solicitada no se encontró.", 
                    "The 404 code indicates that the requested page was not found.")
    },
    "optimización": {
        "definicion": ("Proceso de hacer que un sistema funcione de la manera más eficiente posible.", 
                       "Process of making a system work as efficiently as possible."),
        "ejemplo": ("La optimización del código puede mejorar el rendimiento de una aplicación.", 
                    "Code optimization can improve the performance of an application.")
    },
    "seguridad informática": {
        "definicion": ("Prácticas y tecnologías para proteger sistemas y datos de ataques y accesos no autorizados.", 
                       "Practices and technologies to protect systems and data from attacks and unauthorized access."),
        "ejemplo": ("La seguridad informática incluye el uso de firewalls y antivirus.", 
                    "Cybersecurity includes the use of firewalls and antivirus software.")
    },
    "firewall": {
        "definicion": ("Sistema que controla el tráfico de red y protege contra accesos no autorizados.", 
                       "System that controls network traffic and protects against unauthorized access."),
        "ejemplo": ("Un firewall puede bloquear conexiones no deseadas a una red.", 
                    "A firewall can block unwanted connections to a network.")
    },
    "antivirus": {
        "definicion": ("Software diseñado para detectar y eliminar virus y malware.", 
                       "Software designed to detect and remove viruses and malware."),
        "ejemplo": ("El software antivirus escanea el sistema en busca de amenazas.", 
                    "Antivirus software scans the system for threats.")
    },
    "phishing": {
        "definicion": ("Técnica de fraude en línea que busca obtener información confidencial de los usuarios.", 
                       "Online fraud technique that seeks to obtain confidential information from users."),
        "ejemplo": ("Los ataques de phishing a menudo utilizan correos electrónicos falsos para engañar a los usuarios.", 
                    "Phishing attacks often use fake emails to trick users.")
    },
    "criptografía": {
        "definicion": ("Práctica de proteger información mediante técnicas de codificación.", 
                       "Practice of protecting information through encoding techniques."),
        "ejemplo": ("La criptografía se utiliza para asegurar la comunicación en línea.", 
                    "Cryptography is used to secure online communication.")
    },
    "token": {
        "definicion": ("Elemento de seguridad que se utiliza para autenticar a un usuario o dispositivo.", 
                       "Security element used to authenticate a user or device."),
        "ejemplo": ("Los tokens se utilizan en sistemas de autenticación para verificar la identidad del usuario.", 
                    "Tokens are used in authentication systems to verify the user's identity.")
    },
    "autenticación": {
        "definicion": ("Proceso de verificar la identidad de un usuario o sistema.", 
                       "Process of verifying the identity of a user or system."),
        "ejemplo": ("La autenticación de dos factores añade una capa adicional de seguridad.", 
                    "Two-factor authentication adds an extra layer of security.")
    },
    "autorización": {
        "definicion": ("Proceso de determinar si un usuario tiene permiso para realizar una acción.", 
                       "Process of determining whether a user has permission to perform an action."),
        "ejemplo": ("La autorización se utiliza para controlar el acceso a recursos en un sistema.", 
                    "Authorization is used to control access to resources in a system.")
    },
    "sesión": {
        "definicion": ("Conjunto de interacciones entre un usuario y un sistema durante un período de tiempo.", 
                       "Set of interactions between a user and a system over a period of time."),
        "ejemplo": ("Las sesiones se utilizan para mantener el estado del usuario en aplicaciones web.", 
                    "Sessions are used to maintain user state in web applications.")
    },
    "ciberataque": {
        "definicion": ("Intento malicioso de acceder, dañar o robar información de un sistema.", 
                       "Malicious attempt to access, damage, or steal information from a system."),
        "ejemplo": ("Los ciberataques pueden comprometer la seguridad de datos sensibles.", 
                    "Cyber attacks can compromise the security of sensitive data.")
    },
    "red privada virtual": {
        "definicion": ("Tecnología que crea una conexión segura a través de una red pública.", 
                       "Technology that creates a secure connection over a public network."),
        "ejemplo": ("Las VPN se utilizan para proteger la privacidad en línea y acceder a contenido restringido.", 
                    "VPNs are used to protect online privacy and access restricted content.")
    },
    "sistema de gestión de contenido": {
        "definicion": ("Software que permite crear, gestionar y modificar contenido digital.", 
                       "Software that allows creating, managing, and modifying digital content."),
        "ejemplo": ("Los sistemas de gestión de contenido facilitan la creación de sitios web y blogs.", 
                    "Content management systems facilitate the creation of websites and blogs.")
    },
    "blog": {
        "definicion": ("Sitio web que se actualiza regularmente con contenido nuevo, generalmente en formato de artículos.", 
                       "Website that is regularly updated with new content, usually in the form of articles."),
        "ejemplo": ("Los blogs son una forma popular de compartir información y opiniones en línea.", 
                    "Blogs are a popular way to share information and opinions online.")
    },
    "e-commerce": {
    "definicion": ("Comercio electrónico, compra y venta de bienes y servicios a través de Internet.", 
                   "Electronic commerce, buying and selling goods and services over the Internet."),
    "ejemplo": ("Las plataformas de e-commerce permiten a los usuarios comprar productos en línea.", 
                "E-commerce platforms allow users to purchase products online.")
},

    "SEO": {
        "definicion": ("Optimización para motores de búsqueda, práctica de mejorar la visibilidad de un sitio web en los resultados de búsqueda.", 
                       "Search Engine Optimization, practice of improving a website's visibility in search results."),
        "ejemplo": ("El SEO es crucial para aumentar el tráfico a un sitio web.", 
                    "SEO is crucial for increasing traffic to a website.")
    },
    "marketing digital": {
        "definicion": ("Promoción de productos o servicios a través de plataformas digitales.", 
                       "Promotion of products or services through digital platforms."),
        "ejemplo": ("El marketing digital incluye estrategias como publicidad en redes sociales y marketing por correo electrónico.", 
                    "Digital marketing includes strategies like social media advertising and email marketing.")
    },
    "redes sociales": {
        "definicion": ("Plataformas en línea que permiten la interacción y el intercambio de contenido entre usuarios.", 
                       "Online platforms that allow interaction and content sharing among users."),
        "ejemplo": ("Las redes sociales son herramientas poderosas para la comunicación y el marketing.", 
                    "Social media are powerful tools for communication and marketing.")
    },
    "contenido viral": {
        "definicion": ("Contenido que se comparte rápidamente en Internet, alcanzando una gran audiencia.", 
                       "Content that is rapidly shared on the Internet, reaching a large audience."),
        "ejemplo": ("Los videos virales pueden generar millones de visitas en poco tiempo.", 
                    "Viral videos can generate millions of views in a short time.")
    },
    "influencer": {
        "definicion": ("Persona que tiene la capacidad de influir en las decisiones de compra de otros debido a su autoridad, conocimiento, posición o relación con su audiencia.", 
                       "Person who has the ability to influence the purchasing decisions of others due to their authority, knowledge, position, or relationship with their audience."),
        "ejemplo": ("Los influencers utilizan sus plataformas para promocionar productos y servicios.", 
                    "Influencers use their platforms to promote products and services.")
    },
    "algoritmo de recomendación": {
        "definicion": ("Sistema que sugiere productos o contenido a los usuarios basado en sus preferencias y comportamientos anteriores.", 
                       "System that suggests products or content to users based on their previous preferences and behaviors."),
        "ejemplo": ("Los algoritmos de recomendación se utilizan en plataformas como Netflix para sugerir películas.", 
                    "Recommendation algorithms are used on platforms like Netflix to suggest movies.")
    },
    "análisis predictivo": {
        "definicion": ("Uso de datos, algoritmos y técnicas de machine learning para identificar la probabilidad de resultados futuros.", 
                       "Use of data, algorithms, and machine learning techniques to identify the likelihood of future outcomes."),
        "ejemplo": ("El análisis predictivo se utiliza en marketing para anticipar el comportamiento del consumidor.", 
                    "Predictive analytics is used in marketing to anticipate consumer behavior.")
    },
    "inteligencia de negocios": {
        "definicion": ("Conjunto de estrategias y tecnologías para analizar datos de negocios y ayudar en la toma de decisiones.", 
                       "Set of strategies and technologies to analyze business data and assist in decision-making."),
        "ejemplo": ("Las herramientas de inteligencia de negocios permiten a las empresas tomar decisiones informadas basadas en datos.", 
                    "Business intelligence tools allow companies to make informed decisions based on data.")
    },
    "data warehouse": {
        "definicion": ("Sistema utilizado para almacenar y analizar grandes volúmenes de datos de diferentes fuentes.", 
                       "System used to store and analyze large volumes of data from different sources."),
        "ejemplo": ("Un data warehouse centraliza datos de múltiples sistemas para facilitar el análisis.", 
                    "A data warehouse centralizes data from multiple systems to facilitate analysis.")
    },
    "data lake": {
        "definicion": ("Almacenamiento de datos en su formato original, permitiendo el análisis posterior.", 
                       "Storage of data in its original format, allowing for later analysis."),
        "ejemplo": ("Los data lakes son útiles para almacenar grandes volúmenes de datos no estructurados.", 
                    "Data lakes are useful for storing large volumes of unstructured data.")
    },
    "ETL": {
        "definicion": ("Proceso de Extracción, Transformación y Carga de datos en un sistema de almacenamiento.", 
                       "Process of Extracting, Transforming, and Loading data into a storage system."),
        "ejemplo": ("El proceso ETL se utiliza para preparar datos para su análisis en un data warehouse.", 
                    " The ETL process is used to prepare data for analysis in a data warehouse.")
    },
    "deep learning": {
        "definicion": ("Subcampo de machine learning que utiliza redes neuronales profundas para el análisis de datos.", 
                       "Subfield of machine learning that uses deep neural networks for data analysis."),
        "ejemplo": ("El deep learning se utiliza en aplicaciones como el reconocimiento de voz y la visión por computadora.", 
                    "Deep learning is used in applications like speech recognition and computer vision.")
    },
    "procesamiento del lenguaje natural": {
        "definicion": ("Área de la inteligencia artificial que se ocupa de la interacción entre computadoras y humanos a través del lenguaje natural.", 
                       "Area of artificial intelligence that deals with the interaction between computers and humans through natural language."),
        "ejemplo": ("El procesamiento del lenguaje natural se utiliza en chatbots y asistentes virtuales.", 
                    "Natural language processing is used in chatbots and virtual assistants.")
    },
    "chatbot": {
        "definicion": ("Programa que simula una conversación con usuarios a través de texto o voz.", 
                       "Program that simulates a conversation with users through text or voice."),
        "ejemplo": ("Los chatbots se utilizan en atención al cliente para responder preguntas frecuentes.", 
                    "Chatbots are used in customer service to answer frequently asked questions.")
    },
    "realidad aumentada": {
        "definicion": ("Tecnología que superpone información digital sobre el mundo real.", 
                       "Technology that overlays digital information onto the real world."),
        "ejemplo": ("La realidad aumentada se utiliza en aplicaciones de juegos y educación para mejorar la experiencia del usuario.", 
                    "Augmented reality is used in gaming and education applications to enhance user experience.")
    },
    "realidad virtual": {
        "definicion": ("Simulación de un entorno tridimensional que puede ser explorado e interactuado por un usuario.", 
                       "Simulation of a three-dimensional environment that can be explored and interacted with by a user."),
        "ejemplo": ("La realidad virtual se utiliza en simulaciones de entrenamiento y entretenimiento.", 
                    "Virtual reality is used in training simulations and entertainment.")
    },
    "internet de las cosas": {
        "definicion": ("Red de dispositivos físicos conectados a Internet que pueden recopilar y compartir datos.", 
                       "Network of physical devices connected to the Internet that can collect and share data."),
        "ejemplo": ("Los dispositivos del Internet de las cosas pueden incluir termostatos inteligentes y cámaras de seguridad.", 
                    "Internet of Things devices can include smart thermostats and security cameras.")
    },
    "blockchain": {
        "definicion": ("Tecnología de registro distribuido que asegura la integridad y transparencia de las transacciones.", 
                       "Distributed ledger technology that ensures the integrity and transparency of transactions."),
        "ejemplo": ("Blockchain se utiliza en criptomonedas para registrar transacciones de manera segura.", 
                    "Blockchain is used in cryptocurrencies to securely record transactions.")
    },
    "criptomoneda": {
        "definicion": ("Moneda digital que utiliza criptografía para asegurar transacciones y controlar la creación de nuevas unidades.", 
                       "Digital currency that uses cryptography to secure transactions and control the creation of new units."),
        "ejemplo": ("Bitcoin es la criptomoneda más conocida y utilizada en el mundo.", 
                    "Bitcoin is the most well-known and widely used cryptocurrency in the world.")
    },
    "smart contract": {
        "definicion": ("Contrato autoejecutable con los términos del acuerdo directamente escritos en código.", 
                       "Self-executing contract with the terms of the agreement directly written into code."),
        "ejemplo": ("Los smart contracts se utilizan en blockchain para automatizar procesos y transacciones.", 
                    "Smart contracts are used in blockchain to automate processes and transactions.")
    },
    "fintech": {
        "definicion": ("Tecnología que busca mejorar y automatizar la entrega y uso de servicios financieros.", 
                       "Technology that seeks to improve and automate the delivery and use of financial services."),
        "ejemplo": ("Las aplicaciones de fintech permiten realizar transacciones financieras de manera rápida y segura.", 
                    "Fintech applications allow for fast and secure financial transactions.")
    },
    "edtech": {
        "definicion": ("Tecnología educativa que utiliza herramientas digitales para mejorar el aprendizaje y la enseñanza.", 
                       "Educational technology that uses digital tools to enhance learning and teaching."),
        "ejemplo": ("Las plataformas de edtech ofrecen cursos en línea y recursos educativos accesibles.", 
                    "Edtech platforms offer online courses and accessible educational resources.")
    },
    "healthtech": {
        "definicion": ("Tecnología que busca mejorar la atención médica y la salud a través de soluciones digitales"
                       "Technology that seeks to improve healthcare and health through digital solutions."),
        "ejemplo": ("Las aplicaciones de healthtech permiten a los pacientes monitorear su salud y comunicarse con médicos.", 
                    "Healthtech applications allow patients to monitor their health and communicate with doctors.")
    },
    "agrotech": {
        "definicion": ("Tecnología que busca mejorar la agricultura y la producción de alimentos.", 
                       "Technology that seeks to improve agriculture and food production."),
        "ejemplo": ("Las soluciones de agrotech utilizan sensores y datos para optimizar el rendimiento de los cultivos.", 
                    "Agrotech solutions use sensors and data to optimize crop yields.")
    },
    "proptech": {
        "definicion": ("Tecnología que busca mejorar la compra, venta y gestión de propiedades inmobiliarias.", 
                       "Technology that seeks to improve the buying, selling, and management of real estate."),
        "ejemplo": ("Las plataformas de proptech facilitan la búsqueda y compra de propiedades en línea.", 
                    "Proptech platforms facilitate the online search and purchase of properties.")
    },
    "insurtech": {
        "definicion": ("Tecnología que busca mejorar y modernizar la industria de seguros.", 
                       "Technology that seeks to improve and modernize the insurance industry."),
        "ejemplo": ("Las aplicaciones de insurtech permiten a los usuarios gestionar sus pólizas de seguro de manera eficiente.", 
                    "Insurtech applications allow users to efficiently manage their insurance policies.")
    },
    "mobility": {
        "definicion": ("Tecnología que busca mejorar el transporte y la movilidad urbana.", 
                       "Technology that seeks to improve transportation and urban mobility."),
        "ejemplo": ("Las soluciones de movilidad incluyen aplicaciones de transporte compartido y vehículos eléctricos.", 
                    "Mobility solutions include ride-sharing apps and electric vehicles.")
    },
    "smart city": {
        "definicion": ("Ciudad que utiliza tecnología para mejorar la calidad de vida de sus habitantes y la eficiencia de sus servicios.", 
                       "City that uses technology to improve the quality of life of its inhabitants and the efficiency of its services."),
        "ejemplo": ("Las ciudades inteligentes utilizan sensores para gestionar el tráfico y los recursos de manera eficiente.", 
                    "Smart cities use sensors to manage traffic and resources efficiently.")
    },
    "sostenibilidad": {
        "definicion": ("Práctica de utilizar recursos de manera que se satisfagan las necesidades actuales sin comprometer la capacidad de las futuras generaciones.", 
                       "Practice of using resources in a way that meets current needs without compromising the ability of future generations."),
        "ejemplo": ("Las iniciativas de sostenibilidad buscan reducir el impacto ambiental de las actividades humanas.", 
                    "Sustainability initiatives aim to reduce the environmental impact of human activities.")
    },
    "energía renovable": {
        "definicion": ("Energía que se obtiene de fuentes naturales que se reponen a sí mismas.", 
                       "Energy obtained from natural sources that replenish themselves."),
        "ejemplo": ("La energía solar y eólica son ejemplos de fuentes de energía renovable.", 
                    "Solar and wind energy are examples of renewable energy sources.")
    },
    "cambio climático": {
        "definicion": ("Alteraciones a largo plazo en las temperaturas y patrones climáticos de la Tierra.", 
                       "Long-term changes in Earth's temperatures and climate patterns."),
        "ejemplo": ("El cambio climático está provocando fenómenos meteorológicos extremos en todo el mundo.", 
                    "Climate change is causing extreme weather events worldwide.")
    },
    "economía circular": {
        "definicion": ("Modelo económico que busca minimizar el desperdicio y hacer un uso más eficiente de los recursos.", 
                       "Economic model that seeks to minimize waste and make more efficient use of resources."),
        "ejemplo": ("La economía circular promueve la reutilización y el reciclaje de materiales.", 
                    "The circular economy promotes the reuse and recycling of materials.")
    },
    "responsabilidad social corporativa": {
        "definicion": ("Práctica de las empresas de tener en cuenta el impacto social y ambiental de sus actividades.", 
                       "Practice of companies to consider the social and environmental impact of their activities."),
        "ejemplo": ("Las empresas que adoptan la responsabilidad social corporativa contribuyen al bienestar de la comunidad.", 
                    "Companies that adopt corporate social responsibility contribute to the well-being of the community.")
    },
    "ética en la tecnología": {
        "definicion": ("Estudio de los principios morales que guían el desarrollo y uso de la tecnología.", 
                       "Study of the moral principles that guide the development and use of technology."),
        "ejemplo": ("La ética en la tecnología es crucial para abordar problemas como la privacidad y la seguridad de los datos.", 
                    "Ethics in technology is crucial for addressing issues like data privacy and security.")
    },
    "privacidad de datos": {
        "definicion": ("Derecho de los individuos a controlar cómo se recopilan y utilizan sus datos personales.", 
                       "Right of individuals to control how their personal data is collected and used."),
        "ejemplo": ("Las leyes de privacidad de datos protegen la información personal de los usuarios.", 
                    "Data privacy laws protect users' personal information.")
    },
    "protección de datos": {
        "definicion": ("Conjunto de leyes y regulaciones que protegen la información personal de los individuos.", 
                       "Set of laws and regulations that protect individuals' personal information."),
        "ejemplo": ("El GDPR es un ejemplo de regulación de protección de datos en la Unión Europea.", 
                    "GDPR is an example of data protection regulation in the European Union.")
    },
    "GDPR": {
        "definicion": ("Reglamento General de Protección de Datos, legislación de la UE que protege la privacidad de los datos de los ciudadanos.", 
                       "General Data Protection Regulation, EU legislation that protects citizens' data privacy."),
        "ejemplo": ("El GDPR establece normas estrictas sobre cómo las empresas deben manejar los datos personales.", 
                    "GDPR sets strict rules on how companies must handle personal data.")
    },
    "ciberseguridad": {
        "definicion": ("Prácticas y tecnologías para proteger sistemas y datos de ataques y accesos no autorizados.", 
                       "Practices and technologies to protect systems and data from attacks and unauthorized access."),
        "ejemplo": ("La ciberseguridad es esencial para proteger la información sensible de las empresas.", 
                    "Cybersecurity is essential to protect sensitive information of companies.")
    },
    "análisis forense digital": {
        "definicion": ("Proceso de recuperación y análisis de datos de dispositivos digitales para investigaciones legales.", 
                       "Process of recovering and analyzing data from digital devices for legal investigations."),
        "ejemplo": ("El análisis forense digital se utiliza en investigaciones de delitos cibernéticos.", 
                    "Digital forensics is used in investigations of cyber crimes.")
    },
    "redes neuronales convolucionales": {
        "definicion": ("Tipo de red neuronal utilizada principalmente en el reconocimiento de imágenes y procesamiento de video.", 
                       "Type of neural network primarily used in image recognition and video processing."),
        "ejemplo": ("Las redes neuronales convolucionales son fundamentales en aplicaciones de visión por computadora.", 
                    "Convolutional neural networks are fundamental in computer vision applications.")
    }
}

miembros_equipo = [
    {
        "Nombre": "Gabriel Pedreros",
        "Edad": 17,
        "Rol": "Líder técnico y creador de código",
        "Alias": ["El arquitecto del código", "El visionario técnico"],
        "Translation": {
            "Name": "Gabriel Pedreros",
            "Age": 17,
            "Role": "Technical Leader and Code Creator",
            "Aliases": ["The Code Architect", "The Technical Visionary"]
        }
    },
    {
        "Nombre": "Jesús Vidal",
        "Edad": 16,
        "Rol": "Integrante de desarrollo",
        "Alias": ["El ejecutor del código", "El constructor ágil"],
        "Translation": {
            "Name": "Jesús Vidal",
            "Age": 16,
            "Role": "Development Member",
            "Aliases": ["The Code Executor", "The Agile Builder"]
        }
    },
    {
        "Nombre": "Maximiliano Veliz",
        "Edad": 17,
        "Rol": "Coordinador de pruebas y desarrollador",
        "Alias": ["El evaluador", "El crítico del código"],
        "Translation": {
            "Name": "Maximiliano Veliz",
            "Age": 17,
            "Role": "Testing Coordinator and Developer",
            "Aliases": ["The Evaluator", "The Code Critic"]
        }
    },
    {
        "Nombre": "Fernando Ibañez",
        "Edad": 16,
        "Rol": "Experto en GitHub",
        "Alias": ["El maestro de repositorios", "El guardián del repositorio"],
        "Translation": {
            "Name": "Fernando Ibañez",
            "Age": 16,
            "Role": "GitHub Expert",
            "Aliases": ["The Repository Master", "The Repository Guardian"]
        }
    },
    {
        "Nombre": "Matías Lara",
        "Edad": 17,
        "Rol": "Especialista en diseño de interfaces",
        "Alias": ["El artista del código", "El escultor digital"],
        "Translation": {
            "Name": "Matías Lara",
            "Age": 17,
            "Role": "Interface Design Specialist",
            "Aliases": ["The Code Artist", "The Digital Sculptor"]
        }
    },
    {
        "Nombre": "Valentina San Martín",
        "Edad": 16,
        "Rol": "Gestora de documentación y comunicación",
        "Alias": ["La estratega digital", "La narradora de datos"],
        "Translation": {
            "Name": "Valentina San Martín",
            "Age": 16,
            "Role": "Documentation and Communication Manager",
            "Aliases": ["The Digital Strategist", "The Data Storyteller"]
        }
    },
    {
        "Nombre": "Macarena Jamett",
        "Edad": 48,
        "Rol": "Profesora",
        "Alias": ["La mentora del código", "La guía pedagógica"],
        "Translation": {
            "Name": "Macarena Jamett",
            "Age": 48,
            "Role": "Professor",
            "Aliases": ["The Code Mentor", "The Pedagogical Guide"]
        }
    }
]


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
        "definicion": (definicion, traduccion),
        "ejemplo": (traduccion, definicion)  # Invertir para mantener la estructura
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
        definicion, traduccion = diccionario_programacion[palabra]["definicion"]
        mensaje_definicion = f"{palabra}: {definicion} ({traduccion})"
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
        definicion, _ = diccionario_programacion[palabra]["definicion"]
        hablar(definicion)
    else:
        mensaje_no_encontrada = mensajes_es["palabra_no_encontrada"] if idioma_actual == "español" else mensajes_en["palabra_no_encontrada"]
        print(mensaje_no_encontrada)
        hablar(mensaje_no_encontrada)

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
    menu()
