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


def more_cards_choice():
    """
    This function gives the player a choice to get one more card or wants to stay
    """
    player_cards = []
    computer_cards = []
    while True:
        print("------------------------")
        choice = input(f"Do you want one more card?\n Press Y if you want one more or N if not. ")
        if choice == "y":
            player_hand.append(deck_of_cards.pop(0))
            computer_hand.append(deck_of_cards.pop(0))
            player_cards = [f"{card[1]}{card[0]}" for card in player_hand]
            computer_cards = [f"{card[1]}{card[0]}" for card in computer_hand]
            return True
        elif choice == "n":
            return False
    player_cards_str = ' '.join(player_cards)
    computer_cards_str = ' '.join(computer_cards)


def who_wins():
    """
    Who wins function that convert every card to a number and decides who wins.
    """
    card_values = {
        "Ace": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "Jack": 10,
        "queen": 10,
        "King": 10,
        "\u2663": 0,
        "\u2660": 0,
        "\u2666": 0,
        "\u2665": 0,
    }


    player_total = 0
    for card in player_hand:
        card_value = card_values[card[0]]
        player_total += card_value

    computer_total = 0
    for card in computer_hand:
        card_value = card_values[card[0]]
        computer_total += card_value

    if player_total == 21:
        print(f"BlackJack!! {player_name} wins")
        print("------------------------")
    elif computer_total == 21:
        print("Sorry, the Computer got BlackJack!")
        print("------------------------")
    elif player_total <= 20 and computer_total >= 20:
        print(f"You Win {player_name}!")
        print("------------------------")
    elif player_total >= 20 and computer_total <= 20:
        print("Sorry you lost.")
        print("------------------------")
    elif player_total == computer_total and player_total <= 21:
        print("Its a draw!")
        print("------------------------")
    elif player_total and computer_total > 21:
        print("Both Lose!")
        print("------------------------")


def restart_game():
    """
    Simple restart function after the game is done.
    """
    restart = input("Do you want to play agian? press y")
    if restart == "y":
        main()
    else:
        sys.exit("You exited the game")