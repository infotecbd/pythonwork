from validation import validate_name, validate_phone

def add_contact(contacts):
    print("\nAdd a New Contact")
    name = input("Enter name: ")
    if not validate_name(name):
        return

    phone = input("Enter phone number: ")
    if not validate_phone(phone):
        return

    if phone in [contact['phone'] for contact in contacts.values()]:
        print("Error: This phone number already exists.")
        return

    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"Contact '{name}' added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts available.")
        return

    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")

def remove_contact(contacts):
    name = input("\nEnter the name of the contact to remove: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' removed successfully.")
    else:
        print(f"Error: Contact '{name}' not found.")

def search_contact(contacts):
    search_term = input("\nEnter name or phone to search: ")
    results = [
        (name, details) for name, details in contacts.items()
        if search_term in name or search_term in details['phone']
    ]

    if results:
        print("\nSearch Results:")
        for name, details in results:
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
    else:
        print("No contacts found.")
