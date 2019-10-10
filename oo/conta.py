class Conta:
    def __init__(self, numero, titular, saldo, limite):
        # print("construindo objeto {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O saldo de {} é: {}".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if (self.__saldo - valor > 0 - self.__limite):
            self.__saldo -= valor

    def transfere(self, valor, destino):
        """Retira o valor da conta que chama o metodo e deposita no conta declarada

        :param destino:
        :param valor:
        """
        self.saca(valor)
        destino.deposita(valor)

# TODO: escrever a classe
