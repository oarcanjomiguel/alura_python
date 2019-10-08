import random

def jogar():
    MENSAGEM_INICIAL = "Bem vindo ao jogo de adivinhação!"
    MENSAGEM_OK = "Você acertou!"
    MENSAGEM_NOK = "Você errou!"
    MENSAGEM_MAIOR = MENSAGEM_NOK + " Seu chute foi maior que o número!"
    MENSAGEM_MENOR = MENSAGEM_NOK + " Seu chute foi menor que o número!"
    MENSAGEM_FIM = "Fim de jogo!"

    CHUTE_MAXIMO = 100
    CHUTE_MINIMO = 1
    TENTATIVAS_DIFICULDADE = [20, 10, 5]
    PONTOS_INICIAIS = 1000
    pontos = PONTOS_INICIAIS

    print(len(MENSAGEM_INICIAL)*"*")
    print(MENSAGEM_INICIAL)
    print(len(MENSAGEM_INICIAL)*"*")

    numero_secreto = random.randrange(1,101)
    dificuldade = 0
    while(not (dificuldade in [1,2,3]) ):
        dificuldade = int(input("selecione a dificuldade (1)Fácil, (2)Médio, (3)Difícil: "))
    TENTATIVAS_MAXIMO = TENTATIVAS_DIFICULDADE[dificuldade-1]
    for rodada in range(TENTATIVAS_MAXIMO):
        print("Tentativa {} de {}".format(rodada+1,TENTATIVAS_MAXIMO))
        chute = int(input("Digite um número de {} a {}: ".format(CHUTE_MINIMO, CHUTE_MAXIMO)))
        if(chute < CHUTE_MINIMO or chute > CHUTE_MAXIMO):
            print("Você deve digitar um número entre {} e {}".format(CHUTE_MINIMO, CHUTE_MAXIMO))
            continue
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print(MENSAGEM_OK)
            break
        else:
            if (chute > numero_secreto):
                pontos_perdidos = chute - numero_secreto
            else:
                pontos_perdidos = numero_secreto - chute
            pontos = pontos - pontos_perdidos
            if(maior):
                print(MENSAGEM_MAIOR)
            elif(menor):
                print(MENSAGEM_MENOR)
    print(MENSAGEM_FIM)


if __name__ == "__main__":
    jogar()