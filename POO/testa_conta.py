def cria_conta(titular, numero, saldo, limite):
    """
    Função que cria uma conta dados os parâmetros:
        titular : str
        numero : str
        saldo : float
        limite : float
    """

    conta = {'titular': titular, 'numero': numero, 'saldo': saldo, 'limite': limite}
    return conta
    
def saca(conta, valor):
    """
    Função de saque para a conta criada
        Recebe 2 argumentos: conta e valor a ser sacado
    """
    conta['saldo'] -= float(valor)

def deposita(conta, valor):
    """
    Função de depósito para a conta criada
        Recebe 2 argumentos: conta e valor a ser depositado
    """
    conta['saldo'] += float(valor)

def extrato(conta):
    """
    Função que retorna o valor do extrato da conta criada
        Recebe apenas um parâmetro: conta
    """

    print(f'numero: {conta["numero"]} \nsaldo: {conta["saldo"]}')


if __name__ == '__main__':
    conta1 = cria_conta('João', '123-4', 12000.0, 100.00)
    conta2 = cria_conta('Maria', '123-5', 15000.0, 100.00)

    saca(conta1, 100.00)
    saca(conta2, 500.00)
    
    print(conta1['saldo'])
    print(conta2['saldo'])
    
    deposita(conta1, 20.00)
    deposita(conta2, 50.00)

    print(conta1['saldo'])
    print(conta2['saldo'])

    extrato(conta1)
    extrato(conta2)

    print(conta1['saldo'])
    print(conta2['saldo'])

