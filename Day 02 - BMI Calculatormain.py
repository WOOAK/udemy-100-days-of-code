# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_num = float(height)
weight_num = int(weight)
print(height_num**2)
BMI = weight_num / (height_num**2)
print((BMI))
