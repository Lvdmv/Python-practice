import random


class Blackjack:

    def __init__(self, name):
        self.hand = dict()
        self.name = name

    def take_cards(self, count):
        for num in range(count):
            while True:
                card_player = random.randint(0, len(cards_list) - 1)
                if cards_list[card_player][2] == 0:
                    cards_list.remove(cards_list[card_player])
                else:
                    break
            if cards_list[card_player][0] in self.hand:
                self.hand[cards_list[card_player][0]] += cards_list[card_player][1]
            else:
                self.hand[cards_list[card_player][0]] = cards_list[card_player][1]
            if self.summ() > 21:
                if 'ace' in self.hand:
                    self.hand['ace'] = 1
            cards_list[card_player][2] -= 1
            print(f'Карта {self.name} {num + 1}: {cards_list[card_player][0]}')

    def summ(self):
        return sum(self.hand.values())


cards_list = [
    ['2', 2, 4], ['3', 3, 4], ['4', 4, 4], ['5', 5, 4],
    ['6', 6, 4], ['7', 7, 4], ['8', 8, 4], ['9', 9, 4],
    ['10', 10, 4], ['jack', 10, 4], ['ace', 11, 4],
    ['queen', 10, 4], ['king', 10, 4]
]
player_hand = Blackjack('Игрок')
casino_hand = Blackjack('Компьютер')

player_hand.take_cards(2)

while True:
    if player_hand.summ() > 21:
        print(f'Перебор! Сумма игрока {player_hand.summ()}! Компьютер выиграл!')
        break
    action = input('\nеще?/стоп ')
    if action == 'еще':
        player_hand.take_cards(1)
    else:
        casino_hand.take_cards(2)
        print(f'\nСумма очков игрока: {player_hand.summ()}')
        print(f'Сумма очков компьютера: {casino_hand.summ()}')
        if player_hand.summ() == 21:
            if casino_hand.summ() == 21:
                print('Ничья')
            else:
                print('Игрок победил')
        elif casino_hand.summ() == 21:
            print('Компьютер победил')
        elif player_hand.summ() > casino_hand.summ():
            print('Игрок победил')
        elif player_hand.summ() < casino_hand.summ():
            print('Компьютер победил')
        else:
            print('Ничья')
        break
