# Write your solution here

def histogram(a_string:str):
    freq_table = {}
    for char in a_string:
        if char not in freq_table:
            freq_table[char] = 0
        freq_table[char] += 1
    # print the star or histogram of each character

    for key, value in freq_table.items():
        stars = "*" * value
        print(f"{key} {stars}")
