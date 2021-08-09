from random import randrange
start = randrange(1,5)
end = randrange(5,11)
absent = []

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
            absent.append(self.name)
            print("{} is not coming to school today due to {}".format(self.name, status))
        else:
            print("{} is here".format(self.name))

student1 = Student("Kim", "tired", "illness")

class Math_Student(Student):
    def __init__(self, name):
        Student.__init__(self, name, "wonderous", "good")

class Sports_Student(Student):
    def __init__(self, name):
        Student.__init__(self, name, "hyped", "excused")

soccer_player = Sports_Student("Messi")
math_student = Math_Student("Tao")
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





