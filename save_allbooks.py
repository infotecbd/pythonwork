# title, authors, ISBN, publishing year, price and quanity

def  save_allbooks(all_books):
    with open("all_books.csv", "w") as fp:
        for book in all_books:
            line = f"{book['title']}, \n{book['author']}, \n{book['isbn']}, \n{book['year']}, \n{book['price']}, \n{book['quantity']} \n"
            fp.write(line)


