import random

validlist = ["rock", "paper", "scissor"]

while True:
    userchoice = input("Choose ur weapon - Rock/Paper/Scissor:  ").lower()
    if userchoice not in validlist:
        print("Invalid choice! Try again.")
        continue

    compchoice = random.choice(validlist)
    print("You chose: ", userchoice)
    print("Computer's choice: ", compchoice)

    if userchoice == compchoice:
        print("It's a draw!")

    elif (
            (userchoice == "paper" and compchoice == "rock") or
            (userchoice == "rock" and compchoice == "scissor") or
            (userchoice == "scissor" and compchoice == "paper")
        
        ):
        print("You win!!!")
    else:
        print("Computer wins!!!")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        break