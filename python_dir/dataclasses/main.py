"""
A dataclass é poderosa e parametrizável

@dataclass
ou
@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)

Com dataclass já temos:
__init__    para inicializar o objeto
__eq__      para fazer uma comparação entre objetos
__repr__    para representar a classe

Temos como inicializar algo depois de construir o objeto com :
__post_init__

Temos como setar os atributos na declaração do decorator:
@dataclass

Como customizar:
init=False      se quisermos que a classe não inicie
repr=False      se não quisermos a representação da classe
eq=False        se não quisermos a comparação
frozen=False    se não quisermos que seja mutávél

Se inicializarmos a classe com frozen=True, o __post_init__ dará um erro porque
não conseguirá inicializá-lo, já que a classe já foi construída

Com o field podemos setar cada atributo
lazy load                   para acontecer depois
valor padrão                com um default
fazer um factory do vazio   chamando qualquer função que possa ser executada sem nenhum argumento
repr?                       representar ou não o atributo na classe

default_factory             Se não passar nada, será um objeto com o valor padrão, diferente de None.
                            Isso pode ser qualquer função externa

Precisamos usar a tipagem (Typing)

Podemos converter o objeto em dict com asdict ou tuple com astuple
Exemplo no código

OU VICE-VERSA
Exemplo:
data = {"nome": "Clarice", "sobrenome": "Kappes", "ddd": 13}
clarice = Pessoa2(**data)
clarice
Pessoa2(nome='Clarice', sobrenome='Kappes', telefone={}, nome_completo='Clarice Kappes')
"""
from dataclasses import dataclass, field, asdict, astuple


@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    ddd: int
    telefone: dict[str, str]
    nome_completo: str

    def __post_init__(self):
        self.nome_completo = f"{self.nome} {self.sobrenome}"


# Precisamos passar todos os campos porque não existem um default como na classe Pessoa2 abaixo
# amauri = Pessoa("Amauri", "Giovani", 13)
# TypeError: Pessoa.__init__() missing 2 required positional arguments: 'telefone' and 'nome_completo'

@dataclass
class Pessoa2:
    nome: str
    sobrenome: str
    ddd: int = field(repr=False)                                # não será representado na classe
    telefone: dict[str, str] = field(default_factory=dict)      # default dict = {}, pode ser função externa
    nome_completo: str = field(init=False)                      # torna mutável

    def __post_init__(self):
        self.nome_completo = f"{self.nome} {self.sobrenome}"


# amauri = Pessoa("Amauri", "Giovani", 13)
# amauri
# Pessoa(nome='Amauri', sobrenome='Giovani', telefone={}, nome_completo='Amauri Giovani')

# amauri.telefone |= {'movel': '99128-4678'}
# amauri
# Pessoa(nome='Amauri', sobrenome='Giovani', telefone={'movel': '99128-4678'}, nome_completo='Amauri Giovani')

# asdict(amauri)
# {
#     'nome': 'Amauri',
#     'sobrenome': 'Giovani',
#     'ddd': 13,
#     'telefone': {
#         'movel': '99128-4678'
#     },
#     'nome_completo': 'Amauri Giovani'
# }

# astuple(amauri)
# ('Amauri', 'Giovani', 13, {'movel': '99128-4678'}, 'Amauri Giovani')
