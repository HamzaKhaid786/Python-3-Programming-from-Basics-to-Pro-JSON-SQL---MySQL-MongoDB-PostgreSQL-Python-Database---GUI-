# Age Calculator

dob = input("Enter Your Date of Birth(yyyy/mm/dd): ")
y =  dob[0:4]
age = 2024 - int(y)
print("You are "+str(age)+" year old")
print(f"You are {age} years old")


#Another Method
dob = input("Enter Your Date of Birth(dd/mm/yyyy): ")
y =  dob[-4:]
age = 2024 - int(y)
print("You are "+str(age)+" year old")
print(f"You are {age} years old")
