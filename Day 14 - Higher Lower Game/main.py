from game_data import data
from random import sample,randint
from art import logo,vs
from replit import clear

def print_info(Name,job,place,ind):

    sentence = f"{Name}, a {job}, from {place}"
    if ind == 'A':
        print("Compare A: " + sentence)
    else:
        print("Against B: " + sentence)


def assign_value(dict):

    name = dict['name']
    job = dict['description']
    place = dict['country']
    fans = dict['follower_count']
    return name,job,place,fans

def check_winner(fansA,fansB):
    winner = ''
    if fansA > fansB:
        winner = 'A'
    else:
        winner = 'B'
    return winner

def next_chosen():
    index = randint(1,number_of_data)
    return index

number_of_data = len(data)
def game():
    
    
    #starting data
    index = sample(range(number_of_data),2)
    dict1 = data[index[0]]
    dict2 = data[index[1]]
    
    score = 0
    option = ''
    winner = option
    while winner == option:
        clear()
        print(logo)
        if score != 0:
            print(f"You are right, current score is {score}.")
        name,job,place,fans= assign_value(dict1)
        print_info(name,job,place,'A')
        fansA = fans
        print(vs)
        name,job,place,fans = assign_value(dict2)
        print_info(name,job,place,'B')
        fansB = fans
        winner = check_winner(fansA,fansB)
        option = input("Who has more followers? Type A or B")
        if winner != option:
            clear()
            print(f"Sorry wrong, your final score is {score}.")
            return
        score += 1
        dict1 = dict2
        while dict1 == dict2:
            index = next_chosen()
            dict2 = data[index]

game()





