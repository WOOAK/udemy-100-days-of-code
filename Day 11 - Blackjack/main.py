############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play_option = input("Do you want to play Blackjack? Type 'y' or 'n'.")

def result(n1,n2):
    if n1 > n2:
        print("You win!")
    elif n1 == n2:
        print("Draw game!")
    else:
        print("You lose!")

def print_score(player_cards,player_total,dealer_cards,dealer_total,final):
    if final == False:
        print(f"Your cards: {player_cards},current score = {player_total}")
        print(f"Dealer's first card: {dealer_cards[0]}")
    else:
        print(f"Your final hand: {player_cards},final score: {player_total}")
        print(f"Computer final hand: {dealer_cards},final score: {dealer_total}")

def blackjack():
#first round
    Ace = 11
    end_game = False
    Burst = False
    player_cards = random.sample(cards,2)
    dealer_cards = random.sample(cards,2)


    player_total = sum(player_cards)
    dealer_total = sum(dealer_cards)
    print_score(player_cards,player_total,dealer_cards,dealer_total,False)
    #print(f"Your cards: {player_cards},current score = {player_total}")
    #print(f"Dealer's first card: {dealer_cards[0]}")
   
    if player_total == 21:
        print("You have BlackJack! You win!")
        return

    else:
        deal_card = input("Type 'y' to deal card, type 'n' to pass.")

    #deal card, computer choose to draw card if <21? 
    while deal_card == 'y' and end_game == False:
        new_card = random.choice(cards)
        player_cards.append(new_card)
        player_total = sum(player_cards)

        
        if player_total > 21:
            if Ace in player_cards:
                player_cards[player_cards.index(Ace)] = 1
                player_total = sum(player_cards)
            else:
                Burst = True
                end_game = True

        #to end game, either burst/blackjack/choose to not deal card
        if end_game == False:
            print_score(player_cards,player_total,dealer_cards,dealer_total,False)
            deal_card = input("Type 'y' to deal card, type 'n' to pass.")

    #increase dealer'schance to win (put a specific level)

    ignore_result = False
    while dealer_total < 17:
        new_card = random.choice(cards)
        dealer_cards.append(new_card)
        dealer_total = sum(dealer_cards)
    
        if dealer_total > 21:
            if Ace in dealer_cards:
                dealer_cards[dealer_cards.index(Ace)] = 1
                dealer_total = sum(dealer_cards)
            else:
                ignore_result = True
    
    print_score(player_cards,player_total,dealer_cards,dealer_total,True)

    if Burst == True:
        print("You burst and lose")
    elif ignore_result == True:
        print("You win!")
    else:
        result(player_total,dealer_total)

if play_option == 'y':
    blackjack()






##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

