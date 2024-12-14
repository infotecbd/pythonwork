import json

BOOKS_FILE = "books.json"

def load_books():
    try:
        with open(BOOKS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_books(books):
    with open(BOOKS_FILE, "w") as f:
        json.dump(books, f, indent=4)

def add_book():
    books = load_books()
    title = input("Enter the title of the book: ")
    try:
        quantity = int(input("Enter the quantity of the book: "))
    except ValueError:
        print("Invalid input! Quantity should be a number.")
        return

    books.append({"title": title, "quantity": quantity})
    save_books(books)
    print(f"\nBook '{title}' added with quantity {quantity}.\n")
