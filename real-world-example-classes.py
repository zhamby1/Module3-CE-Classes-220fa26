#create a checking account class that can deposit money

class Checking_Account:
    def __init__(self,id_number,name,balance):
        self.id_number = id_number
        self.name = name
        self.balance = balance

    def print_details(self):
        print(self.id_number)
        print(self.name)
        print(self.balance)

    def deposit(self,value):
        self.balance = self.balance + value

    def withdrawl(self,value):
        if self.balance - value <= 0:
            print("Cannot withdrawl...will go over the amount you have left")
        else:
            self.balance = self.balance - value



zach_hamby = Checking_Account(132432, "Zach Hamby", 500.00)
zach_hamby.print_details()

print("**************************")

random_person = Checking_Account(4546451, "Tim Johnson", 1000.00)
random_person.print_details()

print("***************************")

random_person.deposit(1200.00)
random_person.print_details()

print("****************************")

zach_hamby.withdrawl(1000.00)
zach_hamby.print_details()
