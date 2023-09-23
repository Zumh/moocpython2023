# Write your solution here
def older_people(people: list, year: int)->list:
    olders = []
    for person in people:
        if person[1] < year:
            olders.append(person[0])
    return olders 