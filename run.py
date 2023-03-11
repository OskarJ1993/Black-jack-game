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
}

cards_suits = ("\u2663", "\u2660", "\u2666", "\u2665")

deck_of_cards = []
player_hand = []
computer_hand = []
computer_total = 0
player_total = 0
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
    global player_total
    global computer_total
    
    while True:
        print("------------------------")
        choice = input(f"Do you want one more card?\n Press Y if you want one more or N if not. ")
        try:
            if choice.lower() == "y":
                player_hand.append(deck_of_cards.pop(0))
            player_cards = [f"{card[1]}{card[0]}" for card in player_hand]
            if player_total > 21:
                print(f"{player_name} got {player_cards} cards\n Computer wins as {player_name} exceeded 21")
                return False
            if computer_total < 12:
                computer_hand.append(deck_of_cards.pop(0))
            computer_cards = [f"{card[1]}{card[0]}" for card in computer_hand]
            computer_cards_string = " ".join(computer_cards)
            if choice.lower() == "y":
                print(f" {player_name} got {player_cards} cards\n Computer got {computer_cards_string}")
                continue
            elif choice.lower() == "n":
                return False
            else:
                raise ValueError("Invalid input. Please enter 'y' or 'n'.")
        except ValueError as e:
            print(e)
            continue










def who_wins():
    """
    Who wins function that convert every card to a number and decides who wins.
    """
    global player_total
    global computer_total

    for card in player_hand:
        card_value = card_values[card[1]]
        player_total += card_value

    for card in computer_hand:
        card_value = card_values[card[1]]
        computer_total += card_value

    print(player_total)
    print(computer_total)

    if player_total == 21:
        print(f"BlackJack!! {player_name} wins")
        print("------------------------")
    elif computer_total == 21:
        print("Sorry, the Computer got BlackJack!")
        print("------------------------")
    elif player_total < 21 and computer_total > 21:
        print(f"You Win {player_name}!")
        print("------------------------")
    elif player_total > 21 and computer_total < 20:
        print(f"{player_name} you lost.")
        print("------------------------")
    elif player_total == computer_total and player_total <= 21:
        print("Its a draw!")
        print("------------------------")
    elif player_total > 21 and computer_total <= 21:
        print("Sorry you lost.")
        print("------------------------")
    elif player_total <= 21 and computer_total > 21:
        print(f"You Win {player_name}!")
        print("------------------------")
    elif player_total > computer_total and player_total <= 21:
        print(f"You Win {player_name}!")
        print("------------------------")
    elif player_total < computer_total and computer_total <= 21:
        print("Sorry you lost.")
        print("------------------------")



def restart_game():
    """
    Simple restart function after the game is done.
    """
    global player_total
    global computer_total
    restart = input("Do you want to play agian? press y or n: ")
    if restart == "y":
        computer_total = 0
        player_total = 0
        main()
    else:
        sys.exit("You exited the game")



def main():
    shuffle_cards()
    start_game()
    while more_cards_choice():
        print(f"{player_name} got {player_hand} cards\n Computer got {computer_hand}")
    print("------------------------")
    who_wins()
    print("------------------------")
    restart_game()



print("Welcome to the game of Blackjack!")
print(" __________         __________      ")
print("|A         |       |K         |     ")
print("|♡         |       |♣         |     ")
print("|          |       |          |     ")
print("|    ♡     |       |    ♣     |     ")
print("|          |       |          |     ")
print("|        ♡ |       |        ♣ |     ")
print("|         A|       |         K|     ")
print("|__________|       |__________|     \n")
player_name = input("Please enter your name: ")
print("------------------------")
main()