'''
Criar uma classe carro que possui 2 atributos compostos por
2 outras classes:
1) Motor -> responsa de controlar a velocidade
    atrib: velocidade, metodo acelerar: incrementa velocidade,
método frear: decrementa a velocidade

2)Direção -> responsa de controlar a direção
    atrib: valor de direção com valores possiveis Norte -Sul -Leste-Oeste
    método girar_a_direita
    método girar_a_esquerda
    N
O       L
    S

    Exemplo:
    >>> #testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # testando direção
    >>> direcao= Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste"
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul"
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste"
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte"
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste"
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul"
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste"
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte"
    >>> carro= Carro(direcao, motor)
    >>> carro.calcular_velocidade
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_a_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_a_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_a_direcao()
    'Oeste'



'''

#class Carro(direcao, motor):

class Motor:

    def __init__(self,velocidade=0):
            self.velocidade= velocidade

    def acelerar(self):
            self.velocidade += 1

    def frear(self):
            self.velocidade -= 2
            self.velocidade = max(0, self.velocidade) # avoids if/else"
NORTE = 'Norte'
LESTE = 'Leste'
OESTE = 'Oeste'
SUL = 'Sul'
class Direcao:


    rotacao_a_direita_dct = {NORTE:LESTE, LESTE:SUL, SUL:OESTE, OESTE:NORTE} #big elif: probably possible to use dict"
    rotacao_a_esquerda_dct = {NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL}

    def __init__(self):
        self.valor = NORTE

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]

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
