# Source code for the game
import random

cash = 5000

def gameSystem(cash):
    print('''----------------------------------------
    
    
    Lets begin the game again>>>>>..........''')

   

    betAmount = int(input("Enter the amount you want to bet: "))
    if betAmount > cash or betAmount <= 0:
        print("You dont have enough cash !!!")
        return instructionLogin()

    else: 
            print("Valid input+")
            cash = cash - betAmount
            print("\n\nYou bet for $ ",betAmount)
            print(" \nYour current balance is now: $ ",cash)
            print("\n\n\nSystem is genrating a number which u have to between (1 - 10).......")

    
            randomNum = random.randint(1 , 10)

   
            for i in range(0,3):
                guessNum = input("Guess the number b/t (1 - 10):  ")
                if int(guessNum) == int(randomNum):
                    print('''
                    ----------------------------------------------------------------------------------------
                    
                    ******Bravo you did it !!!!! You guess the right number ( ''',guessNum,''' )****** 
                    
                    ----------------------------------------------------------------------------------------\n\n\n\n''')
                    betAmount = betAmount*2
                    cash = cash + betAmount
                    print("Total balance you have now $", cash)
                    break
        
                elif int(guessNum) > int(randomNum):
                    print("\nTake a lower number and try again...... -_- ")
                elif int(guessNum) < int(randomNum):
                    print("\nTake a higher number from what you guess and try again...... -_-")


            else: 
                print('''\n\n\nYou miss all the chance ****** Better luck next time ******
                The correct number was......... [''',randomNum, ''']''')

    
                
    return gameSystem(cash)

    




def instructionLogin():
    print('''**************************************

    Game instruction: 
    
    1> By default you will get $5000.
    2> Select amount you want to bet.
    3> Guess a number.
    4> You will get 3 chance to guess the number.
    5> If u guess the right one your bet money will get double.
    6> You can continue the game further.


    ************************************************''')
    name = input("Enter your name: ")
    

    print("Welcome ",name, "*You can start game by pressing 1+ [] ")

    response = input("Enter your response: ")

    if response == str('1'):
        gameSystem(cash)
    else:
        print("Invalid Input !!!")
        return instructionLogin()
    
 

instructionLogin()
