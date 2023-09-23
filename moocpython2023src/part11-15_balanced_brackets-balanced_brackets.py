
def balanced_brackets(my_string: str):
    
    if len(my_string) == 0:
        return True 

    if my_string[0] == '(' and my_string[-1] == ']' or my_string[0] == '[' and my_string[-1] == ')':
        return False 
    elif my_string[0] in ')]' or (my_string[-1] in '[('):
        return False
    elif my_string[0] in '[(' and not (my_string[-1] in '])'):
        return balanced_brackets(my_string[:-1])
    elif my_string[-1] in '])' and not (my_string[0] in '[('):
        return balanced_brackets(my_string[1:])
    

    return balanced_brackets(my_string[1:-1])
 

   
if __name__ == "__main__":
    ok = balanced_brackets("([([])])")
    print(ok)

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)

    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("(()]")
    print(ok)

    # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok)

    # ok = balanced_brackets("(((())))")
    # print(ok)

    # # # there is one closing bracket too many, so this produces False
    # ok = balanced_brackets("()())")
    # print(ok)

    # # this one starts with a closing bracket, False again
    # ok = balanced_brackets(")()")
    # print(ok)

    # # this produces False because the function only handles entirely nested brackets
    # ok = balanced_brackets("()(())")
    # print(ok)

    # ok = balanced_brackets("(Hello)")
    # print(ok)


    """
    The core idea is focus on matching brackets and ignoring none brackets.
    Return true if there is no more pair to find in the string
    If we couldn't find a pair then it will be false
    
    def balanced_brackets(mj: str):
    # string is empty, so it is ok
    if len(mj) == 0:
        return True
 
    # if first character is not any bracket, let's eat it away
    if not mj[0] in "()[]":
        return balanced_brackets(mj[1:])
 
    # if last is not any bracket, let's eat it away
    if not mj[-1] in "()[]":
        return balanced_brackets(mj[:-1])
    
    # now is known that first and last characters are brackets
    # check if they are a pair
    if mj[0]=="(" and mj[-1]==")":
        return balanced_brackets(mj[1:-1])
    if mj[0]=="[" and mj[-1]=="]":
        return balanced_brackets(mj[1:-1])
 
    # were not, so this string is not ok
    return False
 
 
    # remove first and last character
    """