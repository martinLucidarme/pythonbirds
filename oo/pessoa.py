class Pessoa:
    def __init__(self, *filhos, nome= None, idade=25):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'olá {id(self)}'


if __name__ == '__main__':
    clayton = Pessoa(nome='Zé')
    luciano = Pessoa(clayton, nome='Martin')
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome= 'Ruella'
    print(luciano.sobrenome)
    print(luciano.__dict__)
    print(clayton.__dict__)
    del luciano.filhos
    print(luciano.__dict__)
