# Anos em 2022 comparado a data de nascimento

nome = input('Digite seu nome completo: ')

scape = True

while scape:
    try:
        ano = int(input('Digite seu ano de nascimento: '))
        if ano >= 1922 and ano <= 2021:
            idade = 2022 - ano
            print('O(A) {} está fará {} anos em 2022'.format(nome, idade))
        else:
            raise
    except Exception:
        print('Ano de nascimento inválido, tente novamente')
    else:
        scape = False
