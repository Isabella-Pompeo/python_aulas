class Nodo:
    valor = 0
    proximo = None

class Fila:
    pri = None

    def adicionar(self, valor):
        novoNodo = Nodo()
        novoNodo.valor = valor
        if self.pri is None:
            self.pri = novoNodo
        else:
            nodoAtual = self.pri
            while nodoAtual.proximo is not None:
                nodoAtual = nodoAtual.proximo
            nodoAtual.proximo = novoNodo

    def remover(self):
        if self.pri is None:
            print("Fila vazia! nada pra remover")
        elif self.pri.proximo is None:
            self.pri = None
        else:
            self.pri = self.pri.proximo
    
    def print(self):
        nodoAtual = self.pri
        if nodoAtual is None:
            return
        while nodoAtual.proximo is not None:
            print("--------------------------")
            print("End:",nodoAtual)
            print("Valor:",nodoAtual.valor)
            print("Prox:",nodoAtual.proximo)
            print("--------------------------")
            nodoAtual = nodoAtual.proximo
        print("--------------------------")
        print("End:",nodoAtual)
        print("Valor:",nodoAtual.valor)
        print("Prox:",nodoAtual.proximo)
        print("--------------------------")

    def tamanho(self):
    tamanho = 0
    nodoAtual = self.pri
        if nodoAtual is None:
            return
        while nodoAtual.proximo is not None:
            tamanho += 1
            nodoAtual = nodoAtual.proximo
        tamanho += 1
        print("A fila tem ", tamanho,' elementos')  

fila = Fila()
fila.adicionar(1)
fila.adicionar(2)
fila.adicionar(3)
fila.add_prioridade(4)
fila.remover()
fila.print()
fila.tamanho()
 

def trocar(self, i1, i2):

def add_prioridade(self, valor):
    novoNodo.prp

def remover_valor(self, valor):