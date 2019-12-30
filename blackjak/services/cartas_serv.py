import sys
sys.path.append('C:/Users/55479/Desktop/blackjak/')
from random import shuffle

class CartasDao:
    def carta_sorted(self):
        list_carta = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'J', 'Q', 'K']
        shuffle(list_carta)
        carta = list_carta[0]
        return carta

    def valor_de_carta(self, nome, rodada: int):
        if nome == 'A' and rodada > 1:
            valor = 1
        elif nome == 'A' and rodada <= 1:
            valor = 11
        elif nome == 'J' or nome == 'Q' or nome == 'K':
            valor = 10
        else:
            valor = int(nome)
        return valor
