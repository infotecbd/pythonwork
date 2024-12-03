def view_all_books(all_books):
    if all_books != []:
        for book in all_books:
            print(f" Title:{book['title']}, \n Author:{book['author']}, \nBook: {book['isbn']}, \nYear: {book['year']}, \nPrice: {book['price']}, \nQuantity: {book['quantity']} \n")