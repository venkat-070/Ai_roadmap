def display(d):
    for key,value in d.items():
        print(key+": "+value)
contacts = {"Ravi":"148622545","Sita":"2587896525","Amit":"187521462"}
contacts_upper = {key.upper():value for key,value in contacts.items()}
display(contacts)
display(contacts_upper)

