
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]






students_approved = []

for i in range(len(grades)):
    if grades[i] >= 80:
        students_approved.append(students[i])
    print(students_approved)