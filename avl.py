from abb import ABB

class AVL(ABB):

    def altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def balance(self, nodo):
        if not nodo:
            return 0
        return self.altura(nodo.izquierda) - self.altura(nodo.derecha)

    def rotar_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha

        x.derecha = y
        y.izquierda = T2

        y.altura = 1 + max(self.altura(y.izquierda), self.altura(y.derecha))
        x.altura = 1 + max(self.altura(x.izquierda), self.altura(x.derecha))

        return x

    def rotar_izquierda(self, x):
        y = x.derecha
        T2 = y.izquierda

        y.izquierda = x
        x.derecha = T2

        x.altura = 1 + max(self.altura(x.izquierda), self.altura(x.derecha))
        y.altura = 1 + max(self.altura(y.izquierda), self.altura(y.derecha))

        return y

    def insertar(self, raiz, valor):
        raiz = super().insertar(raiz, valor)

        raiz.altura = 1 + max(self.altura(raiz.izquierda), self.altura(raiz.derecha))
        balance = self.balance(raiz)

        if balance > 1 and valor < raiz.izquierda.valor:
            return self.rotar_derecha(raiz)
        if balance < -1 and valor > raiz.derecha.valor:
            return self.rotar_izquierda(raiz)
        if balance > 1 and valor > raiz.izquierda.valor:
            raiz.izquierda = self.rotar_izquierda(raiz.izquierda)
            return self.rotar_derecha(raiz)
        if balance < -1 and valor < raiz.derecha.valor:
            raiz.derecha = self.rotar_derecha(raiz.derecha)
            return self.rotar_izquierda(raiz)

        return raiz

    def eliminar(self, raiz, valor):
        raiz = super().eliminar(raiz, valor)

        if not raiz:
            return raiz

        raiz.altura = 1 + max(self.altura(raiz.izquierda), self.altura(raiz.derecha))
        balance = self.balance(raiz)

        if balance > 1 and self.balance(raiz.izquierda) >= 0:
            return self.rotar_derecha(raiz)
        if balance > 1 and self.balance(raiz.izquierda) < 0:
            raiz.izquierda = self.rotar_izquierda(raiz.izquierda)
            return self.rotar_derecha(raiz)
        if balance < -1 and self.balance(raiz.derecha) <= 0:
            return self.rotar_izquierda(raiz)
        if balance < -1 and self.balance(raiz.derecha) > 0:
            raiz.derecha = self.rotar_derecha(raiz.derecha)
            return self.rotar_izquierda(raiz)

        return raiz
