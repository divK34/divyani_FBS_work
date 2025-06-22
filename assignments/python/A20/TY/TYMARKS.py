class TYMarks:
    def __init__(self, tm=0, pm=0):
        self.theory_marks = tm
        self.practical_marks = pm

    def cal_marks(self):
        return self.theory_marks + self.practical_marks