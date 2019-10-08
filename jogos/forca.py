import random

MENSAGEM_INICIAL = "Bem vindo ao jogo de forca!"
LIMITE_ERROS = 7


def jogar():
    imprime_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_palavra_secreta(palavra_secreta)

    enforcou: bool = False
    acertou = False
    erros = 0

    while (not enforcou) and (not acertou):
        print(letras_acertadas)
        chute = pede_chute()
        if (chute in palavra_secreta):
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)
            print("Errou! faltam", str(LIMITE_ERROS - erros), "tentativas")
        enforcou = erros >= LIMITE_ERROS
        acertou = '_' not in letras_acertadas
        if (enforcou):
            break
    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()


def imprime_abertura():
    print(len(MENSAGEM_INICIAL) * "*")
    print(MENSAGEM_INICIAL)
    print(len(MENSAGEM_INICIAL) * "*")
    pass


def carrega_palavra_secreta(nome_arquivo="palavras.txt"):
    palavras = []
    with open(nome_arquivo) as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())
    print(palavras)
    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()
    return palavra_secreta


def inicializa_palavra_secreta(palavra_secreta):
    return ['_' for letra in palavra_secreta]


def pede_chute():
    chute = ""
    while len(chute) != 1:
        chute = input("digite uma letra: ").upper().strip()
    return chute


def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    for index in range(len(palavra_secreta)):
        if palavra_secreta[index] == chute:
            letras_acertadas[index] = chute.upper()


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor():
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()
