# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []
        self.count = 0

    def add_number(self, number:int):
        """
        the method add_number adds a new number to the statistical record
        """
        self.numbers.append(number)
        self.count += 1
    def count_numbers(self):
        """
        the method count_numbers returns the count of how many numbers have been added
        """
        self.count =  len(self.numbers)
        return self.count
    def get_sum(self):
        return sum(self.numbers)
    
    def average(self):
        try:
            return self.get_sum()/self.count_numbers()
        except ZeroDivisionError:
            return self.get_sum()/1

stats = NumberStats()
even_stat = NumberStats()
odd_stat = NumberStats()

input_number = 0
while input_number >= 0 :
    input_number = int(input("Please type in integer numbers: "))
    if input_number >= 0:
        
        stats.add_number(input_number)
        
        if input_number % 2 == 0:
            even_stat.add_number(input_number)
        else:
            odd_stat.add_number(input_number)



print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", even_stat.get_sum()) 
print("Sum of odd numbers:", odd_stat.get_sum())