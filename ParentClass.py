class ParentClass:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# Use the ParentClass class to create an object, and then execute the printname method:

x = ParentClass("Richie", "Carlton")
x.printname()
