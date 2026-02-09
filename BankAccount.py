class BankAccount:
    titleOfBank = "Banky the Bank"
    def __init__(self,customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self,amount):
        self.current_balance += amount

    def withdraw(self,amount):
        if self.minimum_balance <= (self.current_balance - amount):
            self.current_balance -= amount
        else:
            print("Withdrawal Invalid")


    def print_customer_information(self):
        print(f'Customer name:  { self.customer_name}')
        print(f'Customer current balance: ${self.current_balance}')
        print(f'Customer minimum balance: ${self.minimum_balance}')
        print(f'Bank Title: {self.titleOfBank}')
#tests below
bank1 = BankAccount("Jennifer", 500, 50)
bank1.deposit(1000)
bank1.withdraw(25)
bank1.print_customer_information()
bank1.withdraw(50000)
