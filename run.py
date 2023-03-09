import random
import keyboard
import sys


cards_value = [
    "Ace",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "Jack",
    "queen",
    "King",
]

cards_suits = ("\u2663", "\u2660", "\u2666", "\u2665")

deck_of_cards = []
player_hand = []
computer_hand = []
player_name = ""

def shuffle_cards():
    """
    Function that shuffle cards to deck_of_cards randomly.
    """
    for suits in cards_suits:
        for value in cards_value:
            card = (suits, value)
            deck_of_cards.append(card)
    random.shuffle(deck_of_cards)
    return deck_of_cards

def start_game():
    """
    Start game function that gives player and computer 2 random cards each to begin with.
    """
    player_hand.clear()
    computer_hand.clear()
    for _ in range(2):
        player_hand.append(deck_of_cards.pop(0))
        computer_hand.append(deck_of_cards.pop(0))
        player_cards = []
    for card in player_hand:
        card_string = f"{card[1]}{card[0]}"
        player_cards.append(card_string)
    player_cards_str = ' '.join(player_cards)

    computer_cards = []
    for card in computer_hand:
        card_string = f"{card[1]}{card[0]}"
        computer_cards.append(card_string)
    computer_cards_str = ' '.join(computer_cards)

    print(f"You got {player_cards_str} cards\n Computer got {computer_cards_str}")
    return player_cards_str, computer_cards_str  