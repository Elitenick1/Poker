class Card(object):
    card_names = ["Deuce", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King",
                  "Ace"]

    def __init__(self, suit: str, value: int):
        self.suit = suit
        self.value = value

    def name(self):
        return f"{Card.card_names[self.value - 2]}_of_{self.suit}"

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    def get_name(self):
        return self.name

    def image_file_name(self):
        if self.value < 11:

            return f"{self.value}_of_{self.suit}.png"
        else:
            return f"{Card.card_names[self.value - 2].lower()}_of_{self.suit}.png"



