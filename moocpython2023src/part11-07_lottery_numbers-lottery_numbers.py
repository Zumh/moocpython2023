# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, week_number: int, numbers: list[int])->None:
        self.__week = week_number
        self.__numbers = numbers 
    
    def number_of_hits(self, input_number: list[int])->int:
        return len([number for number in input_number if number in self.__numbers])

    def hits_in_place(self, input_number: list[int])->int:
        return [number if number in self.__numbers else -1 for number in input_number]
if __name__ == "__main__":
    # Part 1 LNMatch
    # week5 = LotteryNumbers(5, [1,2,3,4,5,6,7])
    # my_numbers = [1,4,7,11,13,19,24]

    # print(week5.number_of_hits(my_numbers))

    # Part 2 LNMatch in Place
    week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
    my_numbers = [1,4,7,10,11,20,30]

    print(week8.hits_in_place(my_numbers))