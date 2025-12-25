def add(a,b):
    return a + b

def sub(a,b):
    return a - b


def mul(a,b):
    return a * b


def div(a,b):
    if b == 0:
        return "Invalid input! Division by zero not possible!"
    return a / b

while True:
    print("------Basic Calculator------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit!")

    choice = input("Enter your choice from 1-5: ")

    if choice == "5":
        print("Calulator closed! Byee!!")
        break

    if choice in ["1", "2", "3", "4" ]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter seecond number: "))

        if choice == "1":
            print("Your Sum is: ", add(num1, num2))

        elif choice =="2":
            print("Your Difference is: ", sub(num1, num2))

        elif choice =="3":
            print("Your Product is: ", mul(num1, num2))

        elif choice =="4":
            print("Your Quotient is: ", div(num1, num2))

    else:
        print("invalid input! Pls enter a valid number.")