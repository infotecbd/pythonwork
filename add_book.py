# title, authors, ISBN, publishing year, price and quanity

from save_allbooks import save_allbooks

def add_books(all_books):
    title = input("Please enter a book Title: ")
    author = input("Please enter author name: ")
    isbn = input("Please input a ISBN number: ")
    year= input("Please input year of Published: ")
    price= input("Please input price of the Book: ")
    quantity= input("Please input the quantity of the books: ")

    # Add all in a dictionary
    book = {
        "title" : title,
        "author" : author,
        "isbn" : isbn,
        "year" : year,
        "price" : price,
        "quantity" : quantity
    }

    #Now need to append it in all_books[] list
    all_books.append(book)

    # Now create save function to save all books which are got input from user

    save_allbooks(all_books)

    return all_books