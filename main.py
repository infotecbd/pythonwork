from os import remove

import view_contacts
import view_contacts
import add_contacts
from view_contacts import add_contact

all_contacts=[] # empty list to store book input

while True:
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Search Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
           add_contacts= add_contacts.add_contacts(add_contacts)
        elif choice == "2":
            view_contacts= view_contacts.view_contacts(view_contacts)
        elif choice == "3":
            remove_contact=remove_contact.remove_contact(remove_contacts)
        elif choice == "4":
            search_contact =search_contact.search_contact(search_contacts)
        elif choice == "5":
            print("Exiting... Saving contacts.")
            save_contacts= save_contacts.save_contacts(save_contacts)
            break
        else:
            print("Invalid choice. Please try again.")
























# import contactPersonData
# import view_allbooks
#
# from contactPersonData import (
#     add_contact,
#     view_contacts,
#     remove_contact,
#     search_contact,
# )
#
# all_contacts=[]
#
#
#
#
#
#
#
#     while True:
#         print("\nContact Book Menu")
#         print("1. Add Contact")
#         print("2. View Contacts")
#         print("3. Remove Contact")
#         print("4. Search Contact")
#         print("5. Exit")
#         choice = input("Enter your choice: ")
#
#         if choice == "1":
#            add_contact= add_contact(contacts)
#         elif choice == "2":
#             view_contacts(contacts)
#         elif choice == "3":
#             remove_contact(contacts)
#         elif choice == "4":
#             search_contact(contacts)
#         elif choice == "5":
#             print("Exiting... Saving contacts.")
#             save_contacts(contacts)
#             break
#         else:
#             print("Invalid choice. Please try again.")
#
