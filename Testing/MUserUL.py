from MUser import MUser
class MUserUI:
    @staticmethod
    def menu():
        print("1. SignIn")
        print("2. SignUp")
        print("Enter Option")
        option = int(input())
        return option
    @staticmethod
    def printList(usersList):
        for user in usersList:
            print(user.userName,user.userPassword, user.userRole)