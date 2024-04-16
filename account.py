class Account:  #making the class name Account which will simply take two arguments balance and account_number  
    def __init__(self,balance,account_number):
        self.balance = balance
        self.account_number = account_number

    #to debit the amount
    def debit(self,amount):
        self.balance -= amount
        print(f"The debit amount: ${amount}")
        print(f"The remaining amount: ${self.remain()}")  #here we are simply using the function with self because we know that amount would be different for all object
    

    # to credit the amount
    def credit(self,amount):
        self.balance+=amount
        print(f"\n\nThe Credited amount: ${amount}")
        print(f"The remaining amount: ${self.remain()}")

    # to return the remaining the amount
    def remain(self):
        return self.balance            

account_1 = Account(100000,45678)
debit_amount = int(input("Enter the amount which you want to depit: "))
credit_amount =int(input("Enter the amount which you wnat to credit: "))
account_1.debit(debit_amount)
account_1.credit(credit_amount)