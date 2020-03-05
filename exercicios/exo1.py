lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
print(f'Valor máximo na lista: {max(lista)}')
print(f'Valor mínimo na lista: {min(lista)}')
pares = []
media = 0
soma_negativos = 0



for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        pares.append(lista[i])
    print(pares)
    media =+ media + lista[i]
media = media / len(lista)
print(media)
if lista[i] < 0:
    soma_negativos = soma_negativos + lista[i]
print(soma_negativos)