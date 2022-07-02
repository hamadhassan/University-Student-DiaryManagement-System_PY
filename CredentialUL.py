from collections import UserList
from optparse import Option
from argon2 import PasswordHasher
from pyrsistent import optional
from Credential import Credential
class CredentialUL:
    @staticmethod
    def menu():
        print("1. SignIn")
        print("2. SignUp")
        print("Enter Option")
        option=int(input())
        return option

    @staticmethod
    def printList(credentialist):
        for user in credentialist:
            print(user.username,user.password,user.role)

    @staticmethod 
    def takeInputFromConsole():
        username=input("Enter username ")
        password=input("Enter password ")
        role=input("Enter role ")
        user1=Credential(username,password,role)
        return user1

    @staticmethod
    def takeInputWithoutRole():
        username=input("Enter username ")
        password=input("Enter password")
        user=Credential(username,password,None)
        return user