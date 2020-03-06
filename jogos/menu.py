import adivinhacao
import forca

print('Escolha um jogo')
print('1 - Adivinhação''\n''2 - Forca')
escolha = int(input('Digite um número: '))

if escolha == 1:
    adivinhacao.jogar()
elif escolha == 2:
    forca.jogar()

else:
    print('Opção Inválida')

