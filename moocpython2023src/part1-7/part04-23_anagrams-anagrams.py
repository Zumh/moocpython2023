# Write your solution here
def anagrams(string_first:str, string_second:str):
    return sorted(string_first) == sorted(string_second)