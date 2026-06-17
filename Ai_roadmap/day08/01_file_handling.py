with open("my_notes.txt","w") as file:
    file.write("First note\n")
    file.write("Second note\n")
    file.write("Third note\n")
    print("\ntext written sucessful.\n")
with open("my_notes.txt","r") as file:
    content = file.read()
    print(content)
    print("File read sucessfull.\n")
with open("my_notes.txt","a") as file:
    file.write("Fourth note")
    print("File append sucessfull\n")
with open("my_notes.txt","r") as file:
    text = file.read()
    print(text)
