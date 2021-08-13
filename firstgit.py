from random import randrange
import random 
import csv
#----------------------------------------------------------------#
students = []
score_report = {}
filename = "students.csv"
f = open(filename, "w", encoding="utf8", newline="")
writer = csv.writer(f)
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
    
    def taking_midterm(self, study_hours):
        luck = randrange(1,21)
        score = float(12.5 * study_hours) + luck
        if score > 100:
            score = 100
        print("{}'s score on the midterm is {}".format(self.name, score))
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
        student_score = student.taking_midterm(randrange(1,10))
        score_report[student.name] = float(student_score)
        print(score_report)

def class_average():
    scores = 0
    for key in score_report:
        x = score_report.get(key)
        scores = scores + x
    print("the class average is: ", round(scores / len(score_report), 3))

def report_bad():
    vape = random.choice(students)
    for i in students:
        if i == vape:
            print("student {}, follow me to the main office".format(i.name))

def report_good():
    all_scores = score_report.values()
    max_score = max(all_scores)
    highest_scorer = max(score_report, key = score_report.get) 
    print("Congratulations! {} got the highest score of".format(highest_scorer), max_score)      






#----------------------------------------------------------------#
soccer_player = Sports_Student("Messi")
math_student = Math_Student("Tao")
ms_2 = Math_Student("Euler")
football_player = Sports_Student("Metcalf")
midterm_result()
class_average()
report_bad()
report_good()
#----------------------------------------------------------------#
key_list = list(score_report.keys())
val_list = list(score_report.values())
print(key_list)
print(val_list)

            






