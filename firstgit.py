absent = [3, 7]

for student in range(1,11):
    if student in absent:
        continue 
    print("{}th student is here".format(student))