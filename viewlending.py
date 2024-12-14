import json

LENDINGS_FILE = "lendings.json"

def load_lendings():
    try:
        with open(LENDINGS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def view_lendings():
    lendings = load_lendings()
    if not lendings:
        print("\nNo active lendings.\n")
        return

    print("\nActive lendings:")
    for lending in lendings:
        print(f"- {lending['borrower_name']} borrowed '{lending['book_title']}' (Due: {lending['due_date']})")
