CurrentTry=1
TotalGuesses=3
CorrectAnswer="Dog"
FirstLetter=CorrectAnswer[0]
#----------
while CurrentTry<=TotalGuesses:
    UserAnswer=input(f"Guess the animal name starting with '{FirstLetter}':")
    #---------
    UserAnswer=UserAnswer.replace(" ","")
    if UserAnswer=="":
        print("Enter the valid animal name!")
        continue
    #---------
    if UserAnswer==CorrectAnswer:
        print("You Win!")
        break
    else:
        print("")
        print(f"Wrong Answer! Try again! Left({TotalGuesses-CurrentTry} of {TotalGuesses})")
    #-----------------------
    CurrentTry+=1# CurrentTry= CurrentTry+1
#====================
else:
    print("You lost!")