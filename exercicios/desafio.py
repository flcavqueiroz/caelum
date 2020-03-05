'''ESTRUTURA DE DADOS:

1. Faça um programa que leia dados do usuário (nome, sobrenome, idade) 
adicione em uma lista e imprima seus elementos na tela.


1. Faça um programa que leia 4 notas, mostre as notas e a média na tela.


1. Faça um programa utilizando um `dict` que leia dados de entrada do usuário. 
O usuário deve entrar com os  dados de uma pessoa como nome, idade e cidade 
onde mora (fique livre para acrescentar outros). Após isso, você deve imprimir 
os dados como o exemplo abaixo:
    
      nome: João
      idade: 20
      cidade: São Paulo


1. (Desafio) Utilize o exercício anterior e adicione a pessoa em uma lista. 
Pergunte ao usuário se ele deseja adicionar uma nova pessoa. Após adicionar 
dados de algumas pessoas, você deve imprimir todos os dados de cada pessoa de 
forma organizada.'''

#Programa 01 - Dados do usuário
dados = []
dicionario = {
    'nome': 'Fernando',
    'sobrenome': 'Queiroz',
    'idade': 31,
    'formação': 'Biologia'
}
for i in dicionario.values():
    dados.append(i)
print(dados)

#Programa 02 - Notas e Media
notas = []
media = 0
usuario = int(input('Insira 4 notas (com decimais) para saber a média: '))


for i in range(usuario):
    '''dados = input('Idade/altura:    ').split(" ")
    idades.append(float(dados[0]))
    alturas.append(float(dados[1]))'''