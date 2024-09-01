import os

if_exist = os.path.exists("testdel.txt")

if if_exist:
   os.remove("testdel.txt")
   print("Its Done")
else:
    print("File not found")
