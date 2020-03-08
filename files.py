#"x" - Create - will create a file, returns an error if the file exist

#"a" - Append - will create a file if the specified file does not exist

#"w" - Write - will create a file if the specified file does not exist

f = open("file0.txt", "r")
print(f.readline())
f.close()


import os
if os.path.exists("file.txt"):
  os.remove("file.txt")
else:
  print("The file does not exist")
  
  
import os
os.rmdir("myfolder00") 