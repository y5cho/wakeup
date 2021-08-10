from random import randrange
import random 

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
            print("{} is not coming to school today for being {}".format(name, status))
        else:
            print("{} is here".format(name))

class Math_Student(Student):
    def __init__(self, name):
        Student.__init__(self, name, "wonderous", "good")
        students.append(self)
    
    def taking_midterm(self, study_hours):
        luck = randrange(1,21)
        score = float(12.5 * study_hours) + luck
        if score > 100:
            score = 100
        print("{}'s score on the midterm is {}".format(self.name, score))


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

ms_2.taking_midterm(6)        









