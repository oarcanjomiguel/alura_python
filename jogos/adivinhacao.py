import random

MENSAGEM_INICIAL = 'Bem-vindo ao jogo de Adivinhação'
MENSAGEM_OK = 'Você acertou!'
MENSAGEM_NOK = 'Você errou!'
MENSAGEM_MAIOR = MENSAGEM_NOK + ' O seu chute foi maior!'
MENSAGEM_MENOR = MENSAGEM_NOK + ' O seu chute foi menor!'
MENSAGEM_FINAL = 'Fim de jogo!'
TENTATIVAS_MAXIMO = 3
CHUTE_MAXIMO = 100
CHUTE_MINIMO = 1
PONTUACAO_INICIAL = 1000

numero = random.randint(CHUTE_MINIMO, CHUTE_MAXIMO)

print(len(MENSAGEM_INICIAL)*'*')
print(MENSAGEM_INICIAL)
print(len(MENSAGEM_INICIAL)*'*')

pontuacao = PONTUACAO_INICIAL

for tentativa in range(0,TENTATIVAS_MAXIMO):
    print('Rodada {} de {}'.format(tentativa+1, TENTATIVAS_MAXIMO))
    chute=int(input("Digite um número inteiro entre {} e {}: ".format(CHUTE_MINIMO, CHUTE_MAXIMO)))
    if(chute < CHUTE_MINIMO or chute > CHUTE_MAXIMO):
        print('O número deve ser entre {} e {}!'.format(CHUTE_MINIMO, CHUTE_MAXIMO))
        continue
    print('Você digitou:',chute)

    acertou = chute == numero
    maior = chute > numero
    menor = chute < numero
    if(acertou):
        print(MENSAGEM_OK)
        break
    elif(maior):
        print(MENSAGEM_MAIOR)
        pontuacao -= chute - numero
    elif(menor):
        print(MENSAGEM_MENOR)
        pontuacao -= numero - chute
print(MENSAGEM_FINAL)
print('Sua taxa de acerto é: {:04.2f}'.format(tentativa/TENTATIVAS_MAXIMO))
print('Você fez {} pontos'.format(pontuacao))