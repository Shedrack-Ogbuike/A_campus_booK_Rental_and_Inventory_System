# Liberary Manager - A campus booK Rental and Inventory System

Inventory = {}
from datetime import datetime, timedelta


    
# Add/Update a new book to the library inventory 
def add_book():
    """Allows a user to add books to the Inventory.
    The user is prompted to enter is book title
     """
     
    book_title = input("Enter the book title: ").strip()
    
    # Check if book exist in the Inventory
    if book_title in Inventory:
        print(f"{book_title} is in the inventory")
        additional_quantity = int(input("How many copies are you adding to the inventory"))
        Inventory[book_title]["quantity"] += additional_quantity
        print(f"{additional_quantity} copies of {book_title} has been added to the inventory")
    else:
    
    # If it does not exist add to the inventory
        
        book_ID = input("Enter the book ID").strip()
        author = input("Enter the author: ").strip()
        quantity = int(input("Enter the quantity: "))    
        Inventory[book_title] = {"author": author, "quantity": quantity, "book_ID": book_ID, "available": True}
        print(f" {quantity} copies of {book_title} has been added to the inventory.")  
    
    
# Display Inventory

def display_Inventory():
    """ Display the current Inventory of Books
    """
    
    if not Inventory:
        print("\nThe inventory is empty, No book available")
    else:
        print("\n current Inventory:")
        print(f"{'Book_Title':<25}{'Quantity':<10}{str('Book_ID'):<25}{'Author':<25}{'Available'}")
        print("-" * 50)
        for book_title, details in Inventory.items():
           print(f"{book_title:<25}{details["quantity"]:<10}{details[str("book_ID")]:<25}{details["author"]:<25}{details["available"]}")
           
# List to track borrowed books
Borrowers_List = []
# Fine settings
Fine_Per_Day = 2  # $2 per extra day
           
# Rent a book from the library inventory
def rent_book():
    """Allows a user to rent a book.
    The user is prompted to enter book title"""
    book_title = input(" Enter the book title you want to rent").strip()
    if book_title in Inventory:
        if Inventory[book_title]["available"] and Inventory[book_title]["quantity"] > 0 :
            Inventory[book_title]["available"] = True
            
            # Decrease quantity by 1 
            Inventory[book_title]["quantity"] -= 1

            borrowers_name = input("Enter Borrower's name").strip()
            borrowers_ID = input("Enter borrowers_ID").strip()
            borrow_date = datetime.now()
            due_date = borrow_date + timedelta(days=7)  # 7-day due date
            
            Rental_list = {"name of borrower": borrowers_name,
                           "borrowers_ID": borrowers_ID,
                           "book_title": book_title, 
                           "book_ID" : Inventory[book_title]["book_ID"],
                           "borrow_date" : borrow_date.strftime("%Y-%m-%d"),
                           "due_date": due_date.strftime("%Y-%m-%d"),
                           "status": "Borrowed" }
            Borrowers_List.append(Rental_list)
            
            
            print(f" {borrowers_name} with ID {borrowers_ID} has  successfully borrowed {book_title}  by {Inventory[book_title]['author']}  ")
            print(f" Borrow Date: {borrow_date.strftime("%Y-%m-%d %H:%M:%S")}")
            print(f" Due Date: {due_date.strftime("%Y-%m-%d %H:%M:%S")}")
            
        else:
            print("Sorry, the book is not available")
    else:
        print("Invalid book title, book not found in the inventory")
        
# Return a book to the library Inventory

def return_book():
    """Allows a user to return a book ,
    The user is prompted to enter book title"""
    book_title = input("Enter the book title:").strip()       
    
    if book_title in Inventory:      
        borrowers_name = input("Enter Borrower's name").strip()
        borrowers_ID = input("Enter borrowers_ID").strip()
            
        if not borrowers_name or not borrowers_ID:
            raise ValueError(" Borrowers name and Borrower's ID cannot be empty!")
        
        # Check if the borrower exists and has borrowed this book
        borrower_found = False
        for rental in Borrowers_List:
            if rental["borrowers_ID"] == borrowers_ID and rental["book_title"] == book_title and rental["status"] == "Borrowed":
                borrower_found = True
                break
        if not borrower_found:
            print("Error: Borrower not found or book was not borrowed.")
            return
        
        # Check if borrower has already returned the book
        for rental in Borrowers_List:
            if rental["borrowers_ID"] == borrowers_ID and rental["book_title"] == book_title:
                if rental["status"] == "Returned":
                    print("Error: You have already returned this book.")
                    return
                
            rental["status"] = "Returned"  # Mark as returned
            break
        
        # Calculate return date and due date    
        borrow_date = datetime.now()
        return_date = datetime.now()
        due_date = borrow_date + timedelta(days=7)  # 7-day due date
        days_late = (return_date - due_date).days
        
        # Calculate fine if late
        fine = max(0, days_late * Fine_Per_Day) if days_late > 0 else 0

        
        # Increase quantity by 1
        Inventory[book_title]["quantity"] +=1
        Inventory[book_title]["available"] = Inventory[book_title]["quantity"] > 0
        
        print(f" {borrowers_name} with ID {borrowers_ID} has  successfully returned {book_title}  by {Inventory[book_title]["author"]}")
        print(f" You returned the book {days_late} days late. A fine of ${fine} must be paid.")
        print(f" retutn_date: {return_date.strftime("%Y-%m-%d %H:%M:%S")}")
        
        if days_late <= 0:
            print("No fine applied. Book returned on time.")
            
    else:
        print("Invalid book title, book not found in the Inventory")
# List of borrowers        
def display_borrowers():
    """Displays the list of borrowers and their borrowed books."""
    if Borrowers_List:
        print("List of Borrowers:")
        for rental in Borrowers_List:
            print(f"Name: {rental['name of borrower']}")
            print(f"Borrower's ID: {rental['borrowers_ID']}")
            print(f"Book Title: {rental['book_title']}")
            print(f"Borrow Date: {rental['borrow_date']}")
            print(f"Due Date: {rental['due_date']}")
            print(f"Status: {rental['status']}")
            print("-" * 40)  
    else:
        print("No borrowers found.")

        
# Main Function

def main():
    """Displays the main menu and allows the user to interact with the system.
    """
    
    print("Welcome to the Library Manager!")

    
    while True:
        print("\n Library Manager Menu")
        print("1. Add/Update a Book")
        print("2. Display Inventory")
        print("3. Rent a Book")
        print("4. Return a Book")
        print("5. Display Borrowers")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            display_Inventory()
        elif choice == "3":
            rent_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            display_borrowers()
        elif choice == "6":
            print("Thank you for using the Library Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
# Run the program
if __name__ == "__main__":
    main()
        

        
    
    
    
            
        
        
    
    




