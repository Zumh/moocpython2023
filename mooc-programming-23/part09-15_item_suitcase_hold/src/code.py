# Write your solution here:


class Item:
    def __init__(self,input_name: str, input_weight: int)->None:
        self.__name = input_name 
        self.__weight = input_weight
    

    def name(self)->str:
        return self.__name
    
    def weight(self)->int:
        return self.__weight

    def __str__(self)->str:
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:
    """
    a constructor which takes the maximum weight as an argument
    a method named add_item which adds the item given as an argument to the suitcase. The method has no return value.
    a __str__ method which returns a string in the format "x items (y kg)"
    """
    def __init__(self,maximum_weight: int)->None: 
        self.__items = []
        self.__max_weight = maximum_weight

    def weight(self)->int:
        total_weight = 0

        for item in self.__items:
            total_weight += item.weight()

        return total_weight

    def add_item(self, given_item: Item)->None: 
        
        total_weight = self.weight() + given_item.weight()

        if total_weight <= self.__max_weight: 
            self.__items.append(given_item)

    def __str__(self)->str:
        # calculate total weight 
        item_amount = len(self.__items)
        if item_amount == 1:
            return f"{len(self.__items)} item ({self.weight()} kg)"
        else: 
            return f"{len(self.__items)} items ({self.weight()} kg)" 
    
    def print_items(self):
        
        for item in self.__items:
            print(item)
    
    def is_empty(self)->bool:
        return self.__items == []

    def heaviest_item(self)->int:
        if self.is_empty():
            return None 
        heaviest = self.__items[0]
        heaviest_weight = heaviest.weight()
        for item in self.__items:
            if heaviest_weight < item.weight():
                heaviest_weight = item.weight()
                heaviest = item 
        return heaviest


class CargoHold:    
    def __init__(self, given_max_weight: int)->None:
        self.__max_weight = given_max_weight
        self.__suitcases = []

    def add_suitcase(self, given_suitcase: Suitcase):
        total_weight = given_suitcase.weight()

        # get total suit case weight for first time adding given suitcase
        # we subtract weight from limited max_weight
        if len(self.__suitcases) == 0:
            for suitcase in self.__suitcases:
                total_weight += suitcase.weight()

        if total_weight <= self.__max_weight:
            self.__suitcases.append(given_suitcase)
            self.__max_weight -= total_weight

    def __str__(self)->str:
        suitcase_amount = len(self.__suitcases)
        if suitcase_amount == 1:
            return f"{len(self.__suitcases)} suitcase, space for {self.__max_weight} kg"
        else:
            return f"{len(self.__suitcases)} suitcases, space for {self.__max_weight} kg"

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()
if __name__ == "__main__":

    # # Part 1 - Item class
    # book = Item("ABC Book", 2)
    # phone = Item("Nokia 3210", 1)

    # print("Name of the book:", book.name())
    # print("Weight of the book:", book.weight())

    # print("Book:", book)
    # print("Phone:", phone)

    # Part 2 - Suitcase 
    # book = Item("ABC Book", 2)
    # phone = Item("Nokia 3210", 1)
    # brick = Item("Brick", 4)

    # suitcase = Suitcase(5)
    # print(suitcase)

    # suitcase.add_item(book)
    # print(suitcase)

    # suitcase.add_item(phone)
    # print(suitcase)

    # suitcase.add_item(brick)
    # print(suitcase)

    # Part - 4 All the items 
    # book = Item("ABC Book", 2)
    # phone = Item("Nokia 3210", 1)
    # brick = Item("Brick", 4)

    # suitcase = Suitcase(10)
    # suitcase.add_item(book)
    # suitcase.add_item(phone)
    # suitcase.add_item(brick)

    # print("The suitcase contains the following items:")
    # suitcase.print_items()
    # combined_weight = suitcase.weight()
    # print(f"Combined weight: {combined_weight} kg")

    # Part - 5 Heaviet Object
    # book = Item("ABC Book", 2)
    # phone = Item("Nokia 3210", 1)
    # brick = Item("Brick", 4)

    # suitcase = Suitcase(10)
    # suitcase.add_item(book)
    # suitcase.add_item(phone)
    # suitcase.add_item(brick)

    # heaviest = suitcase.heaviest_item()
    # print(f"The heaviest item: {heaviest}")

    # Part - 6 Cargo Hold 
    # cargo_hold = CargoHold(1000)
    # print(cargo_hold)

    # book = Item("ABC Book", 2)
    # phone = Item("Nokia 3210", 1)
    # brick = Item("Brick", 4)

    # adas_suitcase = Suitcase(10)
    # adas_suitcase.add_item(book)
    # adas_suitcase.add_item(phone)

    # peters_suitcase = Suitcase(10)
    # peters_suitcase.add_item(brick)

    # cargo_hold.add_suitcase(adas_suitcase)
    # print(cargo_hold)

    # cargo_hold.add_suitcase(peters_suitcase)
    # print(cargo_hold)

    # Part - 7 print item 
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()