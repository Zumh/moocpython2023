# Write your solution here
def palindromes(word:str):
    left = 0
    right = len(word)-1
    is_palindrome = True
    while left < right and is_palindrome == True:
        if word[left] != word[right]:
            is_palindrome = False
        left += 1
        right -= 1
    return is_palindrome

is_palindrome = False
while is_palindrome == False:
    word = input("Please type in a palindrome: ")
    is_palindrome = palindromes(word)
    if is_palindrome == False:
        print("that wasn't a palindrome")
    else:
        print(f"{word} is a palindrome!")

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
