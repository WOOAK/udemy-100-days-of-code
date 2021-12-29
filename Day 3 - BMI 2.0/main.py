# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = weight / (height**2)
BMI_round = round(BMI)
#tier
if BMI_round < 18.5:
  status = 'underweight'
elif BMI_round < 25:
  status = 'normal weight'
elif BMI_round < 30:
  status = 'slightly overweight'
elif BMI_round < 35:
  status = 'obese'
else:
  status = 'clinically obese'

print(f"Your BMI is {BMI_round}, you are {status}.")

