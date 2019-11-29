class Employee:
    def __init__(myobj, name, age):
        myobj.name = name
        myobj.age = age

    def caller(obj):
        print("Hello : ", obj.name)


p1 = Employee("tomy", 36)
p1.caller()

#Delete Object
del p1
p1.caller()