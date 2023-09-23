# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name
class Room:
    def __init__(self) -> None:
        self.persons = []

    def add(self, person: Person):       
        "add(person: Person) adds the person given as an argument to the room."
        self.persons.append(person)

    def is_empty(self):
        "is_empty() returns True or False depending on whether the room is empty."
        return len(self.persons) == 0 

    def print_contents(self):
        "print_contents() prints out the contents of the list of persons in the room."
        combined_height = 0
        for person in self.persons:
            combined_height += person.height
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {combined_height} cm")
        for person in self.persons:
            print(f"{person} ({person.height} cm)")
    
    def shortest(self)->Person:
        if self.is_empty():
            return None
        min_height_person = self.persons[0]
        for person in self.persons:
            if min_height_person.height > person.height:
                min_height_person = person
        return min_height_person

    def remove_shortest(self)->Person:
        shortest_person = self.shortest()
        if shortest_person:
            shortest_person = self.persons.pop(self.persons.index(shortest_person))
        return shortest_person
if __name__ == "__main__":
    # part 1: Room
    # room = Room()
    # print("Is the room empty?", room.is_empty())
    # room.add(Person("Lea", 183))
    # room.add(Person("Kenya", 172))
    # room.add(Person("Ally", 166))
    # room.add(Person("Nina", 162))
    # room.add(Person("Dorothy", 155))
    # print("Is the room empty?", room.is_empty())
    # room.print_contents()

    # part 2: shortest person

    # room = Room()

    # print("Is the room empty?", room.is_empty())
    # print("Shortest:", room.shortest())

    # room.add(Person("Lea", 183))
    # room.add(Person("Kenya", 172))
    # room.add(Person("Nina", 162))
    # room.add(Person("Ally", 166))

    # print()

    # print("Is the room empty?", room.is_empty())
    # print("Shortest:", room.shortest())

    # print()

    # room.print_contents()

    # Part 3: remove shortest person
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
