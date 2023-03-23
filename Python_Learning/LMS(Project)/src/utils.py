'''

'''
from config import LMS

def take_input(purpose):
    flag = True
    while flag:
        try:
            type = int(input(f"Please enter options for {purpose}:")) ## Explicit Type Castings
            flag = False
        except Exception as e:
            print(f"You have entered wrong {purpose}")

    return type

def user_menu():
    flag = True
    while flag:
        print( "USER MENU:\n1. STUDENT\n2. TEACHER\n3. EXIT")
        input=take_input("User Menu")
        if input == 1:
            print("STUDENT MENU:\n1. Web Programming\n2. Rich Dad Poor Dad\n3. Data Structures")
        elif input == 2:
            print("TEACHER MENU:\n1. Artificial Intelligence\n2. Machine Learning\n3. Deep learning\n4. Advanced Python")
        elif input == 3:
            flag = False
            print("Returning back to Main Menu")
        else:
            print("WRONG INPUT")

def add_book():
    print("Welcome to Adding Books Page..")
    flag = True
    while flag:
        print("Do you want to add a book..y/n")
        input = input()
        if input == "y":
            bookName = input("Book Name:")
            bookAuthor = input("Book Author:")
            bookPrice = input("Book Price:" )
            bookFormat = input("Book Format: ")
            bookISBN = input("Book ISBN:")
            bookPublisher = input("Book Publisher:")
        else:
            flag = False