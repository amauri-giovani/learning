class Grafo:
    def __init__(self, numero_vertices):
        """
        Cria uma quantidade delistas conforme o numero_vertices passado
        E = arestas. Quando se cria o Grafo não existem arestas e por isso E = 0.
        """
        self.adj = [[] for i in range(numero_vertices)]
        self.V = numero_vertices
        self.E = 0

    def adiciona_aresta(self, vertice1, vertice2):
        """
        Torna vizinhos no grafo os vértices 1 e 2
        vértice 2 entra na lista de vizinhos do 1
        vértice 1 entra na lista de vizinhos do 2
        Como os vértices 1 e 2 se tornaram vizinhos, formou-se uma aresta, E += 1
        """
        self.adj[vertice1].append(vertice2)
        self.adj[vertice2].append(vertice1)
        self.E += 1

    def vizinhos(self, v):
        """Retorna a lista de todos os vizinhos de um determinado vértice"""
        return self.adj[v]

# Adicionando arestas
G = Grafo(3)
G.adiciona_aresta(0, 1)
G.adiciona_aresta(0, 2)
"""
O Grafo ficará assim: 3 vértices e 2 arestas:
(0) --- (1)
 |
 |
(2)
"""
print(f"G tem {G.V} vértices e {G.E} arestas")


# Outro exemplo
"""
Vamos criar um Grafo com 7 vértices e 7 arestas conforme abaixo:

(0)---(1)---(4)---(5)
 |     |           |
(2)---(3)         (6)
"""
H = Grafo(7)
H.adiciona_aresta(0, 1)
H.adiciona_aresta(0, 2)
H.adiciona_aresta(1, 4)
H.adiciona_aresta(1, 3)
H.adiciona_aresta(3, 2)
H.adiciona_aresta(4, 5)
H.adiciona_aresta(5, 6)
print(f"H tem {H.V} vértices e {H.E} arestas")
print(f"No Grafo H, os vizinhos do vértice 1 são: {H.vizinhos(1)}")
print("Vizinhos do vértice 3 no Grafo H:")
for vertice in H.vizinhos(3):
    print(vertice)
