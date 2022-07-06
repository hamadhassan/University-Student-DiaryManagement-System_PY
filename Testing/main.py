# Including Libraries
from MUserDL import MUserDL
from MUserUL import MUserUI
import os
from time import sleep
# Defining Main Function
def main():
    path = "Data.txt"
    MUserDL.readDataFromFile(path)
    option = 0
    while (option != 3):
        os.system("cls")
        option = MUserUI.menu()
        if (option == 1):
            user = MUserUI.takeInputwithOutRole()
            user = MUserDL.SignIn(user)
            if (user != None):
               if (user.isAdmin()):
                print("This is Admin")
                    #Admin Menu
            else:
                print("This is User")
                #User Menu
            sleep(3)
        elif (option == 2):
            user = MUserUI.TakeInputFromConsole()
            MUserDL.addUserIntoList(user)
            MUserDL.storeUserIntoFile(user, path)
            
if __name__ == "__main__":
    main()