# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __convert_cents(self, money: int, cents: int)->float:
        current_money = money + (cents/100)
        return current_money
        
    def __str__(self):
        cents = self.__convert_cents(self.__euros, self.__cents)
        return f"{cents:.02f} eur"

    def __eq__(self, another: "Money")->bool:
        current_money = self.__convert_cents(self.__euros, self.__cents)
        another_money = self.__convert_cents(another.__euros, another.__cents)
        return current_money == another_money
    
    def __gt__(self, another: "Money")->bool:
        current_money = self.__convert_cents(self.__euros, self.__cents)
        another_money = self.__convert_cents(another.__euros, another.__cents)
        return current_money > another_money

    def __lt__(self, another: "Money")->bool:
        current_money = self.__convert_cents(self.__euros, self.__cents)
        another_money = self.__convert_cents(another.__euros, another.__cents)
        return current_money < another_money

    def __ne__(self, another: "Money")->bool:
        current_money = self.__convert_cents(self.__euros, self.__cents)
        another_money = self.__convert_cents(another.__euros, another.__cents)
        return current_money != another_money
    
    def __add__(self, another: "Money")->"Money":
        euros = self.__euros + another.__euros 
        cents = self.__cents + another.__cents 
        return Money(euros, cents)

    def __sub__(self, another: "Money")->"Money":
        euros = self.__euros - another.__euros 
        cents = self.__cents - another.__cents
        difference = self.__convert_cents(euros, cents)
        if difference < 0:
            raise ValueError("a negative result is not allowed")
        return Money(euros, cents)



    
    


if __name__ == "__main__":
    # Part 1 - str 
    # e1 = Money(4, 10)
    # e2 = Money(2, 5)
    # print(e1)
    # print(e2)

    # Part 2 - Equals amounts
    # e1 = Money(4, 10)
    # e2 = Money(2, 5)
    # e3 = Money(4, 10)

    # print(e1)
    # print(e2)
    # print(e3)
    # print(e1 == e2)
    # print(e1 == e3)

    # Part 3 - Other comparison operators 
    # e1 = Money(4, 10)
    # e2 = Money(2, 5)

    # print(e1 != e2)
    # print(e1 < e2)
    # print(e1 > e2)

    # Part 4 - Addition and subtraction 
    # e1 = Money(4, 5)
    # e2 = Money(2, 95)

    # e3 = e1 + e2 
    # e4 = e1 - e2 

    # print(e3)
    # print(e4)

    # e5 = e2 - e1 

    # Part 5 - The value must not be directly accessible
    print(e1)
    e1.euros = 1000
    print(e1)

"""
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents
 
    def __str__(self):
        # f-string has a handy feature for adding leading zeros:
        # :02d for example means, that output has at least 2 digit
        return f"{self.__euros}.{self.__cents:02d} eur"
 
    # Helper method for returning the value in cents
    # --> makes the comparisons easier
    def __value(self):
        return self.__euros * 100 + self.__cents
 
    # Another helper method which converts cents to value
    def __set_value(self, cents: int):
        self.__euros = cents // 100
        self.__cents = cents - self.__euros * 100
 
    def __eq__(self, other: "Money"):
        return self.__value() == other.__value()
 
    def __lt__(self, other: "Money"):
        return self.__value() < other.__value()
 
    def __gt__(self, other: "Money"):
        return self.__value() > other.__value()
 
    def __ne__(self, other: "Money"):
        return self.__value() != other.__value()
 
    def __add__(self, other: "Money"):
        msum = Money(0,0)
        msum.__set_value(self.__value() + other.__value())
        return msum
 
    def __sub__(self, other: "Money"):
        difference = self.__value() - other.__value()
        if difference < 0:
            raise ValueError("a negative result is not allowed")
        dmoney = Money(0,0)
        dmoney.__set_value(self.__value() - other.__value())
        return dmoney

"""