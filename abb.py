from nodo import Nodo

class ABB:
    def __init__(self):
        self.raiz = None

    def insertar(self, raiz, valor):
        if not raiz:
            return Nodo(valor)
        elif valor < raiz.valor:
            raiz.izquierda = self.insertar(raiz.izquierda, valor)
        else:
            raiz.derecha = self.insertar(raiz.derecha, valor)
        return raiz

    def buscar(self, raiz, valor):
        if raiz is None or raiz.valor == valor:
            return raiz
        if valor < raiz.valor:
            return self.buscar(raiz.izquierda, valor)
        return self.buscar(raiz.derecha, valor)

    def minimo_valor(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    def eliminar(self, raiz, valor):
        if not raiz:
            return raiz
        elif valor < raiz.valor:
            raiz.izquierda = self.eliminar(raiz.izquierda, valor)
        elif valor > raiz.valor:
            raiz.derecha = self.eliminar(raiz.derecha, valor)
        else:
            if raiz.izquierda is None:
                return raiz.derecha
            elif raiz.derecha is None:
                return raiz.izquierda
            temp = self.minimo_valor(raiz.derecha)
            raiz.valor = temp.valor
            raiz.derecha = self.eliminar(raiz.derecha, temp.valor)
        return raiz
