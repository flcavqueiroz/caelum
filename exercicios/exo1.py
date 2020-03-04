lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
print(min(lista))
print(max(lista))
pares = []
for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        pares.append(lista[i])
    print(pares)
print(lista.index([0]))
print(len(lista))