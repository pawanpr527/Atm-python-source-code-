class Atm:
    def __init__(self) :            # __init is a constructer, we we make a object of this class ,
        # print("hello")                  #  the function and data inside __init__ automatically execute to our object 
        self.balance = 0  #in python constructor name is denoted by (__init__) only
        self.pin = ""
        self.menu()

    def menu(self) :
       user_input = input("""
                          Hello,how would you like to proceed ?
                          1. Enter 1 to create pin
                          2. Enter 2 to deposit
                          3. Enter 3 to withdraw
                          4. Enter 4 to check_balance
                          5. Enter 5 to exit
                          """)
       if user_input == "1":
           self.create_pin()
       elif user_input == "2":
           self.deposit_()
       elif user_input== "3":
           self.withdraw_()
       elif user_input == "4":
           self.check_balance()
       else:
           print("Exit ")

    def create_pin(self):
        self.pin = input("Pin : ")  
        print("Pin set successfully")   

    def deposit_(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount "))
            self.balance = self.balance + amount
            print("Deposit successfully")
        else :
            print("Invalid Pin")   
    
    def withdraw_(self):
         temp = input("Enter your pin")
         if temp == self.pin:
            money = int(input("Enter the amount "))
            if money<self.balance:
                self.balance = self.balance - money
                print("withdraw successfully ",money)
            else:
                print("insufficient funds")
         else:
             print("Invalid Pin")    

    def check_balance(self)  :
        temp = input("Enter your pin")
        if temp == self.pin:
            print(self.balance)
        else:
            print("invalid pin")
         

sbi = Atm() 
sbi.deposit_()      
sbi.check_balance()
sbi.withdraw_()
sbi.check_balance()     

