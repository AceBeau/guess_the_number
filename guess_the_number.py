import random

Secret_Key = random.randrange(1,20)



def Main_Game():
    print("#"*75)
    print("#"*8 + " "*20 + "Let's Begin The Fun" + " "*20 + "#"*8)
    print("#"*75)
    print("\n")
    print("Let's Start\n")
    global guess
    for x in range(0,3):
        guess = int(input("Enter Your Guess >> "))
        if guess < Secret_Key:
            print("\nTry To Guess Higher Number!!")
        elif guess > Secret_Key:
            print("\nTry To Guess Lower Number!!")
        else:
            break
    return guess

def check(guess,Secret_Key):
    if guess == Secret_Key:
        print("\n Congratulations!! You Guess The Correct Number ")
    else:
        print("\nOh! Out Of Turns")
        print("\nBetter Luck Next Time")

def Lets_begin():
    print("#"*75)
    print("#"*6 + " "*5 + "Welcome To The Game" + " "*5 + "*"*6 + " "*5 + "Ready For The Fun?" + " "*5 + "#"*6)
    print("#"*75+"\n")
    choice = int(input(" 1. Let's Begin The Fun \n 2. Rules \n 3. I Don't Want To Play  \n >>  "))
    if choice == 1:
        Main_Game()
    elif choice == 2:
        rules()
    else:
        exit()


def rules():
    print("#"*75)
    print("#"*9 + " "*20 + "Rules Of The Game" + " "*20 + "#"*9)
    print("#"*75)
    print("\n > You Will Get Three Chances To Guess The Secret Number")
    choice = int(input("Want To Play? \n 1. Yes \n 2. No \n >> "))
    if choice == 1:
        Main_Game()
    else:
        Lets_begin()
    

Lets_begin()
check(guess,Secret_Key)