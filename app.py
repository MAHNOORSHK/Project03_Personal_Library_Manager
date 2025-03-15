import json
import os

# File to store library data
LIBRARY_FILE = 'library.txt'

# Load library from file (if it exists)
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, 'r') as file:
            return json.load(file)
    return []

# Save library to file
def save_library(library):
    with open(LIBRARY_FILE, 'w') as file:
        json.dump(library, file)

# Add a book
def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    publication_year = int(input("Enter the publication year: "))
    genre = input("Enter the genre of the book: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == 'yes'

    book = {
        'title': title,
        'author': author,
        'publication_year': publication_year,
        'genre': genre,
        'read_status': read_status
    }
    library.append(book)
    print(f"\n Book '{title}' added successfully!\n")

# Remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book['title'].lower() == title.lower():
            library.remove(book)
            print(f"\n Book '{title}' removed successfully!\n")
            return
    print("\n Book not found!\n")

# Search for a book by title or author
def search_book(library):
    print("\nSearch by: ")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        search_term = input("Enter the title: ").lower()
        results = [book for book in library if search_term in book['title'].lower()]
    elif choice == '2':
        search_term = input("Enter the author: ").lower()
        results = [book for book in library if search_term in book['author'].lower()]
    else:
        print("\n Invalid choice!\n")
        return
    
    if results:
        print("\n Matching Books:")
        for i, book in enumerate(results, 1):
            status = 'Read' if book['read_status'] else 'Unread'
            print(f"{i}. {book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} - {status}")
        print()
    else:
        print("\n No matching books found.\n")

# Display all books
def display_books(library):
    if not library:
        print("\n Your library is empty.\n")
        return
    
    print("\n Your Library:")
    for i, book in enumerate(library, 1):
        status = 'Read' if book['read_status'] else 'Unread'
        print(f"{i}. {book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} - {status}")
    print()

# Display statistics
def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        print("\n No books in the library.\n")
        return
    
    read_books = sum(1 for book in library if book['read_status'])
    percentage_read = (read_books / total_books) * 100

    print("\n Library Statistics:")
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%\n")

# Display menu
def display_menu():
    print("\n Welcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

# Main function
def main():
    library = load_library()

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_book(library)
        elif choice == '4':
            display_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            save_library(library)
            print("\n Library saved to file. Goodbye!\n")
            break
        else:
            print("\n Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
