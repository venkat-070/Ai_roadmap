import os 
import json
def load_notes():
    if os.path.exists(r"D:\notes.json"):
        with open("D:\\notes.json") as f1:
            content = json.load(f1)
            return content
    else:
        with open("D:\\notes.json","w") as file:
            data = {"notes":[]}
            json.dump(data,file,indent = 4)
            return data
def save_notes(data):
    with open("D:\\notes.json","w") as file:
        json.dump(data,file,indent = 4)
def add_notes(data):
    note = input("Enter your note: ")
    data["notes"].append({"id":len(data["notes"])+1 , "note" :note})
    save_notes(data)
    print("data saved sucessfully!..")
def view_notes(data):
    if data["notes"]:
        for i in data["notes"]:
            print(str(i["id"])+". "+i["note"])
    else:
        print("No notes saved yet!")
def delete_note(data):
    view_notes(data)
    try:
        del_key = int(input("Enter the id to delete: "))
    except ValueError:
        print("Enter a valid number!")
        return
    if any(note["id"] == del_key for note in data["notes"]):
        data["notes"] = [note for note in data["notes"] if note["id"] != del_key]
        save_notes(data)
        print("The note deleted sucessfully!..")
    else:
        print("Note not found!")
data = load_notes()

while True:
    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Delete Note")
    print("4. Exit")
    
    choice = input("Select an option: ")
    
    if choice == "1":
        add_notes(data)
    elif choice == "2":
        view_notes(data)
    elif choice == "3":
        delete_note(data)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
