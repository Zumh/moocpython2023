# WRITE YOUR SOLUTION HERE:


class BankAccount:

    def __init__(self, name: str, account: str, balance: float)->None:
        self.__name = name 
        self.__account = account 
        self.__balance = balance 
    
    def deposit(self, amount: float):
        "Depositing money to the account"
        self.__balance += amount
        self.__service_charge()

    def withdraw(self, amount: float):
        "for withdrawing money from the account"
        service_charge = self.__balance * (1/100)
        # calculate the total charge including service charge
        balance_left = self.__balance - (amount + service_charge)
        if balance_left >= 0:
            self.__balance -= amount 
            self.__service_charge()
        else:
            raise ValueError("Bank is empty can't with draw")

    @property 
    def balance(self)->int:
        return self.__balance 
    
    def __service_charge(self):
        "decrse balance by 1% percent. deposit or withrdraw. Only after operations are completed"
        service_balance = self.__balance * (1/100)
        self.__balance -= service_balance

if __name__== "__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)