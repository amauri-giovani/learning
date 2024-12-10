"""
Árvore binária funciona da seguinte maneira:
Cada nó(raiz) pode ter filhos ou não e no máximno dois.
Os filhos menores ficam do lado esquerdo.
Os filhos maiores ficam do lado direito.

No caso da árvore binária, a maioria das operações mais importantes, terão custo proporcional a altura da árvore. Uma
coleção com N elementos pode ser organizada na
forma de uma árvore binária de altura aproximada log(N). Só para se ter uma comparação, o valor de log(N) é muito
menor do que N, por exemplo para N igual a 1000 o valor de log(N) será aproximadamente 10.
Neste caso é bem semelhante, para uma árvore com 1000 elementos em uma árvore binária montada de uma maneira bem
“organizada”, a altura da árvore será 10 aproximadamente. Então o custo de se executar uma busca nessa árvore será no
máximo 10 passos de computação.
Outros exemplos são apresentadas a seguir:
    10 elementos: árvore de altura 4
    20 elementos: árvore de altura 5
    1000 elementos: árvore de altura 10
    2000 elementos: árvore de altura 11
"""


class Arvore:
    def __init__(self, chave, filho_esquerdo=None, filho_direito=None):
        self.chave = chave
        self.fesq = filho_esquerdo
        self.fdir = filho_direito

    def exibe_pre_ordem(self):
        if self.fesq is not None:
            self.fesq.exibe_pre_ordem()
        print(self.chave)
        if self.fdir is not None:
            self.fdir.exibe_pre_ordem()

    def exibr_in_ordem(self):
        print(self.chave)
        if self.fesq is not None:
            self.fesq.exibe_pre_ordem()
        if self.fdir is not None:
            self.fdir.exibe_pre_ordem()


x = Arvore(8, None, Arvore(11))
y = Arvore(7, Arvore(5), x)

print(f'y tem chave {y.chave}')
print(f'y tem filho esquerdo {y.fesq}')
print(f'y tem filho direito {y.fdir}')

print(y.exibe_pre_ordem())
print(y.exibr_in_ordem())

"""
Resposta em formato de árvore:

   7
5     8
         11
"""
