import pytest
from laboratorio import (
    ListaEnlazadaOrdenada,
    NodoDoble,
    ValidadorHtml,
    PilaDoble,
    ErrorEnPila,
)


def test_p1_insertar_orden_siguiente():
    lista_enlazada = ListaEnlazadaOrdenada()

    lista_enlazada.agregar("Miguel")
    lista_enlazada.agregar("Francisco")

    lista_enlazada.agregar("Alfonso")

    lista_enlazada.agregar("Jose")

    elementos = []
    nodo_actual = lista_enlazada.cabeza_lista
    for _ in range(4):
        elementos.append(nodo_actual.elemento)
        nodo_actual = nodo_actual.siguiente

    assert elementos == ["Alfonso", "Francisco", "Jose", "Miguel"]
    assert lista_enlazada.esta_ordenada()


def test_p1_insertar_orden_anterior():
    lista_enlazada = ListaEnlazadaOrdenada()

    lista_enlazada.agregar("Miguel")
    lista_enlazada.agregar("Francisco")
    lista_enlazada.agregar("Alfonso")
    lista_enlazada.agregar("Jose")

    elementos = []
    nodo_actual = lista_enlazada.final_lista
    for _ in range(4):
        elementos.append(nodo_actual.elemento)
        nodo_actual = nodo_actual.anterior

    assert elementos == ["Miguel", "Jose", "Francisco", "Alfonso"]
    assert lista_enlazada.esta_ordenada()


def test_p1_lista_esta_ordenada():
    primer_nodo = NodoDoble(elemento="Alfonso", anterior=None, siguiente=None)

    segundo_nodo = NodoDoble(elemento="Francisco", anterior=primer_nodo, siguiente=None)
    primer_nodo.siguiente = segundo_nodo

    tercer_nodo = NodoDoble(elemento="Jose", anterior=segundo_nodo, siguiente=None)
    segundo_nodo.siguiente = tercer_nodo

    cuarto_nodo = NodoDoble(elemento="Miguel", anterior=tercer_nodo, siguiente=None)
    tercer_nodo.siguiente = cuarto_nodo

    lista_enlazada = ListaEnlazadaOrdenada()
    lista_enlazada.cabeza_lista = primer_nodo
    lista_enlazada.final_lista = cuarto_nodo

    assert lista_enlazada.esta_ordenada() is not None
    assert lista_enlazada.esta_ordenada()


def test_p1_lista_desordenada():
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

    assert lista_enlazada.esta_ordenada() is not None
    assert not lista_enlazada.esta_ordenada()


def test_p1_lista_vacia_esta_ordenada():
    lista_enlazada = ListaEnlazadaOrdenada()
    assert lista_enlazada.esta_ordenada()


def test_p1_lista_unitaria_esta_ordenada():
    lista_enlazada = ListaEnlazadaOrdenada()
    lista_enlazada.agregar("Miguel")
    assert lista_enlazada.esta_ordenada()


def test_p1_buscar_nombres():
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

    assert lista_enlazada.esta_ordenada()
    assert lista_enlazada.buscar_texto("Andre") == 0
    assert lista_enlazada.buscar_texto("Renato") == 9
    assert lista_enlazada.buscar_texto("Piero") == -1


def test_p1_busqueda_eficiente():
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

    assert lista_enlazada.esta_ordenada()

    lista_enlazada._reiniciar_lecturas()
    assert lista_enlazada.buscar_texto("Andre") == 0
    assert lista_enlazada._contar_lecturas() == 1

    lista_enlazada._reiniciar_lecturas()
    assert lista_enlazada.buscar_texto("Paolo") == 7
    assert lista_enlazada._contar_lecturas() == 3

    lista_enlazada._reiniciar_lecturas()
    assert lista_enlazada.buscar_texto("Renato") == 9
    assert lista_enlazada._contar_lecturas() == 1


def test_p2_procesar_html_valido():
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

    assert validador.validar(codigo_html)


def test_p2_etiqueta_sin_cerrar():
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

    assert validador.validar(codigo_html) is not None
    assert not validador.validar(codigo_html)


def test_p2_etiqueta_cierre_sin_par():
    validador = ValidadorHtml()
    codigo_html = """
        </body>
            <center>
                <h1>Examen Sustitutorio</h1>
            </center>
            <p>
                Programacion Dinamica
            </p>
        </body>
    """

    assert validador.validar(codigo_html) is not None
    assert not validador.validar(codigo_html)


def test_p2_etiqueta_equivocada():
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
    assert validador.validar(codigo_html) is not None
    assert not validador.validar(codigo_html)


