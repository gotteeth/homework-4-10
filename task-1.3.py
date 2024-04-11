#task 3 



grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

under = [grade if grade >= 80 else "Fail" for grade in grades ]
print("updated grades", under)