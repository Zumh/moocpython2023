# Write your solution here:
class Computer:
    def __init__(self, model: str, speed: int):
        self.__model = model
        self.__speed = speed

    @property
    def model(self):
        return self.__model

    @property
    def speed(self):
        return self.__speed
class LaptopComputer(Computer):
    def __init__(self, model: str, speed: int, weight: int):
        super().__init__(model, speed)
        self.weight = weight 
    def __str__(self)->str:
        return f"{self.model}, {self.speed} MHz, {self.weight} kg"

if __name__ == "__main__":
    "NoteBook Pro15, 1500 MHz, 2 kg"
    laptop = LaptopComputer("NoteBook Pro15", 1500, 2)
    print(laptop)