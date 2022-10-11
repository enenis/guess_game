from random import randint

rand= randint(1,100)
sayac=0
while True:
    sayac+=1
    
    x=int(input("Your Number Prediction 0(game stops) 1/100 : "))
    if x==0:
        print("You Pause the Game")
        break
    elif rand>x:
        print("Enter Larger Number! ")
        continue
    elif rand<x:
        print("Enter Smaller Number! ")
        continue
    elif rand==x:
        print("You Guessed Correctly!!!")
        print("Score :",sayac)
        again=input("Would you like to play again? Y/N : ").capitalize()
        if again=="Y":
            continue
        else:
            break