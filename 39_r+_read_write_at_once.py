MyFile = open("info3.txt","r+")
r = MyFile.write("This text is written using r+")
MyFile.seek(0)
content = MyFile.read()
print(content)