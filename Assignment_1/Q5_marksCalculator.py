# Program to calculate total,average,percentage and grade

marks = []

for i in range(1,7):
    m = float(input(f"Enter marks for subjects{i}: "))
    marks.append(m)

total = sum(marks)
average = total/6
percentage = (total/600)*100

print("Total marks: " , total)
print("Average marks: " , average)
print("Percentage: " , percentage)

if percentage >= 85:
    grade = "Distinction"
elif percentage >= 70:
    grade = "First Division"
elif percentage >= 55:
    grade = "Second Division"
elif percentage >= 45:
    grade = "Third Division"
else:
    grade = "Fail"

print("Grade: " , grade)