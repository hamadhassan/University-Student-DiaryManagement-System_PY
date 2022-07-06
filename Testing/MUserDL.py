import os.path
from MUser import MUser
class MUserDL:
    usersList = []
    @staticmethod
    def addUserIntoList(user):
        MUserDL.usersList.append(user)
    @staticmethod
    def SignIn(user):
        for storedUser in MUserDL.usersList:
            if(storedUser.userName == user.userName and storedUser.userPassword == user.userPassword):
                return storedUser
        return None
    @staticmethod
    def parseData(line):
        line = line.split(",")
        return line[0], line[1], line[2]
    @staticmethod
    def readDataFromFile(path):
        if (os.path.exists(path)):
            fileVariable = open(path, 'r') 
            records = fileVariable.read().split("\n")
            fileVariable.close()
            for line in records:
                userName, userPassword, userRole = MUserDL.parseData(line)
                user = MUser(userName, userPassword,userRole)
                MUserDL.addUserIntoList(user)
                return True
        else:
            return False
    @staticmethod
    def storeUserIntoFile(user, path):
        file = open(path, 'a')
        file.write("\n" + user.userName + "," +
        user.userPassword + "," + user.userRole)
        file.close