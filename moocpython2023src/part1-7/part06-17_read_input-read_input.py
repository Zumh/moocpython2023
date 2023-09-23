# Write your solution here
def read_input(message, low_number, high_number):
    while True:
        try:
            input_str = int(input(message))
            number = int(input_str)
            if low_number <=number<=high_number:
                return number
        except:
            pass
        print(f"You must type in an integer between {low_number} and {high_number}")
    
