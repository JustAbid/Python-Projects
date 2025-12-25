import random

target = random.randint(1,100)

while True:
    
    UserChoice = input("Press Q to exit or Enter you Guess: ")
    if (UserChoice == "Q"):
        break

    UserChoice = int(UserChoice)

    if(UserChoice == target):
        print("Good Guess!! Success!")
        break
    elif (UserChoice < target):
        print("Your Guess is small, take a bigger guess!")
    else: 
        print("Your Guess is big, take a smaller Guess!")
print("-----Game Over!-----")

    
