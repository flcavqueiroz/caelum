import datetime
class Conta:
    def __init__(self, titular, numero, saldo, limite):
        print('Criando uma nova conta')
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def saca(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append(f'saque de {valor}')

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f'depósito de {valor}')


    def transfere_para(self, destino, valor):
        retira = self.saca(valor)
        if retira == False:
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append(f'transferencia de {valor} para {destino}')
            return True
            

    def extrato(self):
        print(f'numero: {self.numero}\nsaldo: {self.saldo}')

class Historico:

    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print(f'data abertura: {self.data_abertura}')
        print('transações: ')
        for t in self.transacoes:
            print('-', t)