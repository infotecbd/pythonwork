import add_book

all_books=[] # empty list to store book input

while True:
    print("Welcome to Library Management System")

    print ("0. Exit")
    print ("1. Add a book")
    print ("2. View All Books")

    # To get input from user

    menu = input("Select any number: ")

    if menu == "0":
        print("Thanks for using Library Management System")
        break
    elif menu == "1":
        all_books = add_book.add_books(all_books)
    elif menu == "2":
        print("Book List here")
    
    else:
        print("You have chosen invalid number")


