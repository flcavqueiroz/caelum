from flask import Flask, render_template, request
from conta import Conta
import csv


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('form.html')


@app.route("/cria_conta", methods=['POST'])
def cria():
    numero = request.form.get('numero')
    titular = request.form.get('titular')
    saldo = float(request.form.get('saldo'))
    limite = float(request.form.get('limite'))

    conta = Conta(numero, titular, saldo, limite)

    arquivo = open('contas.txt', 'a')
    arquivo.write(f'{conta.numero}, {conta.titular}, {conta.saldo}, {conta.limite}')
    arquivo.close()

    return redirect(url_for('lista_contas'))

@app.route("/contas")
def lista_contas():
    arquivo = open('contas.txt', 'r')
    leitor_csv = csv.reader(arquivo)
    l_contas = []

    for l in leitor_csv:
        conta = Conta(l[0], l[1], float(l[2]), float(l[c]))
        l_contas.append(conta)


    arquivo.close()

    return render_template('lista.html', contas=l_contas)
if __name__ == "__main__":
    app.run()