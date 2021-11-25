#TESTE PEGO NA ALURA!!!

class Conta:
    def __init__(self, numero, saldo, limite):
        self.__numero = numero
        self.__saldo = saldo
        self.__limite = limite
        self.__tarifaTransferencia = 8.0

    #NOVO MÉTODO AQUI
    def __temSaldoDisponivelPara(self, valor):
        return valor < (self.__saldo + self.__limite)


    def saca(self, valor):

        if self.__temSaldoDisponivelPara(valor):
            self.__saldo -= valor
            print("Saque efetuado.")
        else:
            print("Saldo insuficiente.")


    def transfere(self, valor, destino):


        valorTotal = valor + self.__tarifaTransferencia

        if self.__temSaldoDisponivelPara(valorTotal):

            self.__saldo -= valorTotal
            destino.deposita(valor)

            print("Transferência efetuada.")
        else:
            print("Saldo insuficiente.")



#Embora o método criado (temSaldoDisponivelPara) evite a duplicação de códigos,
# ele não será chamado por nenhuma outra classe do sistema.
#Logo, não faz sentido deixá-lo público
# e expô-lo na interface pública da classe.