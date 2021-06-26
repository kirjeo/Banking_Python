import pickle
import os








#uncle kenny rock!

class picler_class:

    def __init__(self, dictionary):
        if dictionary == {}:
            pass
        else:
            self.dictionary = dictionary
            self.balance = 0
            dictionary_of_users[self.dictionary['username']] = self.dictionary



    def load(self):
        try:
            picFile = open('names.pickle', 'rb')
            dictionary_of_users = pickle.load(picFile)
            picFile.close()
            return dictionary_of_users
        except:
            return {}

    def clear(self):
        self.dictionary = ''
        picFile = open('names.pickle', 'wb')
        pickle.dump(self.dictionary, picFile)
        picFile.close()

    def setbal(self, value):
        self.balance = value

    def withdraw(self, value, class_username):
        self.value = float(value)
        self.username = class_username
        i = True
        while i:
            if self.value > float(dictionary_of_users[self.username]['balance']):
                print("Error, You can not withdraw more than your current balance\nTry again")
                self.value = float(input("How much do you want to withdraw? "))
            elif self.value < 0:
                print("Error, You can not withdraw more than your current balance\nTry again")
                self.value = float(input("How much do you want to withdraw? "))
            else:
                dictionary_of_users[username]['balance'] = str(float(dictionary_of_users[username]['balance']) - float(self.value))
                print("Balance: " + dictionary_of_users[self.username]['balance'])
                i = False

        return dictionary_of_users

    def deposit(self, value, class_username):
        self.username = class_username
        self.value = float(value)
        i = True
        while i:
            if self.value < 0:
                print("Invalid deposit\nTry again")
                self.value = input("How much do you want to deposit? ")
            else:
                dictionary_of_users[self.username]['balance'] = str(float(dictionary_of_users[self.username]['balance']) + float(self.value))
                print("Balance: " + dictionary_of_users[self.username]['balance'])
                i = False

        return dictionary_of_users

'''class Account:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.balance = 0
        dictionary_of_users[self.dictionary['username']] = self.dictionary

    def setbal(self, value):
        self.balance = value

    def withdraw(self, value, class_username):
        self.value = float(value)
        self.username = class_username
        i = True
        while i:
            if self.value > float(dictionary_of_users[self.username]['balance']):
                print("Error, You can not withdraw more than your current balance\nTry again")
                self.value = float(input("How much do you want to withdraw? "))
            elif self.value < 0:
                print("Error, You can not withdraw more than your current balance\nTry again")
                self.value = float(input("How much do you want to withdraw? "))
            else:
                dictionary_of_users[username]['balance'] = str(float(dictionary_of_users[username]['balance']) - float(self.value))
                print("Balance: " + dictionary_of_users[self.username]['balance'])
                i = False

        return dictionary_of_users

    def deposit(self, value, class_username):
        self.username = class_username
        self.value = float(value)
        i = True
        while i:
            if self.value < 0:
                print("Invalid deposit\nTry again")
                self.value = input("How much do you want to deposit? ")
            else:
                dictionary_of_users[self.username]['balance'] = str(float(dictionary_of_users[self.username]['balance']) + float(self.value))
                print("Balance: " + dictionary_of_users[self.username]['balance'])
                i = False

        return dictionary_of_users'''


# make a class that can write and read to the pickle file
blank_dictionary = {}
picler = picler_class(blank_dictionary)
dictionary_of_users = picler.load()


def get_info():
    new_or_old = input("Do you want to\n1.Login\n2.Signup\n")
    if not new_or_old.isnumeric():
        print("Must enter a number!")
    return new_or_old





while True:
    #new_or_old = get_info()
    #picler.clear()

    picler.save(dictionary_of_users)
    new_or_old = input("Do you want to\n1.Login\n2.Signup\n")
    if new_or_old == "1" or new_or_old == "login":
        i = True
        while i:
            username = input("Username: ")
            if username in dictionary_of_users.keys():
                password = input("Password: ")
                if dictionary_of_users[username]['password'] == password:
                    print("You have logged in")
                    print("Balance: " + dictionary_of_users[username]['balance'])

                    i = True
                    while i:
                        dorw = input("Do you want to\n1.Deposit\n2.Withdraw\n3.Exit\n").lower()
                        if dorw == '1' or dorw == "deposit":
                            amount = input("How much do you want to deposit? ")
                            picler.deposit(amount, username)
                            i = False
                        elif dorw == '2' or dorw == "withdraw":
                            amount = input("How much do you want to withdraw? ")
                            picler.withdraw(amount, username)
                            i = False
                        elif dorw == '3' or dorw == "exit":
                            i = False
                        else:
                            print("Error, you did not chose any of the previous answers\nTry again")
                    i = False
                else:
                    print("Incorrect password")
            else:
                print("Username is not registered")
                print("Try Again")

    elif new_or_old == "2" or new_or_old == "signup":
        i = 1
        while i == 1:
            username = input("Set a Username: ").lower()
            if username in dictionary_of_users.keys():
                print("Username is already taken\nTry again")
            else:
                name = input("What is your name?: ")
                password = input("Set a password: ")
                balance = input("Set a balance: ")
                person = {'username': username, 'name': name, 'password': password, 'balance': balance}
                account = picler_class(person)
                break
        



2