"""
Modelo da entidade Professor e o que ela faz
"""

class Professor:
    # constructor
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    # atualizar dados
    def atualizar(self, dados):
        try:
            id = dados['id']
            nome = dados['nome']
            self.id, self.nome = id, nome
            return self
        except Exception as e:
            print('Algo deu errado na atualização do professor')
            print(e)

    # método dict - Pega os dados id e nome do professor e devolve em formato de dicionário
    def __dict__(self):
        return {'id': self.id, 'nome': self.nome}

    @staticmethod
    def criar(dados):
        try:
            id = dados['id']
            nome = dados['nome']
            return Professor(id=id, nome=nome)
        except Exception as e:
            print('Algo deu errado na criação do professor')
            print(e)
