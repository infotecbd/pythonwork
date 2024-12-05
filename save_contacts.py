# title, authors, ISBN, publishing year, price and quanity
from MySQLdb import connect


def  save_contacts(all_contacts):
    with open("all_contacts.csv", "w") as fp:
        for contacts in all_contacts:
            line = f"{contacts['name']}, \n{contacts['email']}, \n{contacts['phone']}, \n{contacts['address']} \n"
            fp.write(line)
