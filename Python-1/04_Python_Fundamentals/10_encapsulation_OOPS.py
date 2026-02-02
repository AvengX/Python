class BankAccount:
    def __init__(self,name,balance):
        self.name=name #public
        self.__balance=balance  #private - data mangling

    def get_balance(self):  #getters
        return self.balance

    def set_balance(self,new_balance):   #setters
        self.__balance=new_balance

acc1=BankAccount("Rahul Kumar",10_000)

acc1.set_balance(30_000)
print(acc1.name,acc1._BankAccount__balance)