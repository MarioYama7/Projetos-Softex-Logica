# calculadora com opção de sair

n1 = int(input('Digite o rimeiro valor: '))
n2 = int(input('DIgite o segundo valor:  '))
opção = 0
while opção != 6:
    print('Escolha uma das opções:')
    print('''             [1] Somar
             [2] Subtração
             [3] Multiplicação
             [4] Divisão
             [5] Novos valores
             [6] Sair do programa''')
    opção = int(input('Qual a sua escolha?'))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        subtracao = n1 - n2
        print('A subtração de {} - {} é {}'.format(n1, n2, subtracao))
    elif opção == 3:
        multiplicação = n1 * n2
        print('A multiplicação de {} * {} é {}'.format(n1, n2, multiplicação))
    elif opção == 4:
        divisao = n1 / n2
        print('A divisão de {} / {} é {}'.format(n1, n2, divisao))
        if n1 == 0 or n2 == 0:
            raise ZeroDivisionError
    elif opção == 5:
        print('Informe os novos números')
        n1 = int(input('Coloque o primeiro número:'))
        n2 = int(input('Coloque o segundo número:'))
    elif opção == 6:
        print('Finalizando...')
    else:
        print('Opção Inválida, tente novamente')
print('Fim do programa! Pode sair.')
