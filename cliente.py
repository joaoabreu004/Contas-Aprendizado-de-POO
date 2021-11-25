class Cliente:
    def __init__(self, nome):
        self.__nome = nome


    #subtituindo o get com "property"
    @property
    def nome(self):
      print("chamando @property nome()")
      return self.__nome.title()

    #forma alternativa de usar o setter.
    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome