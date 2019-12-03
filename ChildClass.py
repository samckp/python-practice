import ParentClass


class Student(ParentClass):
    def __init__(self, fname, lname):
        ParentClass.__init__(self, fname, lname)
