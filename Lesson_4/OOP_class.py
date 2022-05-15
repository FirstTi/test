class Student:
    demotivated = False

    def __init__(self, tired, progress):
        self.tired = tired
        self.progress = progress


    def study(self):
        if self.tired < 85:
            self.tired = self.tired + 15
        else:
            self.tired = 100

        self.progress += 10

    def relax(self):
        if self.tired > 5:
            self.tired -= 5
        else:
            self.tired = 0

    def is_done(self):
        if self.progress >= 100:
            print("Студет выпустился")
        else:
            print("Студент не доучился")

    def demotivated(self):
        if self.tired > 100:
            return True
        else:
            return False
        # return True if self.tired > 100 else False
        # result = self.tired > 100 ## return self.tired > 100
        # return result

student_ilya = Student(15, 10) #  аргументы передаются позиционно
student_dima = Student(progress=5, tired=20)  # аргументы задаются именованно



print(student_ilya.tired)
print(student_ilya.progress)

student_ilya.study()
student_ilya.study()
student_dima.study()

print(student_ilya.tired)
print(student_ilya.progress)
print("*" * 15)
print(student_dima.tired)
print(student_dima.progress)


student_ilya.name = "Ilya"
print(student_ilya.name)
