import sqlite3

db = sqlite3.connect('data/ebookstore')
cursor = db.cursor()


def new_book():
    book_id = input("Enter the id of the book you want to add: ")
    book_name = input("Enter name of the book you want to add: ")
    book_author = input('Enter name of author: ')
    book_quantity = input("Enter quantity of the book: ")
    cursor.execute(
        f'''Insert into books(id, title, author, qty) values({book_id}, {book_name}, {book_author}, {book_quantity})''')
    db.commit()


def update_book():
    id = input("Enter id of the book: ")
    title = input("Enter title of the book: ")
    quantity = input("Enter quantity of the book: ")
    author = input("Enter author of the book: ")
    cursor.execute(f'''update book set quantity = {quantity} where quantity''')
    db.commit()


def delete_book():
    id = input("Enter id of the book: ")
    title = input("Enter title of the book: ")
    author = input("Enter author of the book: ")
    cursor.execute(
        f'''delete from books where id = {id}, {title}, {author}'''
    )



def search_book():
    id = input("Enter id of the book: ")
    cursor.execute(f'''select id from books where exists (select id from books where id = {id}) 
                    ''')
    book = cursor.fetchone()

while True:
    menu = input("\n"'''Select the following options: 
            n- new book
            u - update book
            d - delete book
            s - search book
            e - exit''').lower()
    if menu == 'n':
        new_book()

    elif menu == 'u':
        update_book()

    elif menu == 'd':
        delete_book()

    elif menu == 's':
        search_book()

    elif menu == 'e':
        exit()
