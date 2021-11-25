class Retangulo:

    def __init__(self, x, y):
        print("construindo objeto...{}".format(self))
        self.__x = x
        self.__y = y
        self.__area = x * y

    def obter_area(self):
        return self.__area