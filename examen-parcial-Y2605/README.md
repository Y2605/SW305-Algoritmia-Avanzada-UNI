[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/odMiGFo-)
# SW 305: Examen Parcial

## Instrucciones

- **Tienen que hacer uso del repositorio de GitHub Classroom para el envío del examen, en el tiempo establecido.** No se aceptarán envíos en otros medios (repositorios privados, correo electrónico, etc) o fuera de tiempo.
- Para evitar inconvenientes, se requiere que envíen sus soluciones parciales a la nube (haciendo _Commit_ y _Push_) por lo menos cada media hora.
- Está permitido consultar el material de clase (diapositivas, libros, código fuente, y apuntes personales). **Consultar recursos como Google, ChatGPT, u otros compañeros está estrictamente prohibido, y se aplicará el reglamento de ser detectado.**
- Utilice la notación y el estilo de programación desarrollado en clase. Se disminuirá puntaje en caso contrario.
- Sólamente ingrese código en las secciones marcadas como `[INICIO]` y `[FIN]`. No edite otras partes de `laboratorio.py`, u otros archivos.
- La instrucción `pass` es un texto temporal. Puede eliminarlo para implementar su solución.
- El uso de `import` está prohibido. No está permitido importar o instalar librerías externas.
- Utilice la sección final de `laboratorio.py` para probar sus soluciones. Todas sus soluciones deben contener pruebas, que demuestren su funcionamiento.

## Primer Problema (6 puntos)

En el archivo `laboratorio.py`, complete la implementación de la clase `ListaEnlazadaOrdenada`, correspondiente a una **lista doblemente enlazada** que preserva sus elemenetos ordenados. **No está permitido utilizar las rutinas de ordenamiento de la librería estándar de Python, como `sort` y `sorted`.** Considere lo siguiente en su implementación:

* El método `agregar()` agrega instancias de `NodoDoble` (ya definida en `laboratorio.py`) a la lista enlazada, de modo que sus valores estén ordenados de forma ascendente. Esto quiere decir que el nodo que contiene al elemento de menor valor debe estar almacenado en el campo `cabeza_lista`, mientras que el nodo con el elemento de mayor valor debe ser accesible desde el campo `final_lista`. Por ejemplo:

    ```python
    lista_enlazada = ListaEnlazadaOrdenada()

    lista_enlazada.agregar("Miguel")
    lista_enlazada.agregar("Francisco")
    lista_enlazada.agregar("Alfonso")
    lista_enlazada.agregar("Jose")
    ```

    En este caso, la lista enlazada debe preservar el siguiente orden: `"Alfonso" -> "Francisco"-> "Jose"-> "Miguel"`. 

* El método `esta_ordenada()` debe retornar `True` en caso la lista enlazada se encuentre ordenada, y `False` en caso contrario. Considere que la la lista enlazada vacía y la lista enlazada de un sólo elemento se encuentran ordenadas. Por ejemplo:

    ```python
    primer_nodo = NodoDoble(elemento="Alfonso", anterior=None, siguiente=None)

    segundo_nodo = NodoDoble(elemento="Francisco", anterior=primer_nodo, siguiente=None)
    primer_nodo.siguiente = segundo_nodo

    tercer_nodo = NodoDoble(elemento="Miguel", anterior=segundo_nodo, siguiente=None)
    segundo_nodo.siguiente = tercer_nodo

    cuarto_nodo = NodoDoble(elemento="Jose", anterior=tercer_nodo, siguiente=None)
    tercer_nodo.siguiente = cuarto_nodo

    lista_enlazada = ListaEnlazadaOrdenada()
    lista_enlazada.cabeza_lista = primer_nodo
    lista_enlazada.final_lista = cuarto_nodo

    lista_enlazada.esta_ordenada() # Debe retornar False.
    ```

