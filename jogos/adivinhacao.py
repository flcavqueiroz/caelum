print('*' * 30)
print(' '* 4, 'Jogo da advinhação')
print('*' * 30)
print('Você terá 3 tentativas para acertar')
print('-' * 30)

numero_secreto = 42
tentativas = 3
rodada = 1
""" nivel = int(input('Escolha um nível de dificuldade'))
 """
for rodada in range(1, tentativas + 1):
    print(f'Tentativa {rodada} de {tentativas}')

    chute = int(input('Digite um número: '))
    print(f'Você digitou: {chute}')

    acerto = chute == numero_secreto
    menor = chute < numero_secreto
    maior = chute > numero_secreto

    #pede o chute do usuário


    if acerto:
        print(f'Após {rodada} rodada(s), Você acertou!')
        break
    elif menor:
        print('Seu chute foi menor')
    elif maior:
        print('Seu chute foi maior')
    rodada = rodada + 1
print('*' * 30,'\nFim do jogo')