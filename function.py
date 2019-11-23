def square(num):
    return num * num;

print("square --" , square(15))

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# Flexible argument using *, we can pass any number of arguments
def my_function(*kids):
  print("The youngest child is " + kids[3])

my_function("Emil", "Tobias", "Linus", "tony")


# Pass keyword for empty method

def passMethod():
    pass

print(passMethod())

#Recursive function

def factorialOfnumber(num):
    if(num>0):
        result = num * (factorialOfnumber(num - 1))
    else:
        result = 1
    return result

print("Factorial of number :", factorialOfnumber(6))