* El método `buscar_texto()` recibe como parámetro una cadena de caracteres a buscar, y retorna la posición de esta cadena en la lista enlazada (la posición `0` le corresponde a `cabeza_lista`, y la última posición le corresponde a `final_lista`). En caso la cadena no se encuentre en la lista, retornar el valor de `-1`. Por ejemplo:

    ```python
    lista_enlazada = ListaEnlazadaOrdenada()
    lista_enlazada.agregar("Oliver")
    lista_enlazada.agregar("Paolo")
    lista_enlazada.agregar("Gianluca")
    lista_enlazada.agregar("Christian")
    lista_enlazada.agregar("Pedro")
    lista_enlazada.agregar("Andre")
    lista_enlazada.agregar("Miguel")
    lista_enlazada.agregar("Renato")
    lista_enlazada.agregar("Joao")
    lista_enlazada.agregar("Luis")

    lista_enlazada.buscar_texto("Andre") # Debe retornar 0
    lista_enlazada.buscar_texto("Renato") # Debe retornar 9
    ```

    Asimismo, el método `buscar_texto()` debe estar optimizado de manera que tome ventaja que la lista enlazada se encuentra ordenada.
    En función al orden alfabético, para algunos valores es conveniente empezar la búsqueda desde `cabeza_lista`, y para otros es más probable encontrar un elemento si empezamos a buscar desde `final_lista`.

    ## Segundo Problema (7 puntos)

    En el archivo `laboratorio.py`, complete la implementación de la clase `ValidadorHtml`, utilizada para validar cadenas de caracteres que representan [documentos HTML](https://developer.mozilla.org/es/docs/Learn/Getting_started_with_the_web/HTML_basics).
    Considere lo siguiente en su implementación:

    * El método `validar()` recibe como parámetro una cadena de caracteres, y retorna `True` si se trata de un documento HTML válido y `False` en caso contrario. En un documento HTML, las partes del texto están delimitadas mediante **etiquetas HTML**. Las etiquetas HTML vienen en pares: una etiqueta de entrada de la forma `<NOMBRE-ETIQUETA>` y una etiqueta de salida de la forma `</NOMBRE-ETIQUETA>`. Por ejemplo:

        ```python
        validador = ValidadorHtml()
        codigo_html = """
            <body>
                <center>
                    <h1>Examen Sustitutorio</h1>
                </center>
                <p>
                    Programacion Dinamica
                </p>
            </body>
        """

        validador.validar(codigo_html) # Debe retornar True
        ```
        Nótese que la etiqueta de entrada `<body>` tiene una correspondiente etiqueta de salida `</body>`. 
        En el ejemplo anterior, hemos utilizado también las etiquetas `<center></center>`, `<h1></h1>`, y `<p></p>`. Por el contrario, en el siguiente ejemplo:

        ```python
        validador = ValidadorHtml()
        codigo_html = """
            <body>
                <center>
                    <h1>Examen Sustitutorio</h1>
                </centro>
                <p>
                    Programacion Dinamica
                </p>
            </body>
        """

        validador.validar(codigo_html) # Debe retornar False
        ```

        Nótese que la etiqueta de entrada `<center>` no tiene la correspondiente etiqueta de cierre `</center>`.

    * El método `validar()` debe asegurarse que las etiquetas HTML inicien con `<` y terminen con `>`. Por ejemplo:

        ```python
        validador = ValidadorHtml()
        codigo_html = """
            <body>
                <center>
                    <h1>Examen Sustitutorio</h1>
                </center>
                <p>
                    Programacion Dinamica
                </p>
            </body
        """

        validador.validar(codigo_html) # Debe retornar False
        ```

        Nótese que la etiqueta de cierre para `<body>` está incompleta.

    * Asimismo, considere que el estándar HTML permite definir atributos opcionales, que forman parte de la etiqueta de entrada. Una etiqueta de entrada con atributos opcionales tiene la forma `<NOMBRE-ETIQUETA NOMBRE-ATRIBUTO-1="VALOR-ATRIBUTO-1" NOMBRE-ATRIBUTO-2="VALOR-ATRIBUTO-2" >`. Por ejemplo:

        ```python
        validador = ValidadorHtml()
        codigo_html = """
            <body bgcolor="yellow">
                <center>
                    <h1 id="primary-navigation">Examen Sustitutorio</h1>
                </center>
                <p id="content" align="center">
                    Programacion Dinamica
                </p>
            </body>
        """

        validador.validar(codigo_html) # Debe retornar True
        ```

        La variable `codigo_html` hace referencia a un documento HTML válido.

## Tercer Problema (7 puntos)

En el archivo `laboratorio.py`, complete la implementación de la clase `PilaDoble`, que representa al tipo abstracto de datos "Pila Doble".
Una pila doble consiste en dos pilas internas, una primaria y una secundaria, y ofrece funcionalidad para interactuar con ambas pilas.
La implementación de las operaciones de `apilar()` y `desapilar()` **debe ser eficiente**: deben tomar un número constante de instrucciones, independientemente del número de elementos en la pila.
Considere lo siguiente en su implementación:

* El constructor de `PilaDoble` tiene como parámetro `capacidad_pila`, que representa la capacidad máxima de cada una una de las pilas internas (la pila primaria y la pila secundaria). 
Los elementos de ambas pilas deben almacenarse en el campo `elementos`, que contiene una lista de longitud `2 * capacidad_pila` de modo que tenga espacio para los elementos de ambas pilas internas.
**El campo `elementos` ya se encuentra disponible,  y no está permitido modificar su longitud**, haciendo uso de métodos como `pop()` o `append()`. 
Para ingresar elementos en ambas pilas, limítese a asignarlos mediante índices (`self.elementos[indice] = elemento_a_ingresar`).

* El método `apilar()` agrega elementos a la pila, y tiene dos parámetros: 1) el parámetro `elemento` contiene el valor a apilar, y 2) el parámetro `pila_secundaria` es un booleano que indica apilar en la pila secundaria (cuando su valor es `True`) o en la pila primaria (cuando su valor es `False`). Si se intenta apilar rebasando la capacidad de la pila, se debe lanzar una excepción `ErrorEnPila`. Por ejemplo:

    ```python
    pila_doble = PilaDoble(capacidad_pila=2)

    pila_doble.apilar(pila_secundaria=True, elemento=100)
    pila_doble.apilar(pila_secundaria=True, elemento=200)

    pila_doble.apilar(pila_secundaria=False, elemento=30)
    pila_doble.apilar(pila_secundaria=False, elemento=40)

    pila_doble.apilar(pila_secundaria=True, elemento=300) # Debe lanzar ErrorEnPila
    ```

    Nótese que en el ejemplo, tanto la pila primaria como la secundaria tienen una capacidad de `2` elementos, por lo que no es posible agregar más valores. La pila primaria contiene `30` y `40` (la cima), mientras que la pila secundaria contiene `100` y `200` (la cima).

