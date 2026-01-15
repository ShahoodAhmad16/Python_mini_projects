books = []


def add_book():
    title = input(f'Title: ')
    author = input(f'Author: ')
    year = int(input(f'Year: '))
    isbn = input(f'ISBN (should be 13 digits): ')
    for b in books:
        if b['isbn'] == isbn:
            print(f'ISBN already exits')
            return
    book = {
        'title': title,
        'author': author,
        'year': year,
        'isbn': isbn
    }
    books.append(book)


def view_all_books():
    if len(books) == 0:
        print(f'Current there are no books in the list please add to view them')
        return
    i = 1
    for book in books:
        print(f'Book{i}'.center(20, '-'))
        print(f'''Title:{book['title']}
Author: {book['author']}
Year: {book['year']}
Isbn: {book['isbn']}
''')
        i += 1


def search_book():
    if len(books) == 0:
        print(f"There aren't any books. Please add some")
        return
    i = 0
    while True:
        book_name = input(f'Title or Author name ').lower()
        for book in books:
            if book_name == book['title'].lower() or book_name == book['author'].lower():
                print(f'{book['title']}'.center(20, '-'))
                print(f'''Author: {book['author']}
Year: {book['year']}
Isbn: {book['isbn']}
''')
                return
        print(f'{book_name} not found')
        if i == 2:
            print(f'Returning to Main menu')
            return
        i += 1


def remove_book():
    if len(books) == 0:
        print(f'Book shelve is empty. Add some books')
        return
    i = 0
    while True:
        book_name = input(f'Enter book ISBN or Title').lower()
        for book in books:
            if book_name == book['title'].lower() or book_name == book['isbn'].lower():
                books.remove(book)
                return
        print(f'{book_name} not found')
        if i == 2:
            print(f'Limit reach return to main menu')
            return
        i += 1


def extra():
    if len(books) == 0:
        print(f"There arn't any books in the shelves")
        return
    while True:
        choice = int(input(f'''1:Total Books
2:List of Authors
3:Exit to main menu
'''))
        if choice == 1:
            print(f'Total Books: {len(books)}')
        elif choice == 2:
            authors = set()
            for book in books:
                authors.add(book['author'])
            print(authors)
        elif choice == 3:
            return
        else:
            print(f'Wrong Choice')


while True:
    choice = int(input(f'''1:Add a Book
2:View all books
3:Search book by name
4:Delete a book
5:Extra
6:Exit
'''))
    if choice == 1:
        add_book()
    elif choice == 2:
        view_all_books()
    elif choice == 3:
        search_book()
    elif choice == 4:
        remove_book()
    elif choice == 5:
        extra()
    elif choice == 6:
        print(f'Exiting')
        break
    else:
        print(f'Invalid Input choice must be between 1 and 6')
