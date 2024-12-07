import jogo

def iniciar_jogo():
    palavra_secreta = jogo.escolher_palavra()
    jogo.jogar(palavra_secreta)

if __name__ == "__main__":
    iniciar_jogo()