class MUser:
    userName = ""
    userPassword = ""
    userRole = ""
    def __init__(self, userName, userPassword, userRole):
        self.userName = userName
        self.userPassword = userPassword
        self.userRole = userRole
    def isAdmin(self):
        if (self.userRole == "Admin"):
            return True
        else:
            return False