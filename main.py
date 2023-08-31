from Deck import Deck
from Hand import Hand
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

if __name__ == '__main__':
    hand1 = Hand()
    hand2 = Hand()
    hand3 = Hand()
    hand4 = Hand()
    poker_game = (hand1, hand2, hand3, hand4)

    hands = [hand1, hand2, hand3, hand4]

    deck = Deck()
    deck.shuffle()

    for i in range(len(poker_game) * 5):
        poker_game[i % len(poker_game)].add_card(deck.deal_card())

    poker_game[0].print_hand()
    print()
    poker_game[1].print_hand()
    print()
    poker_game[2].print_hand()
    print()
    poker_game[3].print_hand()
    print()

    for i in range(len(poker_game)):
        winner = 0
        for y in range(len(poker_game)):
            if not i == y:
                if poker_game[i].compare(poker_game[y]) == 1:
                    winner += 1
            if winner == len(poker_game) - 1:
                print("winning hand")
                poker_game[i].print_hand()
                break

    # testing_deck = Deck()
    # testing_deck.print_deck()
    # testing_deck.shuffle()


def make_row(im1, im2, im3, im4, im5):
    row = Image.new('RGB', (im1.width * 6, im1.height))
    row.paste(im1, (0, 0))
    row.paste(im2, (im1.height, 0))
    row.paste(im3, (im1.height + im2.height, 0))
    row.paste(im4, (im1.height + im2.height + im3.height, 0))
    row.paste(im5, (im1.height + im2.height + im3.height + im4.height, 0))
    return row


def make_column(im1, im2, im3, im4):
    column = Image.new('RGB', (im1.width * 6, im1.height))
    column.paste(im1, (0, 0))
    column.paste(im2, (0, im1.width))
    column.paste(im3, (0, im1.width + im2.width))
    column.paste(im4, (0, im1.width + im2.width + im3.width))
    return column


row1 = make_row(Image.open("cards/" + poker_game[0].get_hand()[0].image_file_name()),
                Image.open("cards/" + poker_game[0].get_hand()[1].image_file_name()),
                Image.open("cards/" + poker_game[0].get_hand()[2].image_file_name()),
                Image.open("cards/" + poker_game[0].get_hand()[3].image_file_name()),
                Image.open("cards/" + poker_game[0].get_hand()[4].image_file_name()))
row2 = make_row(Image.open("cards/" + poker_game[1].get_hand()[0].image_file_name()),
                Image.open("cards/" + poker_game[1].get_hand()[1].image_file_name()),
                Image.open("cards/" + poker_game[1].get_hand()[2].image_file_name()),
                Image.open("cards/" + poker_game[1].get_hand()[3].image_file_name()),
                Image.open("cards/" + poker_game[1].get_hand()[4].image_file_name()))
row3 = make_row(Image.open("cards/" + poker_game[2].get_hand()[0].image_file_name()),
                Image.open("cards/" + poker_game[2].get_hand()[1].image_file_name()),
                Image.open("cards/" + poker_game[2].get_hand()[2].image_file_name()),
                Image.open("cards/" + poker_game[2].get_hand()[3].image_file_name()),
                Image.open("cards/" + poker_game[2].get_hand()[4].image_file_name()))
row4 = make_row(Image.open("cards/" + poker_game[3].get_hand()[0].image_file_name()),
                Image.open("cards/" + poker_game[3].get_hand()[1].image_file_name()),
                Image.open("cards/" + poker_game[3].get_hand()[2].image_file_name()),
                Image.open("cards/" + poker_game[3].get_hand()[3].image_file_name()),
                Image.open("cards/" + poker_game[3].get_hand()[4].image_file_name()))

img = make_column(row1, row2, row3, row4)

d = ImageDraw.Draw(img)
myFont = ImageFont.truetype('Arial', 15)

if (poker_game.index(winner) == 0):
    d.text((img.width - 190, 90), "Winner!", font=myFont, fill=(255, 0, 0))
if (poker_game.index(winner) == 1):
    d.text((img.width - 190, 190), "Winner!", font=myFont, fill=(255, 0, 0))
if (poker_game.index(winner) == 2):
    d.text((img.width - 190, 290), "Winner!", font=myFont, fill=(255, 0, 0))
if (poker_game.index(winner) == 3):
    d.text((img.width - 190, 390), "Winner!", font=myFont, fill=(255, 0, 0))

img.show()