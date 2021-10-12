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

class Homem(Pessoa): #exemplo da Herança: Homem herde de todos os atributos de Pessoa
    pass
class Mutante(Pessoa):
    olhos = 3
    pass

if __name__ == '__main__':
    renzo = Mutante(nome='Zé')
    luciano = Homem(renzo, nome='Martin')
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
    #renzo.olhos=5 #faz olho aparecer no dict do Clayton
    print(renzo.olhos)
    print(renzo.__dict__)
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), renzo.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa,Pessoa)) #pessoa é da classe Pessoa ? = True
    print(isinstance(pessoa, Homem)) #pessoa é da classe Homem ? = false
    print(isinstance(renzo, Pessoa))
    print(isinstance(renzo, Homem))
    print(renzo.olhos)

