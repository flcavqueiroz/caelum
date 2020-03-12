from conta import Conta, ContaCorrente, ContaPoupanca


class AtualizadorDeContas():

    def __init__(self, selic, saldo_total=0):
        self._selic = selic
        self._saldo_total = saldo_total

    
       
    @property
    def saldo_total(self):
        return self._saldo_total

    
    def roda(self, conta):
        print(f'Saldo anterior: {self._saldo_total}')
        conta.atualiza(self._selic)
        print(f'Saldo atualizado: {conta.saldo}')
        self._saldo_total += conta.saldo

        
if __name__ == "__main__":
    c = ContaPoupanca('Elisa', '123-4', 1000.0)
    cc = ContaCorrente('Fernando', '123-5', 1000.0)
    cp = ContaPoupanca('João', '123-6', 1000.0)

    adc = AtualizadorDeContas(0.01)

    adc.roda(c)
    adc.roda(cc)
    adc.roda(cp)

    print(f'Saldo total: {adc.saldo_total}')