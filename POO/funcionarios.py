class Funcionario:


    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario


    @property
    def nome(self):
        return self._nome


    @property
    def cpf(self):
        return self._cpf


    @property
    def salario(self):
        return self._salario

    
    @property
    def get_bonificacao(self):
        return self._salario * 0.1


class Gerente(Funcionario):


    def __init__(self, nome, cpf, salario, senha, qtd_gerenciados):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_gerenciados = qtd_gerenciados


    @property
    def senha(self):
        return self._senha
    

    def autentica(self, senha):
        if self._senha == senha:
            print('Acesso permitido')
            return True
        else:
            print('Acesso negado')
            return False


    @property
    def get_bonificacao(self):
        super().get_bonificacao() + 1000

    @property
    def qtd_gerenciados(self):
        return self._qtd_gerenciados