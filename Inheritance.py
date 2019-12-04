class Parent:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Child(Parent):
    def __init__(self, fname, lname):
        Parent.__init__(self, fname, lname)


x = Child("Tony", "Singh")
x.printname()
