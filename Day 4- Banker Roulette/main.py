# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
#print(names)
#print(names[0])
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
#without choice function
pax = len(names)
the_one = random.randint(0, pax-1)
print(names[the_one] + " is going to buy the meal today!")
#choice funtion
#the_one = random.choice(names)
#print(the_one + " is going to buy the meal today!")
