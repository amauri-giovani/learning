def pessoa(nome, idade):
    return nome, idade


pessoa("Amauri", 48)


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def comer(self):
        return "Pessoa comendo"




# pessoa1 = Pessoa("Amauri", 48)
# pessoa1.nome
# pessoa1.idade
# pessoa1.comer()