class nodo:
    valor = 0
    prox = nonc

class LISTA_SIMPLES
    pri = None
    ult = None

    def AddFinal(self, valor):
        NovoNodo = Nodo()
        NovoNodo.valor = valor

        if self.pri is None and self.ult is None:
            self.pri = NovoNodo
            self.ult = NovoNodo
        else:
            self.ult.prox = NovoNodo
            self.ult = NovoNodo

    def print(self):
        nA = self.pri

        while nA is not None:
            print(nA.valor, nA.prox)
            nA = nA.prox

    def AddInicio(self.valor):

        else
            NovoNodo.prox = self.pri
            self.pri = NovoNodo

    def AddApos(self, NovoValor, ValorBusca)

        else:
            nA = self.pri
             
            while nA.prox is not self.ult:
                if nA.valor == valor.busca:
                    NovoNodo.prox = nA.prox
                    nA.paox = NovoNodo
                nA = nA.prox
            self.Add