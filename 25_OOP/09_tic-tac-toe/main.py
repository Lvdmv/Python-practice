import random


class Comp:

    def __init__(self, sign):
        self.name = 'Компьютер'
        self.sign = sign
        self.step_list = []
        self.tactics = True

    def field_free(self, index):
        if tic_tac_dict[index] == ' ':
            return True
        return False

    def put_a_sign(self, steps, players):
        print('начальная стадия', steps)
        print('начальная сумма Х', self.list_signs(players.sign))
        print('начальная сумма O', self.list_signs(self.sign))
        print('нач слов:', tic_tac_dict)
        if self.sign == 'X':
            self.sign_x(steps, players)
        elif self.tactics:
            self.sign_zero(steps, players)
        else:
            self.defensive_tactics(steps)
        if self.win(steps, players):
            print_fild()
            print(f'{self.name} победа!')
            return True

    def sign_x(self, game_step, person):
        if game_step == 1:
            tic_tac_dict[5] = self.sign
        elif game_step == 2:
            self.round_two()
        elif game_step == 3:
            if self.round_three(self.sign):
                tic_tac_dict[self.round_three(self.sign)] = self.sign
            elif self.position(person.sign):
                if self.field_free(self.position(person.sign)):
                    tic_tac_dict[self.position(person.sign)] = self.sign
                else:
                    tic_tac_dict[self.put_on_field_free()] = self.sign
            elif self.round_foure(person):
                tic_tac_dict[self.round_foure(person)] = self.sign
        elif game_step == 4:
            if self.field_free(self.position2()):
                tic_tac_dict[self.position2()] = self.sign
            else:
                tic_tac_dict[self.put_on_field_free()] = self.sign
        else:
            tic_tac_dict[self.put_on_field_free()] = self.sign

    def sign_zero(self, game_step, person):

        if game_step == 1:
            if self.field_free(5):
                tic_tac_dict[5] = self.sign
            else:
                print('Включение обороны')
                tic_tac_dict[1] = self.sign
                self.tactics = False
        elif game_step == 2:
            if self.position(person.sign):
                tic_tac_dict[self.position(person.sign)] = self.sign
            else:
                self.round_two()
        elif game_step == 3:
            if self.round_three(self.sign):
                tic_tac_dict[self.round_three(self.sign)] = self.sign
            elif sum(self.list_signs(person.sign)) != 15:
                if sum(self.list_signs(person.sign)) == 8:
                    tic_tac_dict[2] = self.sign
                elif sum(self.list_signs(person.sign)) == 10:
                    if self.field_free(7):
                        tic_tac_dict[2] = self.sign
                    else:
                        tic_tac_dict[4] = self.sign
                elif sum(self.list_signs(person.sign)) == 14:
                    tic_tac_dict[6] = self.sign
                elif sum(self.list_signs(person.sign)) == 16:
                    tic_tac_dict[4] = self.sign
                elif sum(self.list_signs(person.sign)) == 20:
                    if self.field_free(3):
                        tic_tac_dict[6] = self.sign
                    else:
                        tic_tac_dict[8] = self.sign
                else:
                    tic_tac_dict[8] = self.sign
            else:
                for i_index in [1, 3, 7, 9]:
                    if self.field_free(i_index):
                        tic_tac_dict[i_index] = self.sign
                        break

        elif game_step == 4:
            if self.field_free(self.position2()):
                tic_tac_dict[self.position2()] = self.sign
            elif self.field_free(self.position2()):
                tic_tac_dict[self.position2()] = self.sign
        else:
            tic_tac_dict[self.put_on_field_free()] = self.sign

    def defensive_tactics(self, game_step):
        if game_step == 2:
            self.round_two()
        elif game_step < 4:
            for i_index in [3, 7, 9]:
                if self.field_free(i_index):
                    tic_tac_dict[i_index] = self.sign
                    break
            else:
                tic_tac_dict[self.put_on_field_free()] = self.sign
        else:
            tic_tac_dict[self.put_on_field_free()] = self.sign

    def round_two(self):
        if {i_index for i_index in [1, 3, 7, 9] if not self.field_free(i_index)}:
            if not self.field_free(1):
                tic_tac_dict[9] = self.sign
            elif not self.field_free(3):
                tic_tac_dict[7] = self.sign
            elif not self.field_free(7):
                tic_tac_dict[3] = self.sign
            elif not self.field_free(9):
                tic_tac_dict[1] = self.sign
        elif not self.field_free(2):
            tic_tac_dict[9] = self.sign
        elif not self.field_free(8):
            tic_tac_dict[1] = self.sign
        elif not self.field_free(4):
            tic_tac_dict[3] = self.sign
        elif not self.field_free(6):
            tic_tac_dict[7] = self.sign

    def round_three(self, sign):
        if 5 in self.list_signs(sign):
            if self.field_free(10 - sum(
                    [i_index for i_index in [1, 3, 7, 9] if i_index in self.list_signs(sign)])):
                return 10 - sum(
                    [i_index for i_index in [1, 3,  7, 9] if i_index in self.list_signs(sign)])
            elif self.field_free(10 - sum({i_index for i_index in [2, 4, 6, 8] if i_index in self.list_signs(sign)})):
                return 10 - sum(
                    [i_index for i_index in [2, 4, 6, 8] if i_index in self.list_signs(sign)])
            else:
                return False
        else:
            return False

    def round_foure(self, players):
        if sum(self.list_signs(players.sign)) == 7:
            if self.field_free(3):
                return 7
            else:
                return 9
        elif sum(self.list_signs(players.sign)) == 9:
            if self.field_free(3):
                return 3
            else:
                return 9
        elif sum(self.list_signs(players.sign)) == 11:
            if self.field_free(1):
                return 1
            else:
                return 7
        elif sum(self.list_signs(players.sign)) == 13:
            if self.field_free(1):
                return 1
            else:
                return 3
        else:
            return False

    def position(self, sign):
        if sum(self.list_signs(sign)) < 6:
            if {i_num for i_num in [2, 3] if i_num in self.list_signs(sign)}:
                return 6 - sum(self.list_signs(sign))
            elif 4 in self.list_signs(sign):
                return 12 - sum(self.list_signs(sign))
        elif sum(self.list_signs(sign)) < 12:
            if 7 in self.list_signs(sign):
                return 12 - sum(self.list_signs(sign))
            elif 3 in self.list_signs(sign):
                return 18 - sum(self.list_signs(sign))
        elif sum(self.list_signs(sign)) < 18:
            if {i_num for i_num in [3, 6] if i_num in self.list_signs(sign)}:
                return 18 - sum(self.list_signs(sign))
            elif {i_num for i_num in [7, 8] if i_num in self.list_signs(sign)}:
                return 24 - sum(self.list_signs(sign))

    def position2(self):
        if sum(self.list_signs(self.sign)) == 9:
            if self.field_free(2):
                return 2
            elif self.field_free(7):
                return 7
            elif self.field_free(9):
                return 9
        elif sum(self.list_signs(self.sign)) == 13:
            if self.field_free(4):
                return 4
            elif self.field_free(3):
                return 3
            elif self.field_free(9):
                return 9
        elif sum(self.list_signs(self.sign)) == 17:
            if self.field_free(6):
                return 6
            elif self.field_free(7):
                return 7
            elif self.field_free(1):
                return 1
        elif sum(self.list_signs(self.sign)) == 21:
            if self.field_free(8):
                return 8
            elif self.field_free(1):
                return 1
            elif self.field_free(3):
                return 3
        return 15 - sum([i_pair for i_pair in (2, 4, 5, 6, 8) if i_pair in self.list_signs(self.sign)])

    def list_signs(self, sign):
        my_sign = []
        for i_index, i_sign in tic_tac_dict.items():
            if i_sign == sign:
                my_sign.append(i_index)
        return my_sign

    def put_on_field_free(self):
        for i_field in tic_tac_dict:
            if self.field_free(i_field):
                return i_field

    def win(self, stage, new_person):
        print('конечная стадия', stage)
        print('конечная сумма X', self.list_signs(new_person.sign))
        print('конечная сумма O', self.list_signs(self.sign))
        print('Конеч слов:', tic_tac_dict)
        if stage == 3:
            if sum(self.list_signs(self.sign)) == 15:
                return True
        elif stage == 4:
            if sum(self.list_signs(new_person.sign)) not in [12, 14, 16, 18]:
                return True
        elif stage == 5:
            if sum(self.list_signs(new_person.sign)) not in [16, 18, 22, 24]:
                return True
        return False


