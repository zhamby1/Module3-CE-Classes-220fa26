#inheritance is the ability to inherit like actions,data or functions from a parent class to a child class 
#it is called a is-a relationship...Parent class called animal and a child class called Dog where dog is an animal
#it can inherit all the functions and data attributes while at the same time modifying or updating those things to give it additional features

#create a checking account class that can deposit money

#base class/parent class
#watch this first them comeback: https://www.youtube.com/watch?v=oROcVrgz91Y&list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_&index=32

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

#now my bank has expanded and I want to make a savings account...savings accounts have some of the same things I want from checking, but I want a savings balance and a percentage match from the bank everytime I deposit funds
#to inherit put the class you want to inherit from in the ()

class Savings_Account(Checking_Account):
    def __init__(self,id_number,name,balance,savings_balance):
        #call the parents class init method cause that doesnt change
        super().__init__(id_number,name,balance)
        self.savings_balance = savings_balance

    #we can either use the above methods, or we can override with them with the same name
    def print_details(self):
        print(self.id_number)
        print(self.name)
        print(self.balance)
        print(self.savings_balance)

    #deposit we want to add 2% of whatever money is deposited into the account each time we make a deposit
    def deposit(self,value):
        matching_money = value * 0.02
        self.savings_balance = self.savings_balance + value + matching_money




zach_savings = Savings_Account(324243,"Zach Hamby",500.00,1000.00)
zach_savings.print_details()
print("************************************")
zach_savings.deposit(1000.00)
zach_savings.print_details()
