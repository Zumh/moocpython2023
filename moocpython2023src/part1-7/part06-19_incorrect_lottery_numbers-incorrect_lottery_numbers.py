# Write your solution here

def verify_week_format(week:str):
    # check if the week format is correct 
    number_of_week = 0
    # split the week 
    week = week.split(" ")
    if len(week) != 2 or week[0] != "week":
        raise ValueError(f"wrong week format")
    number_of_week = int(week[1])
    
    


def verify_seven_numbers(numbers:str):

    number_list = numbers.split(",")

    MAX_NUMBER = 39
    MIN_NUMBER = 1
    # check the length is exactly length
    if len(number_list) != 7:

        raise ValueError("Not short length")
    
    #[1,2,3,4,..]
    # convert the string to integer 
    for indx in range(len(number_list)):
        number = number_list[indx]
        current_number = int(number.replace("\n","").strip())


        
        # check the range
        if not(MIN_NUMBER <= current_number <= MAX_NUMBER):

            raise ValueError(f"Out of range from 1-39 inclusively {current_number}")
        
        # check if the number appears in the rest of the list
        if number in number_list[indx+1:]:

            raise ValueError(f"Current number appear twice in the list {current_number}")


def filter_incorrect():

    with open("lottery_numbers.csv", "r") as loterry_file, open("correct_numbers.csv", "w") as correct_format:
        for content in loterry_file:
            # split the week format from the string 
            lottery_data = content.split(";")
            week = lottery_data[0]
            numbers = lottery_data[1]

            try:
                # verity the week is in a correct format 
                verify_week_format(week)
                verify_seven_numbers(numbers)
                correct_format.write(content)
            except:
                pass

