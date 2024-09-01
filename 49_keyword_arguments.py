
#This is useful when you donn know order of argument is advance because order doesn't matter
def test_func(Fname,Age):
    print(f"Hi, {Fname}, You are {Age} Years Old")

test_func(Age=25,Fname="Hamza")
test_func("Esha",19)
