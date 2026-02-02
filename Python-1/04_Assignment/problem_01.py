class BankAccount:
    def __init__(self,account_number,owner_name,balance):
        self.account_number=account_number
        self.owner_name=owner_name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited {amount} and balance is {self.balance}")

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"Withdraw amount {amount} and balance is {self.balance}")
        else:
            print("Insufficient funds")    

    def check_balance(self):
        print(f"Current balance for {self.owner_name} is {self.balance}")

acc=BankAccount(1234,"Ayush",50_000)
acc.deposit(1000)
acc.withdraw(2000)
acc.check_balance()
