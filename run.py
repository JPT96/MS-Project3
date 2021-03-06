
import random


class card:
    def __init__(self, value, suit):
        self.price = value
        self.value = ['A', '2', '3', '4', '5', '6',
                      '7', '8', '9', '10', 'J', 'Q', 'K'][value-1]
        self.suit = '♥♦♣♠'[suit]

    def show(self):
        print('┌───────┐')
        print(f'| {self.value:<2}    |')
        print('|       |')
        print(f'|   {self.suit}   |')
        print('|       |')
        print(f'|    {self.value:>2} |')
        print('└───────┘')

    def cost(self):
        if self.price >= 10:
            return 10
        elif self.price == 1:
            return 11
        return self.price


class Deck:
    def __init__(self):
        self.cards = []

    def full_deck(self):
        for i in range(1, 14):
            for j in range(4):
                self.cards.append(card(i, j))

    def draw(self, iteration):
        cards = []
        for i in range(iteration):
            card = random.choice(self.cards)
            self.cards.remove(card)
            cards.append(card)
        return cards

    def count(self):
        return len(self.cards)


class player_dealer:
    def __init__(self, dealer, deck):
        self.cards = []
        self.dealer = dealer
        self.deck = deck
        self.score = 0

    def hit(self):
        self.cards.extend(self.deck.draw(1))
        self.score_checker()
        if self.score > 21:
            return 1
        return 0

    def deal(self):
        self.cards.extend(self.deck.draw(2))
        self.score_checker()
        if self.score == 21:
            return 1
        return 0

    def score_checker(self):
        ace_counter = 0
        self.score = 0
        for card in self.cards:
            if card.cost() == 11:
                ace_counter += 1
            self.score += card.cost()

        while ace_counter != 0 and self.score > 21:
            ace_counter -= 1
            self.score -= 10
        return self.score

    def show(self):
        if self.dealer:
            print("Dealer's Cards")
        else:
            print("Player's Cards")

        for i in self.cards:
            i.show()

        print("Score: " + str(self.score))


class The_game:
    def __init__(self):
        self.deck = Deck()
        self.deck.full_deck()
        self.player = player_dealer(False, self.deck)
        self.dealer = player_dealer(True, self.deck)

    def round(self):
        p_status = self.player.deal()
        d_status = self.dealer.deal()

        self.player.show()

        if p_status == 1:
            print("Player got Blackjack! Congrats!")
            if d_status == 1:
                print("Dealer and Player got Blackjack! It's a push. (Tie)")
            return 1

        command = ""
        while command != "Hold":
            bust = 0
            command = input("Hit or Hold?:\n")

            if command == "Hit":
                bust = self.player.hit()
                self.player.show()
            if bust == 1:
                print("Player Busted, You're flat Broke!")
                return 1
        print("\n")
        self.dealer.show()
        if d_status == 1:
            print("The Dealer got BlackJack. Is he cheating?")
            return 1

        while self.dealer.score_checker() < 17:
            if self.dealer.hit() == 1:
                self.dealer.show()
                print("Dealer Bust. I guess he wasn't cheating after all. You win!")
                return 1
            self.dealer.show()

        if self.dealer.score_checker() == self.player.score_checker():
            print("It's a tie, Dealer wins by default")
        elif self.dealer.score_checker() > self.player.score_checker():
            print("dealer wins. Is it rigged?")
        elif self.dealer.score_checker() < self.player.score_checker():
            print("You did it You won! Take your win and run")


b = The_game()
b.round()
