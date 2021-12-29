rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
ans=int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if ans <=0 or ans > 2:
  print("Invalid number, you lose")
else:
  style = [rock,paper,scissors]
  print(style[ans])
  print("Computer chose:")
  comp = random.randint(0,2)
  print(style[comp])
  row1 = ["draw","lose","win"]
  row2 = ["win","draw","lose"]
  row3 = ["lose","win","draw"]
  map = [row1,row2,row3]
  result = map[ans][comp]
  print("You " + result + ".")