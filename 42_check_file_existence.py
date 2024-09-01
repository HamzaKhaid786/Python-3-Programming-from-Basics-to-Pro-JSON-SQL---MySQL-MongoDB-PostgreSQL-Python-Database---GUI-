#importing module
import os

if_exist = os.path.exists("info.txt")

if if_exist:
    print(if_exist)
else:
    print("File not found")

if_exist = os.path.exists("hamza.txt")

if if_exist:
    print(if_exist)
else:
    print("File not found")