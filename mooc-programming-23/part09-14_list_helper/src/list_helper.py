# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def greatest_frequency(cls,my_list: list)->int:
        """
        returns the most common item on the list
        """
        frequency = {}
        for number in my_list:
            if number not in frequency:
                frequency[number] = 0
            frequency[number] += 1
        max_freq_value = 0
        max_freq_number = 0
        for key, value in frequency.items():
            if max_freq_value < value:
                max_freq_value = value 
                max_freq_number = key

        return max_freq_number
    @classmethod
    def doubles(cls, my_list: list)->int:
        """
        Returns the number of unique items which appear at least twice on the list
        """
        frequency_table = {}

        count_appear_twice = 0

        for number in my_list:
            if number not in frequency_table:
                frequency_table[number] = 0
            frequency_table[number] += 1
            if frequency_table[number] == 2:
                count_appear_twice += 1
        
        return count_appear_twice

if __name__ == "__main__":
    #numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    #print(ListHelper.greatest_frequency(numbers))
    numbers = [3, 2, 3, 2, 2, 3, 1, 2, 4, 5, 5, 6]
    print(ListHelper.doubles(numbers))