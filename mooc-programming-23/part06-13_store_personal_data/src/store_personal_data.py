# Write your solution here
def store_personal_data(person: tuple):
    with open("people.csv","a") as myfile:

            name = person[0]
            age = str(person[1])
            height = str(person[2])
            myfile.write(f"{name};{age};{height}\n")

