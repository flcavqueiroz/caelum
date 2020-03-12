import datetime
import csv
import cliente
import abc


class Conta(abc.ABC):
    """
    Cria uma conta passando quatro atributos:
        x = Conta(a, b, c, d)
        a = titular
        b = numero
        c = saldo
        d = limite
    """


    __slots__ = ('_titular', '_numero', '_saldo', '_limite', 'historico')


    _contador = 0

    def __init__(self, titular, numero, saldo, limite=1000.0):
        """
        Inicia o objeto Conta e inclui a data em que a conta foi criada
        """
        print('Criando uma nova conta')
        self._titular = titular
        self._numero = numero
        self._saldo = saldo
        self._limite = limite
        Conta._contador += 1
        self.historico = Historico()

    @staticmethod
    def get_contador():
        """Retorna o número de contas criadas"""
        return Conta._contador

    @property
    def saldo(self):
        return float(self._saldo)
    
    @saldo.setter
    def saldo(self, saldo):
        if self._saldo < 0:
            print('Saldo não pode ser negativo')

    
    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        self._titular = titular.capitalize()

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    def saca(self, valor):
        """
        Função de saque para a conta criada
            Recebe 2 argumentos: conta e valor a ser sacado
        """
        if self._saldo < valor:
            return False
        else:
            self._saldo -= valor
            self.historico.transacoes.append(f'saque de {valor}')

    def deposita(self, valor):
        """
        Função de depósito para a conta criada
            Recebe 2 argumentos: conta e valor a ser depositado
        """
        self._saldo += valor
        #self.historico.transacoes.append(f'depósito de {valor}')


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
            #self.historico.transacoes.append(f'transferencia de {valor} para {destino}')
            return True
            

    def extrato(self):
        """
        Função que retorna o valor do extrato da conta criada
            Recebe apenas um parâmetro: conta
        """
        print(f'numero: {self.numero}\nsaldo: {self.saldo}')

    @abc.abstractmethod
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa


    def __str__(self):
        return f'Titular: {self._titular} - Número: {self._numero} - Saldo: {self._saldo}'


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

        


class ContaCorrente(Conta):

    
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2


    def deposita(self, valor):
        self._saldo += valor - 0.1



class ContaPoupanca(Conta):


    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3


class ContaInvestimento(Conta):
    
    
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5


if __name__ == '__main__':
    #c = Conta('Fernando', '123-4', 1000.0)
    cc = ContaCorrente('Elisa', '123-5', 1000.0)
    cp = ContaPoupanca('Joao', '123-6', 1000.0)
    ci = ContaInvestimento('Elisa Maria', '123-7', 10000.0)

    #c.atualiza(0.01)
    cc.atualiza(0.01)
    cp.atualiza(0.01)
    ci.deposita(1000.0)
    ci.atualiza(0.01)




    #print(c.saldo)
    print(cc.saldo)
    print(cp.saldo)
    print(ci.saldo)

    #print(c)
    print(cc)
    print(cp)
    print(ci)