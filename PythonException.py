try:
    f = open("dfile.txt")
    f.write("Lord of rings")
except:
    print("Something went wrong when writing to the file!!")
finally:
    f.close()
