import adivinhacao
import forca


def jogar():
    MENSAGEM_INICIAL = "Bem vindo à escolha de jogo!"

    print(len(MENSAGEM_INICIAL) * "*")
    print(MENSAGEM_INICIAL)
    print(len(MENSAGEM_INICIAL) * "*")

    jogo = 0
    while not (jogo in [1, 2]):
        jogo = int(input('selecione o jogo (1)Adivinhacao (2)Forca'))
    if jogo == 1:
        adivinhacao.adivinhacao()
    else:
        forca.forca()


if __name__ == "__main__":
    jogar()
