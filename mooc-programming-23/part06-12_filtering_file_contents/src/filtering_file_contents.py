# Write your solution here

def read_file(filename:str):
    problems = []
    with open(filename) as myfile:
        for content in myfile:
            problems.append(content.strip().split(";"))
    return(problems)
def ressemble_csv_format(solution:list)->str:
     # restructure the string 
    line = ""
    for value in solution:
        line += f"{value};"
    line = line[:-1] + "\n"
    return line
    
def write_file(filename:str, solutions:list):
    with open(filename,"w") as myfile:
        for solution in solutions:
            myfile.write(solution)

def filter_solutions():
    # read the file for folder
    solutions = read_file("solutions.csv")
    right_solution = []
    incorrect_solution = []
    substraction = "-"
    addition = "+"
    current_result = 0
    for solution in solutions:
        name_of_student = solution[0]
        result = int(solution[2])
        if substraction in solution[1]:
            numbers = solution[1].split(substraction)
            current_result = int(numbers[0]) - int(numbers[1])
        elif addition in solution[1]:
            numbers = solution[1].split(addition)
            current_result = int(numbers[0]) + int(numbers[1])

        line = ressemble_csv_format(solution)
        # correct
        if current_result == result:
            
            right_solution.append(line)
        else:
            incorrect_solution.append(line)
    
    # write correct file
    write_file("correct.csv", right_solution)
    # write incorrect file
    write_file("incorrect.csv",incorrect_solution)

"""
 # better solution
def filter_solutions():
    # Open all lines
    with open("solutions.csv") as source, open("correct.csv", "w") as correct_file, open("incorrect.csv", "w") as incorrect_file:
        for row in source:
            # Split into pieces
            pieces = row.split(";")
 
            calculation = pieces[1]
            result = pieces[2]
 
            # Addition or subtraction?
            if "+" in calculation:
                operands = calculation.split("+")
                # correct is True or False based on whether the calculation was correct or not
                correct = int(operands[0]) + int(operands[1]) == int(result)
            else:
                operands = calculation.split("-")
                # correct is True or False based on whether the calculation was correct or not
                correct = int(operands[0]) - int(operands[1]) == int(result)
 
            # Write to file
            if correct:
                correct_file.write(row)
            else:
                incorrect_file.write(row)
"""