def jogar():


    print('*' * 30)
    print(' ' * 7, 'Jogo da Forca')
    print('*' * 30)

    palavra_secreta = 'banana'
    palavra_acertada = ['_', '_', '_', '_', '_', '_',]

    acertou = False
    errou  = False

    num_erros = 0

    print(palavra_acertada)

    while(not acertou and not errou):

        chute = input('Digite uma letra: ').lower()
        if chute in palavra_secreta:
            posicao = 0
            for letra in palavra_secreta:
                if letra == chute:
                    #print(f'Encontrei a letra {letra} na posicao {posicao}')
                    palavra_acertada[posicao] = letra
                posicao += 1
        else:
            num_erros += 1


        acertou = '_' not in palavra_acertada
        errou = num_erros == 6
        print(palavra_acertada)

    if (acertou):
        print('Você acertou!')
    else:
        print('Você atingiu o limite de tentativas!')
    print('Fim do Jogo')