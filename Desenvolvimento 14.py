
rodas = int(input('Quantas rodas tem o veículo?'))
peso = float(input('Qual o peso do veiculo?'))
capacidade_pessoas = int(input('Qual a capacidade de pessoas?'))

if rodas == 2 or rodas ==3 :
    print ('O veículo é categoria A')

elif rodas == 4 and peso <= 3500 and capacidade_pessoas <=8 :
    print('O veículo é categoria B')

elif rodas >= 4 and capacidade_pessoas >8 :
    print('O veículo é de classe D')

elif rodas >=4 and peso > 6000 :
    print ('O veículo é de classe E')

elif rodas >= 4 and (peso >= 3500 <= 6000) :
    print('O veículo é de classe C')

else :
    print('Veículo não é de nenhuma categoria')








