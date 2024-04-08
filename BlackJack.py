import random
import time

# Define the kinds of cards and their numbers
kind = ("heart", "diamond", "spade", "club")  # Define the suits
number = ("ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king")  # Define the card values

# Create the deck of cards
deck = [[k, n] for k in kind for n in number]

def Winning_Conditions(player, computer):
    """
    Function to determine the winner of the game based on the final score.
    """
    # Display the final score
    last_Score = f'''------FINAL SCORE-----
|                    |
|        {player}-{computer}       |
|                    |
----------------------'''
    # Print the score gradually
    for char in last_Score:
        time.sleep(0.01)
        print(char, end="")
    
    # Determine the winner based on the scores
    if player > computer:
        time.sleep(0.5)
        print("\n       YOU WIN!")
    elif computer > player:
        time.sleep(0.5)
        print("\n       PC WINS!")
    else:
        time.sleep(0.5)
        print("\n       DRAW")

def Player_Card_Value_Check(sum, cards, pos):
    """
    Function to calculate the value of the player's cards.
    """
    if sum == 0:
        # Calculate the sum of the player's cards
        for card in cards:
            if card[1].isdigit():
                sum += int(card[pos])
            elif card[1] == "ace":
                # If an Ace is encountered, prompt the player to choose its value
                for card in cards:
                    print(card, end="")
                while True:
                    one_or_ten = input("\n\nTurn Ace to 1 or 11: ")
                    if one_or_ten == "1" or one_or_ten == "11":
                        card[1] = one_or_ten
                        sum += int(one_or_ten)
                        break
            else:
                sum += 10
        return sum
    else:
        if cards[pos][pos].isdigit():
            sum += int(cards[pos][pos])
        elif cards[pos][pos] == "ace":
            # Prompt the player to choose the value of the Ace
            while True:
                one_or_ten = input("\n\nTurn Ace to 1 or 11: ")
                if one_or_ten == "1" or one_or_ten == "11":
                    cards[pos][pos] = one_or_ten
                    sum += int(one_or_ten)
                    break
        else:
            sum += 10
        return sum


def PC_Card_Value_Check(sum, cards, pos, p_sum):
    """
    Function to calculate the value of the computer's cards.
    """
    if sum == 0:
        # Calculate the sum of the computer's cards
        for card in cards:
            if card[pos].isdigit():
                sum += int(card[pos])
            elif card[pos] == "ace":
                # If an Ace is encountered, assign its value based on the current sum
                if 21 - sum <= 9:
                    card[pos] = 1
                    sum += 1
                    time.sleep(1)
                    print("\nAce has been made into 1\n")
                    for card in cards:
                        time.sleep(1)
                        print(card, end="")
                else:
                    card[pos] = 11
                    sum += 11
                    time.sleep(1)
                    print("\nAce has been made into 11\n")
                    for card in cards:
                        time.sleep(1)
                        print(card, end="")
            else:
                sum += 10
        return sum
    else:
        # Adjust the value of Ace if necessary
        if cards[pos][pos].isdigit():
            sum += int(cards[pos][pos])
        elif cards[pos][pos] == "ace":
            print(cards)
            if 21 - sum <= 9:
                cards[pos][pos] = 1
                sum += 1
                print(cards)
            else:
                cards[pos][pos] = 10
                sum += 10
                print(cards)
        else:
            sum += 10
        return sum

def computer_turn(player_sum):
    """
    Function to execute the computer's turn.
    """
    deck_list = list(deck)
    computer_cards = []
    computer_sum = 0
    # Deal two initial cards to the computer
    computer_cards.append(random.choice(deck_list))
    deck_list.remove(computer_cards[0])
    computer_cards.append(random.choice(deck_list))
    deck_list.remove(computer_cards[1])
    time.sleep(1)
    print("\nStarting hand for computer's turn:")
    for card in computer_cards:
        time.sleep(1)
        print(card, end="")
    # Calculate the sum of computer's cards
    computer_sum = PC_Card_Value_Check(computer_sum, computer_cards, 1, player_sum)
    time.sleep(1)
    print(f"\nPC SUM: {computer_sum}")
    while True:
        # If the computer's sum is less than player's sum and less than 18, draw another card
        if computer_sum < player_sum and computer_sum < 18:
            time.sleep(1)
            print("PC draws another card")
            computer_cards.append(random.choice(deck_list))
            deck_list.remove(computer_cards[-1])
            # Calculate the sum after drawing another card
            computer_sum = PC_Card_Value_Check(computer_sum, computer_cards, -1, player_sum)
            time.sleep(1)
            for card in computer_cards:
                time.sleep(1)
                print(card, end="")
        else:
            break
    # Check if computer's sum exceeds 21
    if computer_sum >= 22:
        time.sleep(1)
        print("\nPC LOST! YOU WIN!")
        exit()
    time.sleep(1)
    print("\nPC STAYED")
    Winning_Conditions(player_sum, computer_sum)

def Player_Turn():
    """
    Function to execute the player's turn.
    """
    deck_list = list(deck)
    player_cards = []
    player_sum = 0
    # Deal two initial cards to the player
    player_cards.append(random.choice(deck_list))
    deck_list.remove(player_cards[0])
    player_cards.append(random.choice(deck_list))
    deck_list.remove(player_cards[1])
    print("Your first 2 cards are: ")
    # Calculate the sum of player's cards
    player_sum = Player_Card_Value_Check(player_sum, player_cards, 1)
    time.sleep(1)
    for card in player_cards:
        print(card, end="")
        time.sleep(1)
    # Check if player has Blackjack
    if player_sum == 21:
        print("YOU WON!")
        exit()
    while True:
        print(f"\nYour Current Score: {player_sum}")
        while True:
            time.sleep(1)
            player_draw = input("\nDraw/Stay(D/S): ")
            if player_draw.isalpha() and player_draw.lower() in ("d", "s"):
                break
        # If player chooses to draw
        if player_draw.lower() == "d":
            time.sleep(1)
            print("\nOne extra card has been dealt!\n")
            player_cards.append(random.choice(deck_list))
            deck_list.remove(player_cards[-1])
            # Calculate the sum after drawing another card
            for card in player_cards:
                time.sleep(1)
                print(card, end="")
            player_sum = Player_Card_Value_Check(player_sum, player_cards, -1)
            if player_sum == 21:
                print("\n\n-----YOU WON!-----")
                break
            elif player_sum > 21:
                print(f"\n\n-----You lost!-----\nYour total score was {player_sum}")
                break
        else:
            # If player chooses to stay, proceed with computer's turn
            time.sleep(1)
            print(f"Total Score: {player_sum}")
            computer_turn(player_sum)
            break
            
def intro():
    """
    Function to display the introduction of the game.
    """
    introtext = '''
Welcome to the Blackjack Game!

In this game, you will play against the computer to see who can get closer to 21 without going over.
You will be dealt two cards initially, and you can choose to 'draw' additional cards to increase your total score.
Be careful not to exceed 21, or you'll bust and lose the game!
If you're satisfied with your hand, choose to 'stay' and let the computer take its turn.
Let's see who can come out on top and win this round of Blackjack!
'''
    for char in introtext:
        time.sleep(0.01)
        print(char,end="")
    return 

def main():
    """
    Main function to start the game.
    """
    intro()
    Player_Turn()

main()
