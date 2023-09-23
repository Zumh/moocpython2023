# Write your solution here
def smallest_average(person1:dict, person2:dict, person3:dict):
    """
    smallest average
    {'name': 'Larry', 'result1': 3, 'result2': 1, 'result3': 1}
    """
    people = [person1, person2, person3]
    lowest_average = 10000
    lowest_average_person = {}
    for person in people:
        total = 0

        for indx in range(1,len(person)):
            total += person[f"result{indx}"]
        current_average = total/len(person)
        if lowest_average > current_average:
            lowest_average = current_average
            lowest_average_person = person
    return lowest_average_person

