thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#range of indexes by specifying where to start and where to end the range
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


#Tuples are unchangeable, or immutable
#there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
print("before change-",x)
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print("after change -",x)

# For loop on tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

#Join two tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
