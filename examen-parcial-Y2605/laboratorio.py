from typing import Any
import re

class ErrorEnPila(Exception):
    pass


class NodoDoble:
    def __init__(self, elemento, siguiente, anterior):
        self.elemento = elemento
        self.siguiente = siguiente
        self.anterior = anterior

        self.elemento_leido = False

    def __getattribute__(self, nombre_atributo: str) -> Any:
        if nombre_atributo == "elemento":
            self.elemento_leido = True
        return object.__getattribute__(self, nombre_atributo)

    def __str__(self):
        siguiente = self.siguiente.elemento if self.siguiente else None
        anterior = self.anterior.elemento if self.anterior else None
        return f"[Ant:<{anterior}> El:{self.elemento}  Sig:<{siguiente}>] "

    def __repr__(self) -> str:
        return str(self)


class ListaEnlazadaOrdenada:
    def __init__(self):
        self.cabeza_lista = None
        self.final_lista = None
        # [INICIO]: Extienda el constructor entre [INICIO] y [FIN].
        # No edite antes de esta línea.

        pass
        # [FIN]
        
    def largo(self):
        referente=self.cabeza_lista
        num=0
        while referente is not None:
            num+=1
            referente=referente.siguiente
        return num

    def agregar(self, elemento):
        # [INICIO]: Implemente el metodo entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        nuevo_nodo=NodoDoble(elemento,None,None)
        if(self.largo()==0):
            self.cabeza_lista = self.final_lista = nuevo_nodo
        else:
            if (elemento < self.cabeza_lista.elemento):
                nuevo_nodo.siguiente=self.cabeza_lista
                self.cabeza_lista.anterior = nuevo_nodo
                self.cabeza_lista = nuevo_nodo
            elif elemento>self.final_lista.elemento:
                nuevo_nodo.anterior=self.final_lista
                self.final_lista.siguiente = nuevo_nodo
                self.final_lista = nuevo_nodo
            else:
                referente=self.cabeza_lista
                while(referente is not None):
                    if(elemento>referente.elemento):
                        referente=referente.siguiente
                    else:
                        nuevo_nodo.siguiente=referente
                        nuevo_nodo.anterior=referente.anterior
                        referente.anterior.siguiente=nuevo_nodo
                        referente.anterior=nuevo_nodo
                        break
            referente=self.cabeza_lista  
        # [FIN]

    def esta_ordenada(self):
        # [INICIO]: Implemente el metodo entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        if self.largo()==1 or self.largo()==0:
            return True
        else:
            referente=self.cabeza_lista
            while(referente.siguiente is not None):
                if (referente.elemento>referente.siguiente.elemento):
                    return False
                referente=referente.siguiente
            return True
        # [FIN]

    def buscar_texto(self, elemento):
        # [INICIO]: Implemente el metodo entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        referente=self.cabeza_lista
        referente_final=self.final_lista
        if 'a'<=elemento[0].lower()<='m':
            for i in range(self.largo()):
                if (referente.elemento==elemento):
                    return i
                referente=referente.siguiente    
        else:
            for i in range(self.largo()):
                if (referente_final.elemento==elemento):
                    return self.largo()-1-i
                referente_final=referente_final.anterior
        return -1
        # [FIN]

    def _contar_lecturas(self):
        nodo_actual = self.cabeza_lista
        nodos = []
        while nodo_actual is not None:
            nodos.append(nodo_actual)
            nodo_actual = nodo_actual.siguiente

        resultado = sum([1 if nodo.elemento_leido else 0 for nodo in nodos])

        return resultado

    def _reiniciar_lecturas(self):
        nodo_actual = self.cabeza_lista
        while nodo_actual is not None:
            nodo_actual.elemento_leido = False
            nodo_actual = nodo_actual.siguiente

    def __str__(self):
        nodos = []
        nodo_actual = self.cabeza_lista
        while nodo_actual is not None:
            nodos.append(str(nodo_actual))
            nodo_actual = nodo_actual.siguiente

        return "->".join(nodos)

    def __repr__(self) -> str:
        return str(self)


class ValidadorHtml:
    def __init__(self):
        # [INICIO]: Extienda el constructor entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        self.lista=[]
        self.patron=r'<(.*?)>'
        # [FIN]

    def validar(self, codigo_html):
        # [INICIO]: Implemente el metodo entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        caracteres=re.findall(self.patron,codigo_html)
        for caracter in caracteres:
            caracter_formateado=caracter.split(' ')[0]
            if caracter[0]!='/':
                self.lista.append(caracter_formateado)
            else:
                try:
                    self.lista.remove(caracter_formateado[1:])
                except:
                    return False
        return len(self.lista)==0
        # [FIN]


class PilaDoble:
    def __init__(self, capacidad_pila=100):
        self.capacidad_pila = capacidad_pila
        self.elementos = [None for _ in range(2 * capacidad_pila)]
        # [INICIO]: Extienda el constructor entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        self.elementos_pila_secundaria=0
        self.elementos_pila_primaria=0
        # [FIN]

    def apilar(self, pila_secundaria, elemento):
        assert len(self.elementos) == self.capacidad_pila * 2
        # [INICIO]: Implemente el método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        if self.esta_llena(pila_secundaria):
                raise ErrorEnPila()
        if(pila_secundaria):
            self.elementos[self.capacidad_pila+self.elementos_pila_secundaria]=elemento
            self.elementos_pila_secundaria+=1
        else:
            self.elementos[self.elementos_pila_primaria]=elemento
            self.elementos_pila_primaria+=1
        # [FIN]

    def desapilar(self, pila_secundaria):
        assert len(self.elementos) == self.capacidad_pila * 2
        # [INICIO]: Implemente el método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        if self.esta_vacia(pila_secundaria):
                raise ErrorEnPila()
        if(pila_secundaria):
            self.elementos_pila_secundaria-=1
            elemento_desapilado=self.elementos[self.capacidad_pila+self.elementos_pila_secundaria]
            self.elementos[self.capacidad_pila+self.elementos_pila_secundaria]=None
        else:
            self.elementos_pila_primaria-=1
            elemento_desapilado=self.elementos[self.elementos_pila_primaria]
            self.elementos[self.elementos_pila_primaria]=None   
        return elemento_desapilado 
        # [FIN]

    def esta_vacia(self, pila_secundaria):
        assert len(self.elementos) == self.capacidad_pila * 2
        # [INICIO]: Extienda el constructor entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        if(pila_secundaria):
            return self.elementos_pila_secundaria==0
        else:
            return self.elementos_pila_primaria==0
        # [FIN]

    def esta_llena(self, pila_secundaria):
        assert len(self.elementos) == self.capacidad_pila * 2
        # [INICIO]: Extienda el constructor entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        if(pila_secundaria):
            return self.elementos_pila_secundaria==self.capacidad_pila
        else:
            return self.elementos_pila_primaria==self.capacidad_pila
        # [FIN]

    def __setattr__(self, name: str, value: Any) -> None:
        if hasattr(self, "elementos") and name == "elementos":
            raise Exception("No se puede modificar el campo elementos.")
        self.__dict__[name] = value


if __name__ == "__main__":
    # [INICIO]: Pruebe sus soluciones entre [INICIO] y [FIN].
    # No edite antes de esta línea.
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
    print(f"{lista_enlazada.esta_ordenada()=}")

    
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
    print(f"{validador.validar(codigo_html)=}")
    # [FIN]
