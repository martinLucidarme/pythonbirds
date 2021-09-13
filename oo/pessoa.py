class Pessoa:
    def __init__(self, nome= None, idade=25):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'olá {id(self)}'

if __name__ == '__main__':
    p=Pessoa('Martin')
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)
    p.nome = 'oloco'
    print(p.nome)


