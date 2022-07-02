from importlib.resources import path
import os
from time import sleep
from pip import main
from CredentialDL import CredentialDL
from CredentialUL import CredentialUL

def main():
    path="Data.txt"
    #CredentialDL.readDataFromFile(path)
    option =0
    while(option!=3):
        os.system("cls")
        option=CredentialUL.menu()
        if(option==1):
            user=CredentialUL.takeInputWithoutRole()
            user=CredentialDL.SignIn(user)
            if(user!=None):
                if(user.isAdmin()):
                    if(user.isAdmin()):
                        print("This is admin")
                        #Admin menu 
                    else:
                        print("This is user")
                        #user menu
                        sleep(3)
        elif(option==2):
            user=CredentialUL.takeInputFromConsole()
            CredentialDL.addUserIntoList(user)
            CredentialDL.storeUserIntoFile(user,path)


#Main Function
if(__name__=="__main__"):
    main()

