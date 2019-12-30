class Opcao:
    def __init__(self, opcao):
        self.__opcao = opcao

    def get_opcao(self):
        if self.__opcao != True:
            return True
        else:
            return False
