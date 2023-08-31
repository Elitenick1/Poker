from Card import Card
import random


class Deck:
    suits = ("hearts", "diamonds", "spades", "clubs")

    def __init__(self):
        self.deck = []
        for y in Deck.suits:
            for x in range(2, 15):
                self.deck.append(Card(y, x))

    def get_deck(self):
        return self.deck

    def print_deck(self):
        [print(i.name()) for i in self.deck]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        if (len(self.deck) == 0):
            return "None"
        else:
            top = self.deck[0]
            self.deck.remove(top)
            return top
