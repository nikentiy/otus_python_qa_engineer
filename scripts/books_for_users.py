import argparse
import csv
import json


def read_books_file(path: str) -> list:
    books = []
    with open(path, newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            books.append(dict(zip(header, row)))
    return books


def read_users_file(path: str) -> list:
    with open(path, "r") as f:
        return json.loads(f.read())


def write_library(path: str, data: list):
    with open(path, "w") as f:
        s = json.dumps(data, indent=4)
        f.write(s)


def library(books: list, users: list):
    _library = books.copy()
    i=0
    while i != len(users):
        try:
            book = books[i]
        except IndexError:
            return
        user = users[i]
        if not user.get('books'):
            user['books'] = []
        user['books'].append(book)
        _library.remove(book)
        i += 1
    if len(_library) != 0:
        library(_library, users)


def main(books_file, users_file):
    books = read_books_file(books_file)
    users = read_users_file(users_file)
    library(books, users)
    write_library('./src/library.json', users)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Script to assign books from a file to users from a file",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-b", "--books", dest='books', type=str,
                        help="path to csv file with books info")
    parser.add_argument("-u", "--users", dest='users', type=str,
                        help="path to json file with users info")
    args = parser.parse_args()
    main(args.books, args.users)
