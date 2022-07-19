# Calculadora com opções.

print('Escolha dois números para a operação: ')


def calculadora(primeiroNumero, segundoNumero, operacao):

    if operacao == 1:
        return primeiroNumero + segundoNumero
    elif operacao == 2:
        return primeiroNumero - segundoNumero
    elif operacao == 3:
        return primeiroNumero * segundoNumero
    elif operacao == 4:
        if primeiroNumero == 0 or segundoNumero == 0:
            return 'Divisão por zero!\nOperação invalida!'

        else:
            return primeiroNumero / segundoNumero
    else:

        return 0


primeiroNumero = float(input('Escolha o primeiro: '))
segundoNumero = float(input('Escolha o segundo: '))
print('1 = Soma '
      + '2 = Subtração '
      + '3 = multiplicação '
      + '4 = Divisão')
operacao = int(input('Escolha a operação matemática: '))
print(calculadora(primeiroNumero, segundoNumero, operacao))
