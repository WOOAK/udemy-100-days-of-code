student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
grade = ''
for student in student_scores:
    if student_scores[student] >= 91 and student_scores[student] <= 100:
        grade = 'Outstanding'
    elif student_scores[student] >= 81:
        grade = 'Exceed Expectations'
    elif student_scores[student] >= 71:
        grade = 'Acceptable'
    else: 
        grade = 'Fail'
    
    student_grades[student] = grade

    

# 🚨 Don't change the code below 👇
print(student_grades)





