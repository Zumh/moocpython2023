
# print variable
def print_variable(command:str, variables:dict):

    # split the command string in to list and value
    values = command.split(" ")[-1]

    # check if the value is exists in the variable
    if values.isdigit():
        return int(values)
    # if not exist in dictionar list then print 
    else:

        return variables[values]


# A-Z with 0 vlues for each 
def prepare_variable(variables:dict):
    """
    Each program has 26 pre-defined variables, named A to Z. 
    Each variable has the value 0 when the program begins. 
    The notation [variable] refers to one of these 26 variables.
    """
    from string import ascii_uppercase

    value = 0
    for letter in ascii_uppercase:
        variables[letter] = value

# extract commands and values
def extract_helper(command:str, variables:dict)->tuple:
    command_list = command.split(' ')
    input_variable = command_list[1]
    input_values = command_list[2]
    values = 0
    if input_values.isdigit():
        values = int(input_values)
    else:
        values = variables[input_values]
    return input_variable, values


# add variable 
def add_values(command:str, variables:dict):
    # change value of specific variables from command
    input_variable, values = extract_helper(command, variables)
    variables[input_variable] += values

# subtract variable 
def subtract_values(command:str, variables:dict):
    # change value of specific variables from command
    input_variable, values = extract_helper(command, variables)
    variables[input_variable] =  variables[input_variable] - values

# multiply variable
def multiply_values(command:str, variables:dict):
    input_variable, values = extract_helper(command, variables)

    variables[input_variable] = values * variables[input_variable]


def mov_values(command:str, variables:dict):
    input_variable, values = extract_helper(command, variables)
    variables[input_variable] = values


def jump_location(command:str, program: list[str]):
    location_name = command.split(" ")[1]+":"
    indx_position = program.index(location_name)
    return indx_position 
def check_condition(commands:str, varialbes:dict):
    
    # parse variable A and B or left and Right 
   
    
    A,comparison,B = commands.split(' ')
    try:
        A = varialbes[A]
    except:
        A = int(A)
    try:
        B = varialbes[B]
    except:
        B = int(B)
    if (comparison == '!=' and A != B) or (comparison == '==' and A == B) or (comparison == '<=' and A <= B) or (comparison == '>=' and A >= B )or (comparison == '>' and A > B ) or (comparison == '<' and A < B ):
        return True
            
    return False

def run(program:list[str])->list[int]:

    # define variables from A-Z dictionary
    variables = {}
    prepare_variable(variables)

    # command result
    result = []
    indx = 0
    location = {}
    
    while indx < len(program):
        command = program[indx].split(' ')[0]
        commands = program[indx]
        # commands 
        if 'END' == command:
            break
        elif 'PRINT' == command:

            # call print command function
            result.append(print_variable(commands, variables))
        elif 'ADD' == command:
            # call add command function
            
            add_values(commands, variables)

        elif 'SUB' == command:
            # call sub command function

            subtract_values(commands, variables)
        
        elif 'MUL' == command:
            # call mul command function
            multiply_values(commands, variables)
        elif 'MOV' == command:
            # call mov command function
            mov_values(commands, variables)
        elif 'JUMP' == command:
            # jump to the indx value given by alphabet
            indx = jump_location(commands, program)
        elif 'IF' == command:
            # if condition true execute jump command
            find_jump_location = commands.find('JUMP')

            # find condition and check if that condition is true
            if check_condition(commands[len(command):find_jump_location].strip(), variables):
               indx = jump_location(commands[find_jump_location:], program)
    
        indx += 1
    
    return(result)
if __name__ == "__main__":
    # program2 = []
    # program2.append("MOV A 1")
    # program2.append("MOV B 10")
    # program2.append("begin:")
    # program2.append("IF A >= B JUMP quit")
    # program2.append("PRINT A")
    # program2.append("PRINT B")
    # program2.append("ADD A 1")
    # program2.append("SUB B 1")
    # program2.append("JUMP begin")
    # program2.append("quit:")
    # program2.append("END")
    # result = run(program2)
    # print(result)
    program = ['MOV A 10', 'start:', 'PRINT A', 'SUB A 1', 'IF A > 0 JUMP start', 'END']
    result = run(program)
    print(result)

"""
def value(x, data):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if x in characters:
        return data[characters.index(x)]
    else:
        return int(x)
 
def condition(a, condition, b):
    if condition == "==":
        return a == b
    if condition == "!=":
        return a != b
    if condition == "<":
        return a < b
    if condition == "<=":
        return a <= b
    if condition == ">":
        return a > b
    if condition == ">=":
        return a >= b
 
def run(program):
    length = len(program)
    row = 0
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    data = [0]*26
    result = []
    while True:
        if row == length:
            break
        parts = program[row].split(" ")
        if parts[0] == "PRINT":
            result.append(value(parts[1], data))
        if parts[0] == "MOV":
            data[characters.index(parts[1])] = value(parts[2], data)
        if parts[0] == "ADD":
            data[characters.index(parts[1])] += value(parts[2], data)
        if parts[0] == "SUB":
            data[characters.index(parts[1])] -= value(parts[2], data)
        if parts[0] == "MUL":
            data[characters.index(parts[1])] *= value(parts[2], data)
        if parts[0] == "JUMP":
            row = program.index(parts[1]+":")
            continue
        if parts[0] == "IF":
            if condition(value(parts[1], data), parts[2], value(parts[3], data)):
                row = program.index(parts[5]+":")
                continue
        if parts[0] == "END":
            break
        row += 1
    return result
"""