* El método `desapilar()` remueve y retorna elementos de la pila, y tiene como parámetro el booleano `pila_secundaria`. Cuando `pila_secundaria` es `True`, se debe desapilar de la pila secundaria, y cuando es `False` de la pila primaria.
En caso se intente desapilar de una pila vacía se debe lanzar una excepción `ErrorEnPila`. Por ejemplo:

    ```python
    pila_doble = PilaDoble(capacidad_pila=2)

    pila_doble.apilar(pila_secundaria=True, elemento=100)
    pila_doble.apilar(pila_secundaria=True, elemento=200)

    pila_doble.apilar(pila_secundaria=False, elemento=30)
    pila_doble.apilar(pila_secundaria=False, elemento=40)

    elemento_desapilado = pila_doble.desapilar(pila_secundaria=True) # Debe retornar el valor de 200
    elemento_desapilado = pila_doble.desapilar(pila_secundaria=True) # Debe retornar el valor de 100
    elemento_desapilado = pila_doble.desapilar(pila_secundaria=True) # Debe lanzar ErrorEnPila
    ```

* El método `esta_vacia()` tiene como parámetro el booleano `pila_secundaria`. En caso `pila_secundaria` sea `True`, el método debe retornar `True` si la pila secundaria está vacía, y `False` en caso contrario. En caso `pila_secundaria` sea `False` el método debe retornar `True` si la pila primaria está vacía, y `False` en caso contrario. Por ejemplo:

    ```python
    pila_doble = PilaDoble(capacidad_pila=4)

    pila_doble.esta_vacia(pila_secundaria=False) # Debe retornar True
    pila_doble.esta_vacia(pila_secundaria=True) # Debe retornar True

    pila_doble.apilar(pila_secundaria=False, elemento=10)
    pila_doble.esta_vacia(pila_secundaria=False) # Debe retornar False
    ```

* El método `esta_llena()` tiene como parámetro el booleano `pila_secundaria`. En caso `pila_secundaria` sea `True`, el método debe retornar `True` si la pila secundaria está llena, y `False` en caso contrario. En caso `pila_secundaria` sea `False` el método debe retornar `True` si la pila primaria está llena, y `False` en caso contrario. Por ejemplo:

    ```python
    pila_doble = PilaDoble(capacidad_pila=4)

    pila_doble.esta_llena(pila_secundaria=False) # Debe retornar False
    pila_doble.esta_llena(pila_secundaria=True) # Debe retornar False

    pila_doble.apilar(pila_secundaria=False, elemento=10)
    pila_doble.apilar(pila_secundaria=False, elemento=20)
    pila_doble.apilar(pila_secundaria=False, elemento=30)
    pila_doble.apilar(pila_secundaria=False, elemento=40)

    pila_doble.esta_llena(pila_secundaria=False) # Debe retornar True
