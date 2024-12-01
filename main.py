from contactPersonData import (
    add_contact,
    view_contacts,
    remove_contact,
    search_contact,
)
from files import contactPersonData, save_contacts


def main():

    contacts = contactPersonData()

    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Search Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            remove_contact(contacts)
        elif choice == "4":
            search_contact(contacts)
        elif choice == "5":
            print("Exiting... Saving contacts.")
            save_contacts(contacts)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
