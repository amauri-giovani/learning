"""
Heap é um tipo especial de árvore binária quefornece uma implementação eficiente de Fila de Prioridades.
O custo das operações de inserção e remoção será O(lg N), isto é, proporcional à altura da árvore.

Heap é uma árvore binária com as seguintes propriedades:
1) A chave (prioridade) dos filhos é sempre menor que a do pai.
2) A árvore sempre estará o mais preenchida possível começando pela esquerda.

Devido à propriedade de que todo pai é maior que os filhos, o maior elemento de todos sempre estará na raiz.
Portanto, acesso ao máximo custa tempo O(1).

        9
    6       3
  4   5   2

"""

"""
Vamos inserir o 8
        9
    6       8
  4   5   2   3

"""

"""
Vamos remover a raiz 9. 
Nesse caso quem assume a raiz é o último número inserido, o 3.
Como normalmente esse número é menor, trocaremos com seus pais 
        3
    6       8
  4   5   2   

"""

# heap = [9, 6, 3, 4, 5, 2]

class Heap:
    def __init__(self):
        self. heap = []

    def pai(self, ind_filho):
        """
        Retorna o índice que é pai de um determinado índice
        Para descobrir o índice pai pegamos o índice do filho subtraindo 1 e dividimos por 2
        """
        return (ind_filho - 1) // 2

    def fesq(self, ind_pai):
        """
        Retorna o índice do filho esquerdo do índice
        Dado o índice do pai, o índice do filho esquerdo é o dobro do pai mais um
        """
        return 2 * ind_pai + 1

    def fdir(self, ind_pai):
        """
        Retorna o índice do filho direito do índice
        Dado o índice do pai, o índice do filho esquerdo é o dobro do pai mais dois
        """
        return 2 * ind_pai + 2

    def maior_filho(self, ind_pai):
        """
        Retorna o índice do maior filho de um elemento
        Como pode existir elemento sem filhos, fazemos uma verificação
        """
        fesq, fdir = self.fesq(ind_pai), self.fdir(ind_pai)
        if fesq >= len(self.heap):
            return None
        elif (fdir >= len(self.heap)) or (self.heap[fesq] > self.heap[fdir]):
            return fesq
        # elif self.heap[fesq] > self.heap[fdir]:
        #     return fesq
        else:
            return fdir

    def troca(self, i, j):
        """
        Recebe dois índices do heap e troca o conteúdo entre os dois
        Troca de posição entre pai e filho
        """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def maximo(self):
        """
        Retorna o maior elemento do heap (sem remover)
        O maior sempre estará no índice zero 'topo da árvore'
        """
        return self.heap[0]

    def insere(self, novo):
        """
        Inserimos um novo elemento no final do heap
        ind_novo pega o índice de novo
        Enquanto o filho não estiver na raiz e for maior que o pai, chamamos troca
        """
        self.heap.append(novo)
        ind_novo = len(self.heap) - 1
        while (ind_novo != 0 and self.heap[self.pai(ind_novo)] < self.heap[ind_novo]):
            self.troca(ind_novo, self.pai(ind_novo))
            ind_novo = self.pai(ind_novo)

    def remove(self):
        removido = self.maximo()
        self.troca(0, len(self.heap) - 1)
        self.heap.pop()
        i = 0
        while self.maior_filho(i) is not None and self.heap[self.maior_filho(i)] > self.heap[i]:
            ind_filho = self.maior_filho(i)
            self.troca(i, ind_filho)
            i = ind_filho

# Podemos testar inserindo uns números e verificando qual é o maior
h = Heap()
h.insere(3)
h.insere(5)
h.insere(9)
h.insere(2)
h.insere(6)
h.insere(4)
print(f"O máximo na árvore é {h.maximo()}")
h.remove()
print(f"O máximo na árvore é {h.maximo()}")
