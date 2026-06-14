contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    
    choice = input("Select an option: ")
    
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter mobile no: ")
        contacts[name] = phone
        print("Contact added!")
    elif choice == "2":
        if not contacts:
            print("No contacts saved Yet!")
        else:
            for key,value in contacts.items():
                print(key+": "+value)
    elif choice == "3":
        name = input("Enter name: ")
        if name in contacts:
            print(name+": "+contacts[name])
        else:
            print("Contact not found!")
    elif choice == "4":
        name = input("Enter name: ")
        if name in contacts:
            del contacts[name]
            print(name+" Contact deleted!")
        else:
            print("Contact doesnt exists!!")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")