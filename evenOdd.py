#Find even, Odd from a Arraylist.
x = [1,2,3,4,5,6,7]
#listOfLists = [x]

for num in x:
    res = int(num)    
    if (res % 2 == 0):
        print( res, "Even --")
    else:
        print(res, "Odd --")

            