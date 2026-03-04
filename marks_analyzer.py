# Student Marks Analyzer

# Taking input from user
name = input("Enter student name: ")
marks = []

# Taking 3 subject marks
for i in range(3):
    mark = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

# Calculations
total = sum(marks)
average = total / len(marks)

# Grade logic
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "D"

# Output
print("\n----- Result -----")
print("Student Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)