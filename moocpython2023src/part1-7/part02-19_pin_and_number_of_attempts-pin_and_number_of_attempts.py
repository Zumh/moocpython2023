"""
Please write a program which keeps asking the user for a PIN code until they type in the correct one, which is 4321. 
The program should then print out the number of times the user tried different codes.
PIN: 3245
Wrong
PIN: 1234
Wrong
PIN: 0000
Wrong
PIN: 4321
Correct! It took you 4 attempts
"""
# Write your solution here
input_PIN = ""
PIN = "4321"
count_attempt = 0

while input_PIN != PIN:

    input_PIN = input("PIN: ")
    count_attempt += 1
    if PIN != input_PIN:
        print("Wrong")
if count_attempt == 1:
    print(f"Correct! It only took you one single attempt!")    
elif count_attempt > 1:
    print(f"Correct! It took you {count_attempt} attempts")