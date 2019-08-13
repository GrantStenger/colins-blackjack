from random import shuffle

class Deck:

    def __init__(self):

        self.num_decks = 1
        self.suits = ['s', 'h', 'c', 'd']
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        self.create_deck()
        self.shuffle_deck()

    def create_deck(self):

        # Create deck
        self.deck = []

        for deck in range(self.num_decks):
            for suit in self.suits:
                for value in self.values:
                    self.deck.append(value + suit)

    def shuffle_deck(self):
        shuffle(self.deck)

    def deal_card(self):
        card = self.deck.pop()
        return card

    def deal_ten(self):

        has_ten = False
        i = 0

        while not has_ten:
            card = self.deck[i]
            value = card[:-1]
            if value in ['10', 'J', 'Q', 'K']:
                has_ten = True
            else:
                i += 1

        card = self.deck.pop(i)

        return card
