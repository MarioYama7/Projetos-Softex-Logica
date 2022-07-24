import enum


class Politicos(enum.Enum):
    candidato_X = 889
    candidato_Y = 847
    candidato_Z = 515
    branco = 0


def votacao():
    nulos = 0
    l = 0
    b = 0
    a = 0

    while True:
        print("\n\n ----ELEIÇÕES---- \n\n Considere - \n\n - Candidato_X = 889 \n - Candidato_Y = 847 \n - Candidato_Z = 515 \n - nulo = 0 \n")
        votos = input("Digite seu voto: ")

        try:
            numero_votos = int(votos)
            if(numero_votos == Politicos.candidato_X.value):
                l += 1
            elif(numero_votos == Politicos.candidato_Y.value):
                b += 1
            elif(numero_votos == Politicos.candidato_Z.value):
                a += 1
            else:
                nulos += 1

        except ValueError:

            print("Digite um número inteiro.")

            continue
        else:
            question = input("Deseja fazer a contagem de votos? ")

            if(question == "Sim" or question == "sim" or question == "SIM"):
                break
            else:
                continue

    if(l > b and l > a):
        print("Candidato_X venceu!")
    elif(b > l and b > a):
        print("Candidato_Y venceu!")
    elif(a > l and a > b):
        print("Candidato_Z venceu!")

    print("Total de votos: ")
    print("Candidato_X: " + str(l))
    print("Candidato_Y: " + str(b))
    print("Candidato_Z: " + str(a))
    print("Nulos: " + str(nulos))


votacao()
