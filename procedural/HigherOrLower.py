import random


SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4','5', '6', '7', '8', '9', '10',
              'Jack', 'Queen', 'King')

NCARDS = 8

#pass in a deck and this function returns a random card
def get_card(deck_list_in):
    this_card = deck_list_in.pop()
    return this_card

#pass in a deck and this function returns a shuffled deck; a copy of the pass in deck
def shuffle(deck_list_in):
    deck_list_out = deck_list_in.copy()
    random.shuffle(deck_list_out)
    return deck_list_out

#main code
print('Welcom to Higher or Lower')
print('You have to choose whether the next card to be shown will be higher or lower than the current card')
print('Getting it right adds 20; losing subtract 15 points')
print('You have 15 points to start.')
print()

starting_deck_list = []

for suit in SUIT_TUPLE:
    for this_value, rank in enumerate(RANK_TUPLE):
        card_dict = {'rank':rank, 'suit':suit, 'value':this_value +1}
        starting_deck_list.append(card_dict)

score = 50

while True:
    print()
    game_deck_list = shuffle(starting_deck_list)
    current_card_dict = get_card(game_deck_list)
    current_card_value = current_card_dict.get('value')
    current_card_rank = current_card_dict.get('rank')
    current_card_suit = current_card_dict.get('suit')
    print(f'Starting card is: {current_card_rank} of {current_card_suit} ')
    print()

    for card_number in range(0, NCARDS):
        answer = input(f'Will the next card be higher or lower than {current_card_rank} of {current_card_suit}? (enter h or l): ')
        answer = answer.casefold()
        print()
        next_card_dict = get_card(game_deck_list)
        next_card_rank = next_card_dict.get('rank')
        next_card_suit = next_card_dict.get('suit')
        next_card_value = next_card_dict.get('value')
        print(f'Next card is: {next_card_rank} of {next_card_suit}')

        if answer == 'h':
            if next_card_value > current_card_value:
                print('You got it right, it was higher')
                score += 20
            else:
                print('Sorry, it was not higher')
                score -= 15

        elif answer == 'l':
            if next_card_value < current_card_value:
                score += 20
                print('You got it right, it was lower')
            else:
                print('Sorry, it was not lower')
                score -= 15

        print('Your score is: ', score)
        print()
        current_card_rank = next_card_rank
        current_card_value = next_card_value

    go_again = input('To play again, press ENTER, or "q" to quit: ')
    if go_again == 'q':
        break

print('OK bye')

