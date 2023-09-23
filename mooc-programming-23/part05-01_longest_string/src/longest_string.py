# Write your solution here

def longest(strings: list[str])->list[str]:
    longest_strings = strings[0]
    for a_string in strings:
        if len(a_string) >= len(longest_strings):
            longest_strings = a_string
    return longest_strings
        
