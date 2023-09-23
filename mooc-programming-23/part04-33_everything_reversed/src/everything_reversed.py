# Write your solution here

def everything_reversed(my_string:list[str])->list[str]:

    reverse_str = []
    for word in my_string:
        reverse_str.append(word[::-1])
    return reverse_str[::-1]