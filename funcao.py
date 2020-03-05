def soma(x, y, z):
    return x + y + z
print(soma(1, 2, 3))
"""
def imprime():
    print('oi')
    

def dados(nome, idade):
    print(nome)
    print(idade)

dados('José', 40)

def dados1(nome, idade=None):
    if idade:
        return(nome, idade)
    return nome
print(dados1('João', 52)) """


def velocidade_media(dis, t):
    return dis/t
    #print(f'{vel:.2f}')
    #return velocidade_media

print(f'{velocidade_media(100, 20):.2f}')
print(f'{velocidade_media(150, 22):.2f}')
print(f'{velocidade_media(200, 30):.2f}')
print(f'{velocidade_media(50, 3):.2f}')

def calc(a, b):
    return {'soma' : a + b, 'diferença': a - b, 
            'multiplicação': a * b, 
            'divisão': a / b}
    
    

print(calc(100, 20))

def divisão(a, b):
    return a / b

print(divisão(150, 10))