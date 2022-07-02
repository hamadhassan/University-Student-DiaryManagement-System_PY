import os.path
from Credential import Credential

class CredentialDL:
    credentialist=[]

    @staticmethod
    def addUserIntoList(user):
        CredentialDL.credentialist.append(user)

    @staticmethod
    def SignIn(user):
        for storeUser in CredentialDL.credentialist:
            if(storeUser.username==user.username and storeUser.password==user.password):
                return storeUser
        return None

    @staticmethod
    def pareseData(line):
        line=line.split(",")
        return line[0],line[1],line[2]

    @staticmethod
    def readDataFromFile(path):
        if(os.path.exists(path)):
            fileVariable=open(path,'r')
            records=fileVariable.read().split("\n")
            fileVariable.close()
            for line in records:
                username,password,role=CredentialDL.pareseData(line)
                user=Credential(username,password,role)
                CredentialDL.addUserIntoList(user)
                return True
        else:
            return False
            
    @staticmethod 
    def storeUserIntoFile(user,path):
        file=open(path,'a')
        file.write("/n"+user.username+","+user.password+","+user.role)
        file.close()


