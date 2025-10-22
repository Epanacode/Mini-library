from functions_library import *



def main_menu():
    while True:
        print("\n====== Mini Library ======")
        print("1. Add new book")
        print("2. View all books")
        print("3. Delete a book")
        print("4. View total books")
        print("5. Exit")
        print("===========================")
        
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_book()
            
        elif choice == "2":
           view_all_books()
            
        elif choice == "3":
            delete_book()
            
        elif choice == "4":
            view_total_books()
            
        elif choice == "5":
            print("Goodbye!")
            time.sleep(1)
            break
        else:
            print("Invalid choice, try again.")
 


    
if __name__ =="__main__":
    main_menu()