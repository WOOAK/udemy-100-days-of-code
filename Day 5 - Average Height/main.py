# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height = 0
pax = 0
for height in student_heights:
  total_height += student_heights[pax]
  pax += 1
  print(total_height)
  print(pax)
print(round(total_height/pax))


