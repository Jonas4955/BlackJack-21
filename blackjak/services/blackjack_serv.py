from models.player_class import Player

class BlackJack(Player):
    def __init__(self, nome=None):
        self.__nome = nome

    def mostrar_cartas(self):
        dict_cartas = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'A':'1 ou 11', 'J':10, 'Q':10, 'K':10}
        for k, v in dict_cartas.items():
            print(f'\033[1;33mCarta: \033[1;32m{k} \033[1;33mValor: \033[1;32m{v}\033[m')

    def resultado(self, soma):
        print(f'Seu score é de {soma}')
        if soma == 21:
            resultado = f'\033[1;32mParabéns \033[1;34m{self.__nome} \033[1;32mVocê Venceu!!!\033[m\n'
        else:
            resultado = f'\033[1;33mQue pena {self.__nome} Você Perdeu \033[1;31m:(\033[m\n'
        return resultado

    def restart(self, opcao):
        if opcao == True:
            return True
        else:
            return False

