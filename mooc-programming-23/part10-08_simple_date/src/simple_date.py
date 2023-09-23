# WRITE YOUR SOLUTION HERE:

class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        "assuming every month have 30 days"

        self.__day = day 
        self.__month = month 
        self.__year = year 
          
    def __days__(self)->int:
        return self.__year * 360 + self.__month * 30 + self.__day

    def __lt__(self, another: "SimpleDate")->bool:
        return self.__days__() < another.__days__()
    
    def __gt__(self, another: "SimpleDate")->bool:
        return self.__days__() > another.__days__()
        

    def __eq__(self, another: "SimpleDate")->bool:
        
        return self.__days__() == another.__days__()
    
    def __ne__(self, another: "SimpleDate")->bool:
        
        return self.__days__() != another.__days__()

    def __add__(self, another_day: int)->"SimpleDate":
     
        new_days = another_day + self.__day
        new_month = self.__month
        new_year = self.__year
        while new_days >= 30:
            
            new_month += (new_days // 30)
            new_days = new_days % 30

        while new_month >= 12:
            new_year += (new_month // 12)
            new_month = new_month % 12
        
        new_date = SimpleDate(new_days, new_month, new_year)
        return new_date
  

    def __sub__(self, another_day: "SimpleDate")->"SimpleDate":
        
        total_diff_days = self.__days__() - another_day.__days__()
        return abs(total_diff_days)
    def __str__(self)->str:
        return f"{self.__day}.{self.__month}.{self.__year}"
if __name__ == "__main__":  

    # part 1 - comparisons
    # d1 = SimpleDate(4, 10, 2020)
    # d2 = SimpleDate(28, 12, 1985)
    # d3 = SimpleDate(28, 12, 1985)

    # print(d1)
    # print(d2)
    # print(d1 == d2)
    # print(d1 != d2)
    # print(d1 == d3)
    # print(d1 < d2)
    # print(d1 > d2)

    # part 2 - increment
    # d1 = SimpleDate(4, 10, 2020)
    # d2 = SimpleDate(28, 12, 1985)

    # d3 = d1 + 3
    # d4 = d2 + 400

    # print(d1)
    # print(d2)
    # print(d3)
    # print(d4)

    # part 3 - subtract
    # d1 = SimpleDate(4, 10, 2020)
    # d2 = SimpleDate(2, 11, 2020)
    # d3 = SimpleDate(28, 12, 1985)

    # print(d2-d1)
    # print(d1-d2)
    # print(d1-d3)

    sd1 = SimpleDate(1, 4, 1800)
    sd2 = SimpleDate(3, 5, 1842)
    print(sd1-sd2)