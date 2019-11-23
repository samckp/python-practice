x = lambda a : a + 10
print(x(5))

y = lambda a, b : a * b
print(y(5, 9))


#Function with lambda

def lamdaTest(n):
    return lambda a : a * n


mydoubler = lamdaTest(2)
mytripler = lamdaTest(3)

print(mydoubler(11))
print(mytripler(11))
