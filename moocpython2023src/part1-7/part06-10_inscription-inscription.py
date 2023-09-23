# Write your solution here

who = input("Whom should I sign this to: ") 
filename = input("Where shall I save it: ")
with open(filename,"w") as myfile:
    myfile.write(f"Hi {who}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")