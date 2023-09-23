# Write your solution here:

# Write your solution here:
class Clock:
    def __init__(self, hours:int, minutes:int, seconds:int):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
    def __str__(self) -> str:
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
    def tick(self):
        self.seconds += 1
        if self.seconds > 59:
            self.minutes += 1
            self.seconds = 0
            if self.minutes > 59:
                self.minutes = 0
                self.hours += 1
                if self.hours > 23:
                    self.hours = 0
            
    def set(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0

if __name__=="__main__":      
    # clock = Clock(23, 59, 55)
    # print(clock)
    # clock.tick()
    # print(clock)
    # clock.tick()
    # print(clock)
    # clock.tick()
    # print(clock)
    # clock.tick()
    # print(clock)
    # clock.tick()
    # print(clock)
    # clock.tick()
    # print(clock)

    # clock.set(12, 5)
    # print(clock)

    clock = Clock(10,10,58)
    clock.tick()
    clock.tick()
    clock.tick()
    print(clock)