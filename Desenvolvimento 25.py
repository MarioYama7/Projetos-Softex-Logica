# Utilizando os métodos get e set em peso e altura

class Peso():
    def __init__(self, peso_1):
        self.p = peso_1

    '''Método getter para retornar o valor do atributo peso'''

    def get_peso(self):
        return self.p

    '''Método setter para atribuir novo valo do atributo peso'''

    def set_peso(self, peso_2):
        self.p = peso_2


class Altura():
    def __init__(self, altura_1):
        self.a = altura_1
    '''Método getter para retornar o valor do atributo altura'''

    def get_altura(self):
        return self.a

    '''Método setter para atribuir novo valo do atributo peso'''

    def set_altura(self, altura_2):
        self.a = altura_2


class IMC_1 ():
    Peso / (Altura ** 2)


# Determinar um valor para a classe peso
testepeso = Peso(50)
print('O peso da pessoa é: ', testepeso.get_peso())

# Determinar um valor para a classe altura
testealtura = Altura(1.75)
print('A altura da pessoa é', testealtura.get_altura())

# Novo valor para o peso
novo_testep = int(input('Digite um novo peso: '))
testepeso.set_peso(novo_testep)
print('Valor do peso após atribuição: ', testepeso.get_peso())

# Novo valor para altura
novo_testea = float(input('Digite uma nova altura: '))
testealtura.set_altura(novo_testea)
print('Valor da altura após atribuição: ', testealtura.get_altura())
