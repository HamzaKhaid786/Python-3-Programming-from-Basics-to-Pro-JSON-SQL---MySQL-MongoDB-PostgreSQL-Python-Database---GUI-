CurrentTry=1
TotalGuesses=3
CorrectAnswer=6
#----------
while CurrentTry<=TotalGuesses:
    UserAnswer=input("Enter your guess: (Between 0 to 9):")
    #---------
    UserAnswer=UserAnswer.replace(" ","")
    if UserAnswer=="":
        print("Enter the valid number!")
        continue
    #---------
    UserAnswer=int(UserAnswer)
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