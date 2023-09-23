# WRITE YOUR SOLUTION HERE:
class Car:

    def __init__(self) -> None:
        self.__petrol = 0
        self.__odometer = 0
    
    def fill_up(self):
        # fill up the tank 0 - 60 litres
        if  0<=self.__petrol < 60:
            self.__petrol = 60


    def drive(self, km:int):
        # which drives the car for the distance indicated, or for however long the petrol in the tank allows
        # The car consumes one litre of petrol per kilometre.
        # 1litre/1km
        # calculate how much gas we have left if we drive after a given distance
        gas_left = self.__petrol - (km * 1)
        
        if gas_left <= 0 :
            # left over distance we can drive using left over gas
            km = self.__petrol * 1
            # given distance "km" is too far and gas must be reassigned to 0
            gas_left = 0
        # update gas that left and increase distance we just drove
        self.__petrol = gas_left
        self.__odometer += km
        
            

    def __str__(self)->str: 

        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__petrol} litres"

if __name__ == "__main__":
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)