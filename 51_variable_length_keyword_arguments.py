#** kwargs

def test_func(**Students):
    MyGrade = Students["Grade"]
    MyFname = Students["Fname"]
    # MyGrade = Students["Grade"]
    print(f"Hi, {MyFname} You are at Grade {MyGrade}")

test_func(Grade=12,Fname="Hamza")

test_func(Fname="Hamza",Grade=12)


