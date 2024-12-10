class GMBase:
    def __init__(self, modelo, cor, motor):
        self.modelo = modelo
        self.cor = cor
        self.motor = motor

    def __repr__(self):
        return f'<{self.modelo} - {self.cor} - {self.motor}>'

    def __str__(self):
        return self.modelo


class Popular(GMBase):
    def velocidade_maxima(self):
        return '140 Km/h'
