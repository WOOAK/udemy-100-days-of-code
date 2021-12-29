# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
n = 0
highest = student_scores[n]
for score in student_scores:
    if student_scores[n] > highest:
        highest = student_scores[n]
    n += 1

print(f"The highest score in the class is: {highest}.")



