

from save_contacts import save_contacts

def add_contacts(all_contacts):
    name = input("Please enter persons name: ")
    email = input("Please enter persons email: ")
    phone = input("Please enter persons phone number: ")
    address= input("Please enter persons address: ")


    # Add all in a dictionary
    contacts = {
        "name" : name,
        "email" : email,
        "phone" : phone,
        "address" : address,

    }

    #Now need to append it in all_contacts[] list
    all_contacts.append(contacts)

    # Now create save function to save all books which are got input from user

    save_contacts(all_contacts)

    return all_contacts