from random import randrange
absent = [3, 7]
vape = [randrange(0,15)]

for student in range(1,11):
    if student in absent:
        continue 
    elif student in vape:
        print("{}th student, follow me to the main office".format(student))
        break
    print("{}th student is here".format(student))