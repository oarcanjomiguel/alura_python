class Conta:
    def __init__(self, numero, titular, saldo, limite):
        # print("construindo objeto {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("O saldo de {} é: {}".format(self.titular, self.saldo))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if (self.saldo - valor > 0 - self.limite):
            self.saldo -= valor

# TODO: escrever a classe
