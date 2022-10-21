class Pessoa ():
    def __init__(self, nome=None, altura=None, peso=None):
        self.nome = nome
        self.altura = altura
        self.peso = peso
    
    def getIMC (self):
        return self.peso / (self.altura * self.altura)