class Conta:
    def __init__(self, n_agencia, saldo=0):
        self.__saldo = saldo;
        self.n_agencia = n_agencia;

    def depositar(self, valor):
        self.__saldo += valor;

    def sacar(self, valor):
        self.__saldo -= valor;

    def mostrar_saldo(self):
        return self.__saldo;

conta = Conta("0001", 100);
print(conta.n_agencia);
print(conta.mostrar_saldo());