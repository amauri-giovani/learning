class Conta:
    def __init__(self, numero: int):
        self.numero = numero
        self._saldo = 0

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def get_saldo(self):
        return self._saldo

