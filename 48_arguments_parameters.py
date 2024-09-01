# #Single Argument and Parameter
# def test_func(Fname):
#     print(f"Hi, {Fname} You are AMAZING Be the Same ALWAYS")

# test_func("Hamza")
# test_func("Esha")


# #Argument  vs Parameter
# def test_func(Fname):#Parameter
#     print(f"Hi, {Fname} You are AMAZING Be the Same ALWAYS")

# test_func("Hamza")#Argument
# test_func("Esha")

#Multiple Arguments

# def test_func(Fname,Age):
#     print(f"Hi, {Fname}, You are {Age} Years Old")

# test_func("Hamza",24)
# test_func("Esha",19)

#Adding default Value to Parameters

# def test_func(Fname,Age=24):
#     print(f"Hi, {Fname}, You are {Age} Years Old")

# test_func("Hamza",24)
# test_func("Esha")


#passing list as arguments

def test_func(Animals):
    for Animal in Animals:
        print(Animal)

AnimalList = ['Cat','Dog','Monkey']
test_func(AnimalList)


