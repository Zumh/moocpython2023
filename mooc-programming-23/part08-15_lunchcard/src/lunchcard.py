# Write your solution here:
class LunchCard:
    def __init__(self, balance: float) -> None:
        if balance >= 0:
            self.balance = balance 

    def __str__(self) -> str:
        return f"The balance is {self.balance:.01f} euros"

    def eat_lunch(self):
        """
        eat_lunch subtracts 2.60 euros from the balance on the card

        """
        current_balance = self.balance - 2.60
        if current_balance >= 0:
            self.balance = current_balance
    def eat_special(self):
        """
        eat_special subtracts 4.60 euros from the balance on the card
        """
        current_balance = self.balance - 4.60
        if current_balance >= 0:
            self.balance = current_balance

    def deposit_money(self, deposit_money:int):
        """
        raise Value error if deposity money is below zero
        """
        if deposit_money < 0:
            raise ValueError("deposit money is below zero cannot add")
        else:
            self.balance += deposit_money
peters_card = LunchCard(20)
graces_card = LunchCard(30)
peters_card.eat_special()
graces_card.eat_lunch()
print(f"Peter: {peters_card}\nGrace: {graces_card}")
peters_card.deposit_money(20)
graces_card.eat_special()
print(f"Peter: {peters_card}\nGrace: {graces_card}")
peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)
print(f"Peter: {peters_card}\nGrace: {graces_card}")
