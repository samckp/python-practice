a = 290
b = 99
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
 # multiple else statements on the same line:
a = 730
b = 130
print("A") if a > b else print("=") if a == b else print("B")


#And with if
a = 400
b = 44
c = 600
if a > b and c > a:
  print("Both conditions are True")
  

#Nested If else
x = 55
if x > 10:
  print("Above ten,")
  if x > 30:
    print("and also above 20!")
  else:
    print("but not above 20.")