tasks = []

while True:
    print("\n----- Simple To-Do List -----")
    print("1. Add task")
    print("2. View task")
    print("3. Delete task")
    print("4. Exit!")

    UserChoice = input("Select an option between 1 - 4: ")


    if UserChoice == "4":
        print("Thank You!!!")
        break

    if UserChoice == "1":
        addto = input("Enter ur Task: ")
        tasks.append(addto)
        print("Task added successfully!  ")

    elif UserChoice == "2":
        if len(tasks) == 0:
            print("No tasks available!")
        else:
            print("\nYour Tasks:")
            for i, addto in enumerate(tasks, start=1):
                print(f"{i}.{addto}")

    elif UserChoice == "3":
        if len(tasks) == 0:
            print("No tasks to delete!")
        else:
            print("\nYour Tasks:")
            for i, addto in enumerate(tasks, start=1):
                print(f"{i}.{addto}")

            delete_choice = int(input("Enter task number to delete: "))
            
            if 1 <= delete_choice <= len(tasks):
                removed_task = tasks.pop(delete_choice-1)
                print(f"Task '{removed_task}' deleted successfully!")
            else:
                print("Invalid Task number!")
    else:
        print("Invalid Choice!")