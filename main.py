from add_book import add_book
from lendbook import lend_book
from returnbook import return_book
from viewlending import view_lendings

all_books=[]
while True:
        print("\nLibrary Management System")
        print("1. Add a Book")
        print("2. Lend a Book")
        print("3. Return a Book")
        print("4. View Lendings")
        print("5. Exit")

        choice = input("\nEnter your choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            lend_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            view_lendings()
        elif choice == "5":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice! Please try again.\n")
