class ManipuladorDeTributaveis:

    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            total += t.get_valor_imposto()

        return total


if __name__ == "__main__":
    from conta import ContaCorrente, SeguroDeVida
    from tributavel import TributavelMixIn

    cc1 = ContaCorrente('Fernando', '123-4', 1000.0)
    cc2 = ContaCorrente('Elisa', '123-5', 5000.0)
    seguro1 = SeguroDeVida(100.0, 'Fernando', '345-77')
    seguro2 = SeguroDeVida(200, 'Elisa', '237-98')

    lista_tributaveis = []
    lista_tributaveis.append(cc1)
    lista_tributaveis.append(cc2)
    lista_tributaveis.append(seguro1)
    lista_tributaveis.append(seguro2)

    manipulador = ManipuladorDeTributaveis()
    total = manipulador.calcula_impostos(lista_tributaveis)

    print(total)