
import json

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

def return_book():
    books = load_books()
    lendings = load_lendings()

    borrower_name = input("Enter borrower's name: ")
    book_title = input("Enter the title of the book being returned: ")

    for lending in lendings:
        if lending["borrower_name"] == borrower_name and lending["book_title"] == book_title:
            lendings.remove(lending)

            for book in books:
                if book["title"] == book_title:
                    book["quantity"] += 1
                    break

            save_books(books)
            save_lendings(lendings)

            print(f"\nBook '{book_title}' has been returned by {borrower_name}.\n")
            return

    print("\nNo matching lending record found!\n")
