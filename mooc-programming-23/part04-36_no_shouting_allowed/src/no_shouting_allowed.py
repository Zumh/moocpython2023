# Write your solution here
def no_shouting(my_list:list[str])->list[str]:
    
    small_list = []
    for word in my_list:
        if not word.isupper():
            small_list.append(word)
    return small_list