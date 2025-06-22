class SYMarks:
    def __init__(self, ct=0, mt=0, et=0):
        self.computer_total = ct
        self.maths_total = mt
        self.electronics_total = et

    def cal_marks(self):
        return self.computer_total + self.maths_total + self.electronics_total
    
    