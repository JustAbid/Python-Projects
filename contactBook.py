contactBook = {}

while True:
    print("----- Simple Contact Book -----\n") 
    print("1.Add a contact")
    print("2.View all contacts")
    print("3.Search for a contact")
    print("4.Delete a contact")
    print("5.Exit")

    userChoice = input("Select ur option (1-5): ")

    if userChoice == "5":
        print("Contact Book closed!")
        break

    if userChoice =="1":
        name = input("Enter Name: ").lower()
        phno = input("Enter Phone Number: ")
        contactBook[name] = phno
        print("Conttact added successfully!!")

    elif userChoice == "2":
        if len(contactBook) == 0:
            print("No contacts available!")
        else:
            print("Your contacts:")
            for name, phno in contactBook.items():
                print(f"Name: {name} | Phone: {phno}")

    elif userChoice == "3":
        search_name = input("Enter contact name to search: ").lower()

        if search_name in contactBook:
            print(f"Phone Number: {contactBook[search_name]}")
        else:
            print("Not Found!")
        
    elif userChoice == "4": 
        delete_name = input("Enter Name to delete the contact: ").lower()

        if delete_name in contactBook:
            del contactBook[delete_name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    else:
        print("Invalid input! Pls select an option between 1-5")
