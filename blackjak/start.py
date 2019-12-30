import sys
sys.path.append('C:/Users/55479/Desktop/blackjak/')

from random import shuffle
from models.opcao_class import Opcao
from services.cartas_serv import CartasDao
from services.blackjack_serv import BlackJack

print('\033[1;34m', '-'*30, '\033[1;31mBlackJack(21)', '\033[1;34m', '-'*30, '\033[m')
nome = input('Digite seu nome: ')
print('\033[1;34m', '-'*30, '\033[1;31mCartas e Valores', '\033[1;34m', '-'*30, '\033[m')
player = BlackJack(nome)
player.mostrar_cartas()

restart = True
while restart == True:
    rodadas = 0
    soma = 0
    while soma < 21:
        escolha = input('\nDigite ENTER para virar uma Carta: ')
        opcao = Opcao(escolha)
        if opcao.get_opcao() == True:
            carta = CartasDao()
            carta_sort = carta.carta_sorted()
            rodadas += 1
            print(carta.valor_de_carta(carta_sort, rodadas))
            soma += carta.valor_de_carta(carta_sort, rodadas)

    blackjak = BlackJack()
    print(blackjak.resultado(soma))
    escolha = input('Digite ENTER para Jogar novamente: ')
    opcao = Opcao(escolha)
    blackjak.restart(opcao)
