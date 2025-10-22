import os
import json
import time


# ============= FUNCTIONS =======


# تابع لود فایل
def load_books():
    if os.path.exists("books.json"):
        with open("books.json", "r") as file:
            return json.load(file)
    else:
        return []
# تابع ذخیره فایل         
def save_books():
    with open("books.json", "w") as file:
        json.dump(books, file, indent=2)

# تابع اضافه کردن کتاب 

def add_book():
    print("\n=== Add New Book ===")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter publication year: ")

    book = {
        "title" : title,
        "author" : author,
        "year"  : year
    }
    books.append(book)
    save_books()
    print(f"✅Book '{title}' added successfully...!")
    time.sleep(1)

# دیدن کتاب ها 
def view_all_books():
    print("====All Books====")
    if not books:
        print("No book added yet!!")
    else:
        for i, book in enumerate(books, start=1):
            print(f"{i}. '{book['title']}' by {book['author']} in {book['year']}")
    input("\n press Enter to return to menu.....")
    time.sleep(1)
    
# تابع حذف کتاب 
def delete_book():
    print("\n ====Delete Book====")
    if not books:
        print("No book to delete...!")
        time.sleep(1)
        return
    for i, book in enumerate(books, start=1):
        print(f"{i}. '{book['title']} by {book['author']} in {book['year']}")
    try: 
        index = int(input("\nEnter the number of the book to delete: "))
        
        if 1 <= index <= len(books):
            deleted = books.pop(index - 1)
            save_books()
            print(f"✅Deleted '{deleted['title']}' successfully...!")
        else:
            print("❌Invalid number....")
    except IndexError:
        print("❌ Please enter a valid number.")
        
    time.sleep(1)
            

# تابع نمایش تعداد کل کتاب ها

def view_total_books():
    print("\n ====View Total Books====")
    if not books:
        print("No book found...!")
    else:
        print(f"📚 Total books in library ----> {len(books)}")        
    time.sleep(2)
        
        

# ساخت یا بارگذاری لیست
books = load_books()