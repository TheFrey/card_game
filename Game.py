import Const
import Player
from Deck import Deck
from Const import MESSAGES
import time

import random


class Game:
    max_pl_count = 4

    def __init__(self):
        self.players = []
        self.player = None
        self.player_pos = None
        self.dealer = Player.Dealer()
        self.all_players_count = 1
        self.deck = Deck()

    @staticmethod
    def _ask_starting(message):
        while True:
            choice = input(message)
            if choice == 'n':
                return False
            elif choice == 'y':
                return True

    def _launching(self):
        while True:
            bots_count = int(input('Hello, write bots count: '))
            if bots_count <= self.max_pl_count - 1:
                break
        self.all_players_count = bots_count + 1

        for i in range(bots_count):
            b = Player.Bot(Const.NAMES[i])
            self.players.append(b)

            print(b.name, ' is created')
            time.sleep(1)

        name = input('Input your name: ')
        playercheck = input('Enter validate key: ')
        if playercheck == '1234':
            self.player = Player.Cardsharp(name)
        else:
            self.player = Player.Player(name)

        self.player_pos = random.randint(0, self.all_players_count)
        time.sleep(1)
        self.players.insert(self.player_pos, self.player)

    def first_descr(self):
        for player in self.players:
            print('-----***-----')
            print('{} take 2 card'.format(player.name))
            for _ in range(2):
                card = self.deck.get_card()
                player.take_card(card)

        card = self.deck.get_card()
        self.dealer.take_card(card)
        self.dealer.print_cards()

    def check_stop(self, player):
        if player.full_points >= 21:
            return True
        else:
            return False

    def remove_player(self, player):
        if isinstance(player, Player.Player) or isinstance(player, Player.Cardsharp):
            print('You are fall!')
        elif isinstance(player, Player.Bot):
            print('-----***-----')
            print(player.name, 'are fall!')
        self.players.remove(player)

    def ask_cards(self):
        for player in self.players:

            while player.ask_card():
                card = self.deck.get_card()
                player.take_card(card)
                if isinstance(player, Player.Player) or isinstance(player, Player.Cardsharp):
                    player.print_cards()

                is_stop = self.check_stop(player)

                if is_stop:
                    if player.full_points > 21 or isinstance(player, Player.Player) or \
                            isinstance(player, Player.Cardsharp):
                        self.remove_player(player)
                    break

    def check_winner(self):
        if self.dealer.full_points > 21:
            # all win
            print('Dealer are fall! All players who are in game - win!')

        else:
            pointlist = [player.full_points for player in self.players if 21 >= player.full_points
                         > self.dealer.full_points]
            pointlist.append(self.dealer.full_points)
            if max(pointlist) == self.dealer.full_points:
                for player in self.players:
                    if player.full_points == self.dealer.full_points:
                        print(MESSAGES.get('eq').format(player=player, points=player.full_points))
                print(MESSAGES.get('win').format(self.dealer.name, self.dealer.full_points))
            else:
                for player in self.players:
                    if player.full_points == max(pointlist):
                        if isinstance(player, Player.Player) or isinstance(player, Player.Cardsharp):
                            print('You are win!')
                        else:
                            print(MESSAGES.get('win').format(player.name, player.full_points))
                            time.sleep(1)
                    else:
                        if isinstance(player, Player.Player) or isinstance(player, Player.Cardsharp):
                            print('You are lose!')
                        else:
                            print(MESSAGES.get('lose').format(player.name, player.full_points))
                            time.sleep(1)

    def play_with_dealer(self):
        while self.dealer.ask_card():
            card = self.deck.get_card()
            self.dealer.take_card(card)
        self.dealer.print_cards()

    def clear_cards(self):
        self.dealer.cards.clear()
        for player in self.players:
            player.cards.clear()

    def start_game(self):
        message = MESSAGES.get('ask_start')
        if not self._ask_starting(message=message):
            exit(1)

        # generating data for starting
        self._launching()

        while True:

            # give first cards to the players
            self.first_descr()

            # print player cards after first deal
            self.player.print_cards()
            self.player.ace_value()

            if isinstance(self.player, Player.Cardsharp):
                message = MESSAGES.get('ability')
                check = input(message)
                if check == 'y':
                    card = self.deck.get_card()
                    self.player.ability(card)

            # ask players about cards
            self.ask_cards()

            self.play_with_dealer()

            self.check_winner()
            self.clear_cards()

            if not self._ask_starting(MESSAGES.get('rerun')):
                break


Game.asd = 10
