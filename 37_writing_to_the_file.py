#Adding content in files

'''MyFile = open("info.txt","w")

r = MyFile.write("Hamza is the best Developer")
print(r)
MyFile.close()

MyFile = open("info.txt","r")
r = MyFile.read()
print(r)
MyFile.close()

#Adding Multilines

MyFile = open("info.txt","w")

r = MyFile.write("Hamza is the best Developer \n"+ "He is a hacker too")
print(r)
MyFile.close()

MyFile = open("info.txt","r")
r = MyFile.read()
print(r)
MyFile.close()

#writelines
#Adding content in files

MyFile = open("info.txt","w")

r = MyFile.writelines(["Hamza is the best Developer \n", "He is a hacker too"])
MyFile.close()

MyFile = open("info.txt","r")
r = MyFile.read()
print(r)
MyFile.close()'''

#seek method

MyFile = open("info.txt","w")
MyFile.seek(10)
r = MyFile.write("Hamza is the best Developer \n"+ "He is a hacker too")
print(r)
MyFile.close()
MyFile = open("info.txt","r")
r = MyFile.read()
print(r)
MyFile.close()