#task 3 Deep dive 


students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]


for i in range(len(grades)):
    if grades[i] < 80:
        print(students[i], grades[i], activities[i])