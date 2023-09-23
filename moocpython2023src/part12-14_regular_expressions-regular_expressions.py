# Write your solution here
import re

def is_dotw(my_string: str)->bool:
    """
    The function should return True if the string passed as an argument contains an abbreviation 
    for a day of the week (Mon, Tue, Wed, Thu, Fri, Sat, Sun).
    """    
    expression = "Mon|Tue|Wed|Thu|Fri|Sat|Sun"    

    if re.search(expression,my_string):
        return True 
    else:
        return False
def all_vowels(my_string: str):
    expression = "^[aeiou]+$"
    if re.search(expression, my_string):
        return True 
    else:
        return False 

def time_of_day(my_string: str)->bool:
    expression = "([0-1][0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])"
    if re.search(expression, my_string):
        return True 
    else:
        return False 
if __name__ == "__main__":

    # Part 1 literal search for weekday
    # print(is_dotw("Mon"))
    # print(is_dotw("Fri"))
    # print(is_dotw("Tui"))

    # Part 2 check for vowels
    # print(all_vowels("eioueioieoieou"))
    # print(all_vowels("autoooo"))

    # Part 3 time of the day
    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))


    """
    import re
 
def is_dotw(my_string: str):
    return re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun", my_string) is not None
 
def all_vowels(my_string: str):
    return re.search("^[aeiou]*$", my_string) is not None
 
def time_of_day(my_string: str):
    return re.search("^([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$", my_string) is not None
    """