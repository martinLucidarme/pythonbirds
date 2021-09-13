class Pessoa:
    olhos = 2 # atributo default/de Classe geralmente algo médio ou igual pra todos os objetos da classe
              # nao aparece no __dict__

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
    del luciano.filhos #funciona para atributo de objeto, nao de classe
    Pessoa.olhos = 8 #transforma o valor para todos os objetos da classe
    print(luciano.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos)
    clayton.olhos=5 #faz olho aparecer no dict do Clayton
    print(clayton.olhos)
    print(clayton.__dict__)
