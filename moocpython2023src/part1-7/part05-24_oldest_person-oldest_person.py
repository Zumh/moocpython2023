# Write your solution here
def oldest_person(people: list):


    max_age = people[0]
    for person in people:

        if person[1] < max_age[1]:
            max_age = person

    return max_age[0]
