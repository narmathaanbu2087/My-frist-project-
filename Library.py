Library Management System (library.py)

import json import os

FILE_NAME = "library.json"

Load data

def load_data(): if os.path.exists(FILE_NAME): with open(FILE_NAME, "r") as f: return json.load(f) return []

Save data

def save_data(data): with open(FILE_NAME, "w") as f: json.dump(data, f, indent=4)

Add book

def add_book(data): title = input("Enter book title: ") author = input("Enter author name: ") book_id = input("Enter book ID: ")

book = {
    "id": book_id,
    "title": title,
    "author": author,
    "issued": False
}

data.append(book)
save_data(data)
print("Book added successfully!\n")

View books

def view_books(data): if not data: print("No books available!\n") return

print("\n--- Book List ---")
for i, book in enumerate(data, start=1):
    status = "Issued" if book['issued'] else "Available"
    print(f"{i}. ID: {book['id']} | {book['title']} by {book['author']} | {status}")
print()

Issue book

def issue_book(data): book_id = input("Enter book ID to issue: ")

for book in data:
    if book['id'] == book_id:
        if not book['issued']:
            book['issued'] = True
            save_data(data)
            print("Book issued successfully!\n")
        else:
            print("Book already issued!\n")
        return

print("Book not found!\n")

Return book

def return_book(data): book_id = input("Enter book ID to return: ")

for book in data:
    if book['id'] == book_id:
        if book['issued']:
            book['issued'] = False
            save_data(data)
            print("Book returned successfully!\n")
        else:
            print("Book was not issued!\n")
        return

print("Book not found!\n")

Delete book

def delete_book(data): book_id = input("Enter book ID to delete: ")

for book in data:
    if book['id'] == book_id:
        data.remove(book)
        save_data(data)
        print("Book deleted successfully!\n")
        return

print("Book not found!\n")

Main menu

def main(): data = load_data()

while True:
    print("\n====== Library Management System ======")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_book(data)
    elif choice == '2':
        view_books(data)
    elif choice == '3':
        issue_book(data)
    elif choice == '4':
        return_book(data)
    elif choice == '5':
        delete_book(data)
    elif choice == '6':
        print("Thank you!")
        break
    else:
        print("Invalid choice! Try again.\n")

if name == "main": main()
