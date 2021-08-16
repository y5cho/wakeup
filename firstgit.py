from random import randrange
import random 
import csv
from typing import final
#----------------------------------------------------------------#
students = []
midterm_report = {}
final_report = {}
#----------------------------------------------------------------#
class Student:
    def __init__(self, name, mood, status):
        self.name = name 
        self.status = status 
        self.mood = mood
        if self.status != "good":
            print("{} is not coming to school today for being {}".format(name, status))
        else:
            print("{} is here".format(name))
        print("-"*50)
    
    def testing(self, study_hours):
        luck = randrange(1,21)
        score = float(12.5 * study_hours) + luck
        if score > 100:
            score = 100
        return score

class Math_Student(Student):
    def __init__(self, name):
        Student.__init__(self, name, "wonderous", "good")
        students.append(self)

class Sports_Student(Student):
    def __init__(self, name):
        Student.__init__(self, name, "hyped", "excused")
        students.append(self)

def midterm_result():
    for student in students:
        student_score = student.testing(randrange(1,10))
        midterm_report[student.name] = float(student_score)
        print("{}'s score on the midterm is {}".format(student.name, student_score))
    print("-"*50)

def final_result():
    for student in students:
        final_score = student.testing(randrange(1,10))
        final_report[student.name] = float(final_score)
        print("{}'s score on the final is {}".format(student.name, final_score))
    print("-"*50)


def class_average():
    midterm_scores = 0
    for key in midterm_report:
        x = midterm_report.get(key)
        midterm_scores = midterm_scores + x
    print("The class average on the midterm is: ", round(midterm_scores / len(midterm_report), 3))
    final_scores = 0
    for key in final_report:
        x = final_report.get(key)
        final_scores = final_scores + x
    print("The class average on the final is: ", round(final_scores / len(final_report), 3))

def class_grade():
    for student in midterm_report:
        m1 = midterm_report.get(student)
        for key in final_report:
            f1 = final_report.get(key)
        if int(m1 + f1) >= 180:
            class_grade = "A"
        elif int(m1 + f1) < 180 and int(m1 + f1) >= 160:
            class_grade = "B"
        else:
            class_grade = "C"
        print("{}'s final grade in the class: ".format(student), class_grade)

def report_bad():
    vape = random.choice(students)
    for i in students:
        if i == vape:
            print("student {}, follow me to the main office".format(i.name))

def report_good():
    all_scores = midterm_report.values()
    max_score = max(all_scores)
    highest_scorer = max(midterm_report, key = midterm_report.get) 
    print("Congratulations! {} got the highest score of".format(highest_scorer), max_score, " on the midterm")      






#----------------------------------------------------------------#
soccer_player = Sports_Student("Messi")
math_student = Math_Student("Tao")
ms_2 = Math_Student("Euler")
football_player = Sports_Student("Metcalf")
midterm_result()
final_result()
class_average()
class_grade()
#----------------------------------------------------------------#
key_list = list(midterm_report.keys())
val_list = list(midterm_report.values())
#print(" ".join(key_list))

title = "name   score".split("\t") 

with open('students.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(title)
    writer.writerows(zip(key_list , val_list))
            






