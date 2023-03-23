'''
This is main program
In main file we need to write only "business logic".

'''
#Here we are appending this system path in this file.BCS sometimes there may be chance that our "python interpreter or python program" is not able to find this "util.py"  file.                                       
import sys    
sys.path.append("./src")                      
from utils import (take_input, user_menu)
def main():
    print("welcome to the LMS..!")
    
    flag = True
    while flag:
        print("Select your type: \n1.USER\n2.ADMIN\n3.Exit")
        type = take_input("Main Menu")
        if type == 1:
            user_menu()
        elif type == 2:
            print("ADMIN MENU:\n1. Add Book\n2. Add User\n3. Remove User\n4. Remove Book")
        elif type == 3:
            print("Exiting.....")
            flag = False
        else:
            print("Please select either 1/2/3")

if __name__ ==  "__main__":
    main()

