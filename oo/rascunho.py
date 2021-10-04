NORTE = 'Norte'
LESTE = 'Leste'
OESTE = 'Oeste'
SUL = 'Sul'

class Motor:

    def __init__(self):
            self.velocidade= 0

    def acelerar(self):
            self.velocidade += 1

    def frear(self):
            self.velocidade -= 2
            self.velocidade = max(0, self.velocidade) # avoids if/else"

class Direcao:


    rotacao_a_direita_dct = {NORTE:LESTE, LESTE:SUL, SUL:OESTE, OESTE:NORTE} #big elif: probably possible to use dict"
    rotacao_a_esquerda_dct = {NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL}

    def __init__(self):
        self.valor = NORTE

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]

class Carro:
    def __init__(self,direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        return self.motor.acelerar()
    def frear(self):
        return self.motor.frear()

    def calcular_a_direcao(self):
        return self.direcao.valor
    def girar_a_direita(self):
        return self.direcao.girar_a_direita()
    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()


if __name__ == '__main__':

    motor = Motor()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)

    direcao= Direcao()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)

    direcao = Direcao()
    motor = Motor()
    carro = Carro(direcao, motor)
    print(carro.calcular_velocidade())
    carro.acelerar()
    print(carro.calcular_velocidade())
    carro.acelerar()
    print(carro.calcular_velocidade())
    carro.frear()
    print(carro.calcular_a_direcao())
    carro.girar_a_direita()
    print(carro.calcular_a_direcao())
    carro.girar_a_esquerda()
    print(carro.calcular_a_direcao())
    carro.girar_a_esquerda()