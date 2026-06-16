import json

contacts = {
            "Contacts":[{"name":"ravi","Phone":"6302548623"},
                        {"name":"karthik","Phone":"25623562"}
            ]
}
with open("contacts.json","w") as file:
    json.dump(contacts,file,indent=4)
with open("contacts.json","r") as file:
    content = json.load(file)
    for i in content["Contacts"]:
        print("Name: "+i["name"] +" | Phone: "+i["Phone"])
