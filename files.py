import os

FILE_NAME = "contact.txt"

def contactPersonData():
    if not os.path.exists(FILE_NAME):
        return {}

    contacts = {}
    with open(FILE_NAME, "r") as file:
        for line in file:
            name, phone, email, address = line.strip().split(",")
            contacts[name] = {"phone": phone, "email": email, "address": address}
    return contacts

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        for name, details in contacts.items():
            line = f"{name},{details['phone']},{details['email']},{details['address']}\n"
            file.write(line)

