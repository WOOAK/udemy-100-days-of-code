from random import randint
from art import logo

def set_attempt(level):
    if level == "hard":
        attempt = 5
    else:
        attempt = 10
    return attempt

def set_level():
    level = input("Type easy or hard.")
    if level not in difficulty:
        print("Invalid input")
        set_level()
    else:
        return level

def print_info(ind,attempt):
    if ind == 'W':
        print(f"You get it, the number is {number}.")
    elif ind == 'L':
        print("Too low.")
        print(f"Guess again.\nYou have {attempt} attempts.")
    elif ind == 'H':
        print("Too high.")
        print(f"Guess again.\nYou have {attempt} attempts.")
    else:
        print("You've run out of guesses, you lose")

def compare(guess):
    
    ind = ""
    if guess == number:
        ind = 'W'
    elif guess < number:
        ind = 'L'
    else:
        ind = 'H'
    return ind

def check_lose(attempt):
    lose = False
    if attempt == 0:
        lose = True
    return lose

def game():
    end_game = False
    level = set_level()
    attempt = set_attempt(level)
    print(f"You have {attempt} attempts.")
    while not end_game:
        
        guess = int(input("Make a guess: "))
        ind = compare(guess)
        if ind != 'W':
            attempt -= 1
            lose = check_lose(attempt)
            if lose:
                ind = 'F'
                end_game = True
        else:
            end_game = True
        print_info(ind,attempt)

print(logo)       
print("Welcome to the number guessing game.")
print("I'm thinking of a number between 1 and 100.")
number = randint(1,100)
#print(number)
difficulty = ["easy","hard"]
game()




