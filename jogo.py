import random

def escolher_palavra():
    with open('palavras.txt', 'r') as arquivo:
        palavras = arquivo.read().splitlines()
    return random.choice(palavras)

def jogar(palavra_secreta):
    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        print(letras_acertadas)
        chute = input("Chute uma letra: ").strip().lower()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Você errou!")

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas

        print(letras_acertadas)
        print("Erros: {}".format(erros))

    if(acertou):
        print("Parabéns, você ganhou!")
    else:
        print("Você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))