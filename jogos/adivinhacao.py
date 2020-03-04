print('*' * 30)
print(' '* 4, 'Jogo da advinhação')
print('*' * 30)
#print('Você terá 3 tentativas para acertar') """
print('-' * 50)
print('Escolha um nível de dificuldade:\n\n'
    'Nível fácil: [1] = 20 tentativas\n'
    'Nível intermediário: [2] = 10 tentativas\n'
    'Nível difícil: [3] = 3 tentativas\n')
print('-' * 50)
print('Você iniciará o jogo com 1000 pontos\n'
    'O valor do seu chute será subtraído da sua pontuação\n'
    'Caso sua pontuação atinga Zero, o jogo terminará')
print('-' * 50)
pontos = 1000
numero_secreto = 42
tentativas = 3
rodada = 1
nivel = int(input('Escolha um nível de dificuldade: '))
if nivel == 1:
    tentativas += 17
elif nivel == 2:
    tentativas += 7
else:
    nivel == tentativas

for rodada in range(1, tentativas + 1):
    print(f'Rodada {rodada} de {tentativas}')

    chute = int(input('Digite um número: '))
    print(f'Você digitou: {chute}')
    
    

    acerto = chute == numero_secreto
    menor = chute < numero_secreto
    maior = chute > numero_secreto

   
    if acerto:
        print(f'Após {rodada} rodada(s), Você acertou!')
        break
    elif menor:
        print('Seu chute foi menor')
    elif maior:
        print('Seu chute foi maior')
    #rodada = rodada + 1
print('*' * 30,'\nFim do jogo')