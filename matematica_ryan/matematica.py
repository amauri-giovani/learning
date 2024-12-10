from random import randint
import logging


filename = 'logs_matematica.log'

logging.basicConfig(
    filename=filename,
    format='%(asctime)s  %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S',
    level=logging.DEBUG
)


class Matematica:
    def __init__(self, nome):
        self.nome = nome
        self.acertos = 0
        self.erros = 0
        self.opcoes = {1: '+', 2: '-', 3: 'x', 4: '/'}

    def verifica(self, correta, resposta):
        if resposta == correta:
            self.acertos += 1
            return "Resposta correta"
        else:
            self.erros += 1
            return f"Não é bem isso. A resposta correta é {correta}"

    def conta(self, tipo, qtde_num):
        inicio = int('1' + ((qtde_num - 1) * '0'))
        fim = int(qtde_num * '9')
        num1 = randint(inicio, fim)
        num2 = randint(inicio, fim)
        num_maior, num_menor = (num1, num2) if num1 >= num2 else (num2, num1)
        correta = 0
        if tipo == '+':
            correta = num_maior + num_menor
        elif tipo == '-':
            correta = num_maior - num_menor
        elif tipo == 'x':
            correta = num_maior * num_menor
        elif tipo == '/':
            correta = num_maior / num_menor
        resposta = int(input(f"\n{num_maior} {tipo} {num_menor} = "))
        mensagem = self.verifica(correta, resposta)
        print(mensagem)

    def menu(self):
        print("\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")
        try:
            operacao = self.opcoes[int(input("Escolha de 1 a 4 para o tipo de operação: "))]
            qtde_numeros = int(input("Quantos algarismos?: "))
            if qtde_numeros > 0:
                while True:
                    self.conta(operacao, qtde_numeros)
        except (ValueError, KeyError, TypeError):
            print("\n***** Precisa ser um número *****")
            self.menu()


sessao = None
try:
    print("Responda as questões abaixo:")
    nome = input("Digite seu nome: ")
    sessao = Matematica(nome)
    sessao.menu()
except KeyboardInterrupt:
    if isinstance(sessao, Matematica):
        print(f"\n\n{sessao.nome} teve:\n{sessao.acertos} acertos\n{sessao.erros} erros")
        logging.info(f"{sessao.nome} teve {sessao.acertos} acertos e {sessao.erros} erros")
    print("\n\n***** Programa finalizado *****\n")


# //TODO COLOCAR TEMPO
# //TODO CRIAR MÓDULO UTILS
