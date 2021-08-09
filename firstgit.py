from random import randrange
start = randrange(1,5)
end = randrange(5,11)
absent = []

'''
for student in range(start, end):
    absent.append(student)
'''
class Student:
    def __init__(self, name, status):
        self.name = name 
        self.status = status 
        if self.status != "good":
            absent.append(self.name)
            print("{} is not coming to school today due to {}".format(self.name, status))

student1 = Student("Kim", "illness")
print(absent)
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





