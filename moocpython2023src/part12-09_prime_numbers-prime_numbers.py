# Write your solution here
def check_prime(number: int)->bool:
    begin = 2 
    prime = True 
    while begin <= number - 1:
        if number % begin == 0:
            prime = False 
            break
        begin += 1
    return prime
def prime_numbers():
    start = 2
    while True:
        if check_prime(start):
            # we yield or remember and return if only that number is a prime
            yield start
        
        start += 1 
if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))