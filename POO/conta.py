import datetime

class Conta:
    """
    Cria uma conta passando quatro atributos:
        x = Conta(a, b, c, d)
        a = titular
        b = numero
        c = saldo
        d = limite
    """

    def __init__(self, titular, numero, saldo, limite):
        """
        Inicia o objeto Conta e inclui a data em que a conta foi criada
        """
        print('Criando uma nova conta')
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def saca(self, valor):
        """
        Função de saque para a conta criada
            Recebe 2 argumentos: conta e valor a ser sacado
        """
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append(f'saque de {valor}')

    def deposita(self, valor):
        """
        Função de depósito para a conta criada
            Recebe 2 argumentos: conta e valor a ser depositado
        """
        self.saldo += valor
        self.historico.transacoes.append(f'depósito de {valor}')


    def transfere_para(self, destino, valor):
        """
        Função que realiza uma transferencia de uma conta origem para outra destino
            Recebe dois parâmetros: destino e valor
        """

        retira = self.saca(valor)
        if retira == False:
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append(f'transferencia de {valor} para {destino}')
            return True
            

    def extrato(self):
        """
        Função que retorna o valor do extrato da conta criada
            Recebe apenas um parâmetro: conta
        """
        print(f'numero: {self.numero}\nsaldo: {self.saldo}')

class Historico:

    def __init__(self):
        """
        Função que determina a data de abertura da conta e suas transações
        """
        self.data_abertura = datetime.date.today()
        self.transacoes = []

    def imprime(self):
        """
        Função que imprime a data de abertura da conta e suas transações
        """
        print(f'data abertura: {self.data_abertura}')
        print('transações: ')
        for t in self.transacoes:
            print('-', t)

if __name__ == '__main__':
