import json
from datetime import datetime, timedelta

BOOKS_FILE = "books.json"
LENDINGS_FILE = "lendings.json"

def load_books():
    try:
        with open(BOOKS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_books(books):
    with open(BOOKS_FILE, "w") as f:
        json.dump(books, f, indent=4)

def load_lendings():
    try:
        with open(LENDINGS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_lendings(lendings):
    with open(LENDINGS_FILE, "w") as f:
        json.dump(lendings, f, indent=4)

def lend_book():
    books = load_books()
    lendings = load_lendings()

    print("\nAvailable books:")
    for idx, book in enumerate(books):
        print(f"{idx + 1}. {book['title']} (Quantity: {book['quantity']})")

    try:
        choice = int(input("\nEnter the number of the book to lend: "))
        if choice < 1 or choice > len(books):
            print("Invalid choice!")
            return
    except ValueError:
        print("Invalid input!")
        return

    selected_book = books[choice - 1]

    if selected_book["quantity"] <= 0:
        print("There are not enough books available to lend.")
        return

    borrower_name = input("Enter borrower's name: ")
    phone_number = input("Enter borrower's phone number: ")
    return_date = datetime.now() + timedelta(days=14)

    lending = {
        "borrower_name": borrower_name,
        "phone_number": phone_number,
        "book_title": selected_book["title"],
        "due_date": return_date.strftime("%Y-%m-%d")
    }

    lendings.append(lending)
    selected_book["quantity"] -= 1

    save_books(books)
    save_lendings(lendings)

    print(f"\nBook '{selected_book['title']}' has been lent to {borrower_name}. Due date: {return_date.strftime('%Y-%m-%d')}\n")

