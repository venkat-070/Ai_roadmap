while True:
    print("1. Say Hi","2. Say Bye","3. Exit",sep="\n")
    x = input("Select an option: ")
    if x == "1":
        print("\nHi there!\n")
    elif x == "2":
        print("\nBye!\n")
    elif x == "3":
        print("\nExiting...\n")
        break
    else:
        print("\nInvalid choice, try again.\n")


