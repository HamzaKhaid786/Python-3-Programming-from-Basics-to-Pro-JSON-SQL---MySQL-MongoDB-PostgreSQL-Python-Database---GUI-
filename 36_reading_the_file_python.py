
#read
'''MyFile = open("info.txt","r")
content = MyFile.read()
print(content)
MyFile.close()

MyFile = open("info.txt","r")
content = MyFile.read(20)
print(content)
MyFile.close()

MyFile = open("info.txt","r")
MyFile.seek(10)
content = MyFile.read()
print(content)
MyFile.close()



MyFile = open("info.txt","r")
content = MyFile.readline()
print(content)
content = MyFile.readline(5)
print(content)
content = MyFile.readline(2)
print(content)
MyFile.close()


MyFile = open("info.txt","r")
content = MyFile.readlines()
print(content)
MyFile.close()


MyFile = open("info.txt","r")
content = MyFile.readlines()
for x in content
    print(x.replace("\n",""))
MyFile.close()

#Reading Binary File
MyFile = open("info.txt","rb")
content = MyFile.read()
print(content)
MyFile.close()
'''
MyFile = open("info.txt","r")
content = MyFile.read()
print(content)
MyFile.close()