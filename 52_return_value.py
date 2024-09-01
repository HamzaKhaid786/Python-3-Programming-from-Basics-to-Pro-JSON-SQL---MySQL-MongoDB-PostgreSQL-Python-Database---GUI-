
def age_calculator(YearofBirth):
    Age = 2024 - YearofBirth
    return Age

birthyear = int(input("Enter Your Birth Year: "))

r = age_calculator(birthyear)
print(f"You are {r} years old")