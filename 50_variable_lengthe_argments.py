#*args
def test_func(*Animals):
    for Animal in Animals:
        print(Animal)

AnimalList = ['Cat','Dog','Monkey']
test_func(AnimalList)
# AnimalList2 = ['Cat','Dog','Monkey','Lamb','Goat','Snake']
# test_func(AnimalList2)

# test_func("Cat","Dog","Snake","Lamb")