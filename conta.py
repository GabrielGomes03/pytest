class Conta:
    def __init__(self, numero, titular, saldo = 0):
        self.numero = numero
        self.titular = titular
        self.__saldo = saldo
        self.__limite = 50

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            self.__saldo += 0

        elif valor == 0:
            self.__saldo += 0
            return None

        else:
            self.__saldo += valor

    def sacar(self, valor):
        if (self.saldo + self.limite) > valor:
            self.__saldo -= valor
            return True

        else:
            return False

    def conta_teste2(self):
        return '321'

        
    def extrato(self, validacao):
        if validacao == 0:
            return False

    def transferir(self, numero, valor):
        if numero == self.conta_teste2():
            if valor <= (self.saldo + self.limite):
                self.sacar(valor)
                return True 
            else:
                return False
        else:
            return False
