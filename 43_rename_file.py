import os

if_exist = os.path.exists("info3.txt")

if if_exist:
   os.rename("info3.txt","newinfochecker.txt")
   print("Its Done")
else:
    print("File not found")
