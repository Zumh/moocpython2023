# WRITE YOUR SOLUTION HERE:
class Present:
    """
    The name of the present: ABC Book
    The weight of the present: 2
    Present: ABC Book (2 kg)
    """

    def __init__(self, book_name:str, book_weight:int) -> None:
        self.name = book_name
        self.weight = book_weight
    
    def __str__(self) -> str:
        return f"{self.name} ({self.weight} kg)"

class Box:
    def __init__(self) -> None:
        self.presents = []

    def add_present(self, present: Present):
        """
        add_present(self, present: Present) which adds the present given as an argument to the box. 
        The method has no return value.
        """
        self.presents.append(present)

    def total_weight(self):
        """
        total_weight(self) which returns the combined weight of the presents in the box.
        """
        total_present_weight = 0
        for present in self.presents:
            total_present_weight += present.weight
        return total_present_weight
    
if __name__=="__main__":
    # Part 1 - The Present class
    # book = Present("ABC Book", 2)

    # print("The name of the present:", book.name)
    # print("The weight of the present:", book.weight)
    # print("Present:", book)

    # Part 2 - The Box class
    book = Present("ABC Book", 2)

    box = Box()
    box.add_present(book)
    print(box.total_weight())

    cd = Present("Pink Floyd: Dark Side of the Moon", 1)
    box.add_present(cd)
    print(box.total_weight())
