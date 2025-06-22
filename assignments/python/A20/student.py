from SY.SYMARKS import SYMarks
from TY.TYMARKS import TYMarks

class Student:
    def __init__(self, rn=0, n="not given",sy=SYMarks, ty=TYMarks):
        self.roll_no = rn
        self.name = n
        self.sy = sy
        self.ty = ty

    def cal_grade(self):
        tot = self.sy.cal_marks() + self.ty.cal_marks()
        if tot >= 70:
            return f"A"
        elif tot >= 60:
            return f"B"
        elif tot >= 50:
            return f"C"
        elif tot >= 40:
            return f"Pass"
        else:
            return f"Fail"    

s1 = Student(101, "riri", (SYMarks(50,50,50)), TYMarks(49,20))
grade = s1.cal_grade()
print(s1.name,"got grade =", grade)

