import random


class Blackjack:
    cards_list = [
        ['2', 2, 4], ['3', 3, 4], ['4', 4, 4], ['5', 5, 4],
        ['6', 6, 4], ['7', 7, 4], ['8', 8, 4], ['9', 9, 4],
        ['10', 10, 4], ['jack', 10, 4], ['ace', 11, 4],
        ['queen', 10, 4], ['king', 10, 4]
    ]

    def __init__(self, name_player):
        self.name = 'Компьютер'
        self.cards = dict()
        self.player = name_player

    def start(self):
        self.take_cards(2, self.player.cards)
        while True:
            if sum(self.player.cards.values()) > 21:
                print(f'Перебор! Сумма игрока {sum(self.player.cards.values())}! Компьютер выиграл!')
                break
            action = input('\nеще?/стоп ')
            if action == 'еще':
                self.take_cards(1, self.player.cards)
            else:
                self.take_cards(2, self.cards)
                print(f'\nСумма очков игрока: {sum(self.player.cards.values())}')
                print(f'Сумма очков компьютера: {sum(self.cards.values())}')
                if sum(self.player.cards.values()) == 21:
                    if sum(self.cards.values()) == 21:
                        print('Ничья')
                    else:
                        print('Игрок победил')
                elif sum(self.cards.values()) == 21:
                    print('Компьютер победил')
                elif sum(self.player.cards.values()) > sum(self.cards.values()):
                    print('Игрок победил')
                elif sum(self.player.cards.values()) < sum(self.cards.values()):
                    print('Компьютер победил')
                else:
                    print('Ничья')
                break

    def take_cards(self, count, cards):
        for num in range(count):
            card_player = random.randint(0, len(Blackjack(self.player.cards).cards_list) - 1)
            while True:
                if Blackjack(self.player).cards_list[card_player][2] == 0:
                    Blackjack(self.player).cards_list.remove(Blackjack(self.player).cards_list[card_player])
                else:
                    break
            if Blackjack(self.player).cards_list[card_player][0] in cards:
                cards[Blackjack(self.player).cards_list[card_player][0]] \
                    += Blackjack(self.player).cards_list[card_player][1]
            else:
                cards[Blackjack(self.player).cards_list[card_player][0]] \
                    = Blackjack(self.player).cards_list[card_player][1]
            if sum(cards.values()) > 21:
                if 'ace' in cards:
                    cards['ace'] = 1
            Blackjack(self.player).cards_list[card_player][2] -= 1
            print(f'Карта {num + 1}: {Blackjack(self.player).cards_list[card_player][0]}')


class Player:

    def __init__(self, name):
        self.name = name
        self.cards = dict()


player_hand = Player(input('Введите имя игрока: '))
play = Blackjack(player_hand)
play.start()
