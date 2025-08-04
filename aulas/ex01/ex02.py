class Nodo:
    def __init__(self, valor=0):
        self.valor = valor
        self.prox = None

class ListaSimples:
    def __init__(self):
        self.pri = None
        self.ult = None

    def AddFinal(self, valor):
        novo_nodo = Nodo(valor)

        if self.pri is None:
            self.pri = novo_nodo
            self.ult = novo_nodo
        else:
            self.ult.prox = novo_nodo
            self.ult = novo_nodo

    def AddInicio(self, valor):
        novo_nodo = Nodo(valor)

        if self.pri is None:
            self.pri = novo_nodo
            self.ult = novo_nodo
        else:
            novo_nodo.prox = self.pri
            self.pri = novo_nodo

    def AddApos(self, novo_valor, valor_busca):
        novo_nodo = Nodo(novo_valor)
        nA = self.pri

        while nA is not None:
            if nA.valor == valor_busca:
                novo_nodo.prox = nA.prox
                nA.prox = novo_nodo
                if novo_nodo.prox is None:
                    self.ult = novo_nodo
                return
            nA = nA.prox

        print("Valor não encontrado!")

    def imprimir(self):
        nA = self.pri
        while nA is not None:
            print(nA.valor)
            nA = nA.prox
