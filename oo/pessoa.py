class Pessoa:
    olhos = 2 # atributo default/de Classe geralmente algo médio ou igual pra todos os objetos da classe
              # nao aparece no __dict__

    def __init__(self, *filhos, nome= None, idade=25):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'olá {id(self)}'

    @staticmethod #método de classe, atrelado a classe
    def metodo_estatico():
        return '42'
    @classmethod   #utilizado para obter atributos da classe
    def nome_e_atributos_de_classe(cls):
        return f'{cls} tem {cls.olhos} olhos '


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
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), clayton.nome_e_atributos_de_classe())