class Plyer:

    def __init__(self, sign):
        self.name = 'Игрок'
        self.sign = sign
        self.step_list = []

    def field_free(self, index):
        if tic_tac_dict[index] == ' ':
            return True
        return False


def print_fild():
    print(f'|{"-" * 17}|')
    print(
        f'|{" " * 2}{tic_tac_dict[1]}{" " * 2}|{" " * 2}{tic_tac_dict[2]}{" " * 2}|'
        f'{" " * 2}{tic_tac_dict[3]}{" " * 2}|'
    )
    print(f'|{"-" * 17}|')
    print(
        f'|{" " * 2}{tic_tac_dict[4]}{" " * 2}|{" " * 2}{tic_tac_dict[5]}{" " * 2}|'
        f'{" " * 2}{tic_tac_dict[6]}{" " * 2}|'
    )
    print(f'|{"-" * 17}|')
    print(
        f'|{" " * 2}{tic_tac_dict[7]}{" " * 2}|{" " * 2}{tic_tac_dict[8]}{" " * 2}|'
        f'{" " * 2}{tic_tac_dict[9]}{" " * 2}|')
    print(f'|{"-" * 17}|'
          )


def step(count, sign):
    while count != 5:
        try:
            print_fild()
            a = int(input('Выберите номер строки: '))
            b = int(input('Выберите номер столбца: '))
            index = (a - 1)*3 + b
            if index > 9:
                raise KeyError
            if player.field_free(index):
                tic_tac_dict[index] = sign
                count += 1
                if comp.put_a_sign(count, player):
                    return True
            else:
                print('Это поле уже занято')
        except KeyError:
            print('Строка или число выходят за границы игрового поля!')
            print('Введите заново')
        except ValueError:
            print('Можно вводить только числа')
    return False


tic_tac_dict = {i_key: " " for i_key in range(1, 10)}

sign_player = random.choice(('X', 'O'))
player = Plyer(sign_player)
counter = 0

print(f'Вы играете {sign_player}: ')
if sign_player != 'X':
    comp = Comp('X')
    counter += 1
    comp.put_a_sign(1, player)
else:
    comp = Comp('O')
if not step(counter, sign_player):
    print_fild()
    print('Ничья')
