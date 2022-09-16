import random

def jogar():
    print("**********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("**********************************")

    numSecret =  random.randrange(1, 101)
    tot = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        tot = 20
    elif(nivel ==2):
        tot = 10
    else:
        tot = 5

    for rodada in range(1, tot +1):
        print("Tentativa {} de {}\n". format(rodada, tot))
        chute = int(input("Digite o seu número entre 1 e 100: "))

        if(chute < 1 or chute > 100):
            print("Número inválido!")
            continue

        acertou = (chute == numSecret)
        maior   = chute > numSecret
        menor   = chute < numSecret

        if (acertou):
            print("Você acertou e fez {}".format(pontos))
            break
        else:
            if(maior):
                print("\nVocê errou! O seu chute foi maior que o numero secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor que o numero secreto.")
            pontos_perdidos = abs(numSecret - chute)
            pontos = pontos - pontos_perdidos

    print("\nFim do jogo!")

if(__name__ == "__main__"):
    jogar()