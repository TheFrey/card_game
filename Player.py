import abc
import time
import random

from Const import MESSAGES


class AbstractPlayer(abc.ABC):

    def __init__(self, name='Dealer'):
        self.name = name
        self.cards = []
        self.full_points = 0

    def change_points(self):
        self.full_points = sum([card.points for card in self.cards])

    def take_card(self, card):
        self.cards.append(card)
        self.change_points()

    @abc.abstractmethod
    def ask_card(self):
        pass

    def print_cards(self):
        print('------***------')
        print(self.name, " data")
        for card in self.cards:
            print(card)
        time.sleep(1)
        print('Full points: ', self.full_points)


class Player(AbstractPlayer):

    def ask_card(self):
        choice = input(MESSAGES.get('ask_card'))
        if choice == 'y':
            print('{} take a card'.format(self.name))
            time.sleep(1)
            return True
        else:
            return False

    def ace_value(self):
        for card in self.cards:
            if card.rank == 'ace':
                while True:
                    message = MESSAGES.get('ace_check')
                    check = input(message)
                    if check == '1':
                        card.points = 1
                        break
                    elif check == '11':
                        card.points = 11
                        break
                    else:
                        print('Incorrect input')
            self.change_points()


class Cardsharp(Player):

    def ask_card(self):
        choice = input(MESSAGES.get('ask_card'))
        if choice == 'y':
            print('{} take a card'.format(self.name))
            time.sleep(1)
            return True
        else:
            return False

    def ability(self, card):
        message = MESSAGES.get('set_ability')
        check2 = input(message)

        match check2:
            case '1':
                self._change_first_card(card)
            case '2':
                self._change_lust_card(card)
        self.print_cards()

    def _change_lust_card(self, card):
        print('Cheater')
        self.cards.pop()
        self.take_card(card)

    def _change_first_card(self, card):
        print('Cheater')
        self.cards.pop(0)
        self.take_card(card)


class Bot(AbstractPlayer):

    def __init__(self, name):
        super().__init__(name)
        self.max_points = random.randint(17, 20)

    def ask_card(self):
        if self.full_points < self.max_points:
            print('-----***-----')
            print('{} take a card'.format(self.name))
            time.sleep(1)
            return True
        else:
            return False


class Dealer(AbstractPlayer):

    max_points = 17

    def ask_card(self):
        if self.full_points < self.max_points:
            return True
        else:
            return False
