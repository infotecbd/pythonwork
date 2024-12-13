# title, authors, ISBN, publishing year, price and quanity

from save_allbooks import save_allbooks
import random
from datetime import datetime

def add_books(all_books):
    title = input("Please enter a book Title: ")
    author = input("Please enter author name: ")
    isbn = input("Please input a ISBN number: ")
    year= input("Please input year of Published: ")
    price= input("Please input price of the Book: ")
    quantity= input("Please input the quantity of the books: ")

    isbn = random.randint(10000,99999)
    bookAddedAt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

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

    print ("Books added successful")

    return all_books