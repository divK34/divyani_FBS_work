from abc import ABC, abstractmethod

class Student(ABC):
    def __init__(self, sid=0, sname="not given", age=0, per=0):
        self.sid = sid
        self.sname = sname
        self.age = age
        self.percentage = per

    def display(self):
        print("Student id =", self.sid)
        print("Student name =", self.sname)
        print("Student age =", self.age)
        print("Student percentage =", self.percentage)

    @abstractmethod
    def cal_rank(self):
        pass

    def __str__(self):
        return f"Student id = {self.sid}\nStudent name = {self.sname}\nStudent age = {self.age}\nStudent percentage = {self.percentage}"
    
class EnggStudent(Student):
    def __init__(self, sid=0, sname="not given", age=0, per=0, branch="not given", im=0):
        super().__init__(sid, sname, age, per)
        self.branch = branch
        self.internal_marks = im

    def display(self):
        super().display()
        print("Studying branch =", self.branch)
        print("Internal marks =", self.internal_marks)

    def cal_rank(self):
        pass

    def __str__(self):
        return f"Student id = {self.sid}\nStudent name = {self.sname}\nStudent age = {self.age}\nStudent percentage = {self.percentage}\nBranch = {self.branch}\nInternal marks = {self.internal_marks}"
    
class MedStudent(Student):
    def __init__(self, sid=0, sname="not given", age=0, per=0, spe="not given", moi=0):
        super().__init__(sid, sname, age, per)
        self.specialization = spe
        self.marks_of_internship = moi

    def display(self):
        super().display()
        print("Specialization =", self.specialization)
        print("Marks of internship =", self.marks_of_internship)

    def cal_rank(self):
        pass

    def __str__(self):
        return f"Student id = {self.sid}\nStudent name = {self.sname}\nStudent age = {self.age}\nStudent percentage = {self.percentage}\nSpecialization = {self.specialization}\nMarks of internship = {self.marks_of_internship}"   
    
class College:
    def __init__(self):
        self.student_list = []

    def add_student(self):
        print("1. Enggineering student\n2. Medical student")
        ch = int(input("Enter you choice = "))

        if ch==1:
            sid = int(input("Enter the id = "))
            sname = input("Enter the name = ")
            age = int(input("Enter the age = "))
            per = float(input("Enter the percentage = "))
            branch = input("Enter the branch name = ")
            im = float(input("Enter the internal marks = "))
            self.student_list.append(EnggStudent(sid,sname,age,per,branch,im))

        elif ch==2:
            sid = int(input("Enter the id = "))
            sname = input("Enter the name = ")
            age = int(input("Enter the age = "))
            per = float(input("Enter the percentage = "))
            spe = input("Enter the Specialization = ")
            moi = float(input("Enter the marks of internship = "))
            self.student_list.append(EnggStudent(sid,sname,age,per,spe,moi))

        else:
            print("Incorrect choice")

    def search_student(self):
        sid = int(input("Enter the id of student you want to search = "))

        for s in self.student_list:
            if s.sid==sid:
                s.display()
                break
        else:
            print("Incorrect input!!")
    
    def remove_student(self):
        sid = int(input("Enter the id of student you want to remove = "))

        for s in self.student_list:
            if s.sid==sid:
                self.student_list.remove(s)
                break
        else:
            print("Incorrect input!!")
    
    def __str__(self):
        for s in self.student_list:
            return f"{s}"
    
if __name__ == "__main__":
    cl = College()

    while True:
        print("1. Add a student\n2. Get a student\n3. Remove a student\n4. Display all student\n0. To exit")
        ch = int(input("Enter your choice = "))

        if ch==1:
            cl.add_student()
        elif ch==2:
            cl.search_student()
        elif ch==3:
            cl.remove_student()
        elif ch==4:
            print(cl)
        elif ch==0:
            print("Thank you!!")
            break
        else:
            print("Incorrect choice!!")
