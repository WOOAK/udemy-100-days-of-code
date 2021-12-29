#Step 1
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
letter_list = list(chosen_word)
print(letter_list)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter:")
guess = guess.lower()
print(guess)
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#print(len(letter_list))
#for i in range(len(letter_list)):
#  if guess == letter_list[i]:
#    print("Right")
#  else:
#    print("Wrong")
#Instructor, no need count length and no need letter list
for letter in chosen_word:
  if letter == guess:
    print("Right")
  else:
    print("Wrong")
