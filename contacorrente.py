#Criando uma classe (ContaCorrente)

#nomemclatura CamelCase
class ContaCorrente:

# self é a referência que sabe onde encontrar o endereço onde o objeto foi criado
    def __init__(self, numero, titular, saldo, limite):
        print("construindo objeto...{}".format(self))
        #deixando atributos privados!
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        #self.__codigo_banco = "001" #<- ATRIBUTO FIXO


    # métodos = comportamentos
    def extrato(self):
        print("O saldo do {} é R${}".format(self.__titular, self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_para_sacar = (self.__saldo + self.__limite)
        return valor_a_sacar <= valor_disponivel_para_sacar

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor R${}, passou o limite".format(valor))

    def transferir(self, valor, conta_destino):
        self.sacar(valor)
        conta_destino.depositar(valor)

    #get = obter (retorna um valor)

    @property
    def titular(self):
        return self.__titular

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        print("chamando @property limite()")
        return self.__limite

    #set definir (definir um novo valor)

    @limite.setter
    def limite(self, limite):
        print("chamando setter limite()")
        self.__limite = limite

    #MÉTODO ESTÁTICO, POIS NÃO PRECISA DE OBJETO!
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_banco():
        return {'BB':'001', 'CAIXA':'104', 'BRADESCO':'237'}