def test_p2_procesar_etiquetas_con_atributos():
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

    assert validador.validar(codigo_html)


def test_p3_pila_recien_creada():
    pila_doble = PilaDoble(capacidad_pila=4)
    with pytest.raises(Exception):
        pila_doble.elementos = []

    assert pila_doble.esta_vacia(pila_secundaria=False)
    assert pila_doble.esta_vacia(pila_secundaria=True)
    assert not pila_doble.esta_llena(pila_secundaria=False)
    assert not pila_doble.esta_llena(pila_secundaria=True)

    with pytest.raises(AssertionError):
        pila_doble.elementos.append(10)
        pila_doble.esta_llena(pila_secundaria=False)


def test_p3_usar_pila_primaria():
    pila_doble = PilaDoble(capacidad_pila=4)

    pila_doble.apilar(pila_secundaria=False, elemento=10)
    assert not pila_doble.esta_vacia(pila_secundaria=False)

    pila_doble.apilar(pila_secundaria=False, elemento=20)
    pila_doble.apilar(pila_secundaria=False, elemento=30)
    pila_doble.apilar(pila_secundaria=False, elemento=40)

    assert pila_doble.esta_llena(pila_secundaria=False)
    assert pila_doble.esta_vacia(pila_secundaria=True)
    assert not pila_doble.esta_llena(pila_secundaria=True)

    with pytest.raises(ErrorEnPila):
        pila_doble.apilar(pila_secundaria=False, elemento=50)

    assert pila_doble.desapilar(pila_secundaria=False) == 40
    assert not pila_doble.esta_llena(pila_secundaria=False)

    assert pila_doble.desapilar(pila_secundaria=False) == 30
    assert pila_doble.desapilar(pila_secundaria=False) == 20
    assert pila_doble.desapilar(pila_secundaria=False) == 10

    assert pila_doble.esta_vacia(pila_secundaria=False)

    with pytest.raises(ErrorEnPila):
        pila_doble.desapilar(pila_secundaria=False)


def test_p3_usar_pila_secundaria():
    pila_doble = PilaDoble(capacidad_pila=4)

    pila_doble.apilar(pila_secundaria=True, elemento=100)
    assert not pila_doble.esta_vacia(pila_secundaria=True)

    pila_doble.apilar(pila_secundaria=True, elemento=200)
    pila_doble.apilar(pila_secundaria=True, elemento=300)
    pila_doble.apilar(pila_secundaria=True, elemento=400)

    assert pila_doble.esta_llena(pila_secundaria=True)
    assert pila_doble.esta_vacia(pila_secundaria=False)
    assert not pila_doble.esta_llena(pila_secundaria=False)

    with pytest.raises(ErrorEnPila):
        pila_doble.apilar(pila_secundaria=True, elemento=500)

    assert pila_doble.desapilar(pila_secundaria=True) == 400
    assert not pila_doble.esta_llena(pila_secundaria=True)

    assert pila_doble.desapilar(pila_secundaria=True) == 300
    assert pila_doble.desapilar(pila_secundaria=True) == 200
    assert pila_doble.desapilar(pila_secundaria=True) == 100

    assert pila_doble.esta_vacia(pila_secundaria=True)

    with pytest.raises(ErrorEnPila):
        pila_doble.desapilar(pila_secundaria=True)


def test_p3_usar_ambas_pilas():
    pila_doble = PilaDoble(capacidad_pila=2)

    pila_doble.apilar(pila_secundaria=True, elemento=100)

    pila_doble.apilar(pila_secundaria=True, elemento=200)
    pila_doble.apilar(pila_secundaria=False, elemento=30)
    pila_doble.apilar(pila_secundaria=False, elemento=40)

    assert pila_doble.esta_llena(pila_secundaria=True)
    assert pila_doble.esta_llena(pila_secundaria=False)

    with pytest.raises(ErrorEnPila):
        pila_doble.apilar(pila_secundaria=True, elemento=300)
    with pytest.raises(ErrorEnPila):
        pila_doble.apilar(pila_secundaria=False, elemento=50)

    assert pila_doble.desapilar(pila_secundaria=True) == 200
    assert pila_doble.desapilar(pila_secundaria=True) == 100
    assert pila_doble.desapilar(pila_secundaria=False) == 40
    assert pila_doble.desapilar(pila_secundaria=False) == 30

    with pytest.raises(ErrorEnPila):
        pila_doble.desapilar(pila_secundaria=True)
    with pytest.raises(ErrorEnPila):
        pila_doble.desapilar(pila_secundaria=False)
