# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas
# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# #print(data)
# NATO_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(NATO_dict)
#
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# word = input("Enter a word: ").upper()
#
# output_codes = [NATO_dict[letter] for letter in word if letter in NATO_dict]
# print(output_codes)


print([{row.letter: row.code for (index, row) in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}[letter] for letter in input("Enter a word: ").upper()])