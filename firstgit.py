from random import randrange
import random 
start = randrange(1,5)
end = randrange(5,11)
students = []

'''
for student in range(start, end):
    absent.append(student)
'''
class Student:
    def __init__(self, name, mood, status):
        self.name = name 
        self.status = status 
        self.mood = mood
        if self.status != "good":
            print("{} is not coming to school today for being {}".format(self.name, status))
        else:
            print("{} is here".format(self.name))

class Math_Student(Student):
    def __init__(self, name):
        Student.__init__(self, name, "wonderous", "good")
        students.append(self)

class Sports_Student(Student):
    def __init__(self, name):
        Student.__init__(self, name, "hyped", "excused")
        students.append(self)

soccer_player = Sports_Student("Messi")
math_student = Math_Student("Tao")
ms_2 = Math_Student("Euler")
football_player = Sports_Student("Metcalf")

vape = random.choice(students)
for i in students:
    if i == vape:
        print("student {}, follow me to the main office".format(i.name))





'''
vape = [randrange(0,15)]
for student in range(1,11):
    if student in absent:
        continue 
    elif student in vape:
        print("{}th student, follow me to the main office".format(student))
        break
    print("{}th student is here".format(student))

'''





