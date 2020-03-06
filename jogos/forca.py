import random

def jogar():


    titulo()


    palavra_secreta = carrega_palavra_secreta()
    
    letra_acertada = inicializa_letra_acertada(palavra_secreta)
    print(letra_acertada)

    acertou = False
    errou  = False
    num_erros = 0
    while(not errou and not acertou):
        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letra_acertada, palavra_secreta)
        else:
            num_erros += 1
            desenha_forca(num_erros)
        errou = num_erros == 7
        acertou = '_' not in letra_acertada

        print(letra_acertada)
    
    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
    #print(palavra_secreta)




        """ acertou = '_' not in letra_acertada
        errou = num_erros == len(letra_acertada)
        print(letra_acertada)

    if (acertou):
        print('Você acertou!')
    else:
        print('Você atingiu o limite de tentativas!')
    print('Fim do Jogo') """


def titulo():
    print('*' * 30)
    print(' ' * 7, 'Jogo da Forca')
    print('*' * 30)

def carrega_palavra_secreta():
    with open('palavra.txt', 'r') as arquivo:
        palavras = [l.strip() for l in arquivo]
        
        """for l in arquivo:
            palavras.append(l.strip()) """
    
    num = random.randrange(0, len(palavras))

    palavra_secreta = palavras[num].lower()
    return palavra_secreta

def inicializa_letra_acertada(palavra_secreta):
    return ['_' for l in palavra_secreta]

def pede_chute():
    chute = input('Digite uma letra: ').lower()
    return chute
    

def marca_chute_correto(chute, letra_acertada, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if letra == chute:
            #print(f'Encontrei a letra {letra} na posicao {posicao}')
            letra_acertada[posicao] = letra
        posicao += 1
    















def imprime_mensagem_perdedor(palavra_secreta):
    print('Puxa, você foi enforcado!')
    print(f'A palavra era {palavra_secreta}')
    print("    _______________         ")
    print("   /               \        ")
    print("  /                 \       ")
    print("//                   \/\    ")
    print("\|   XXXX     XXXX   | /    ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/      ")
    print("   |\     XXX     /|        ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/        ")
    print("     \_         _/          ")
    print("       \_______/            ")

def imprime_mensagem_vencedor():
    print('Parabéns, você ganhou!')
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

def desenha_forca(num_erros):
    print("  _______     ")
    print(" |/      |    ")

    if(num_erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(num_erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(num_erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(num_erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(num_erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(num_erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (num_erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
