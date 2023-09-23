class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

# Write your solution herer:
def sort_by_length(routes: list)->list:
    def order_by_length(route: ClimbingRoute)->int:
        return route.length
    # longest to shortest length
    return sorted(routes, key= order_by_length, reverse=True)

def sort_by_difficulty(routes: list)->list:
    def order_by_difficulty(route: ClimbingRoute):
        
        key_grade = tuple(route.grade)
        key = (key_grade, '+' in key_grade, route.length)
        # (route.grade, route.length) -> automatically follow the order 
        return key
    return sorted(routes, key=order_by_difficulty, reverse=True)
if __name__ == "__main__":
    # # Class intro
    # route1 = ClimbingRoute("Edge", 38, "6A+")
    # route2 = ClimbingRoute("Smooth operator", 9, "7A")
    # route3 = ClimbingRoute("Synchro", 14, "8C+")


    # print(route1)
    # print(route2)
    # print(route3.name, route3.length, route3.grade)

    # Part 1 sort by length 

    # r1 = ClimbingRoute("Edge", 38, "6A+")
    # r2 = ClimbingRoute("Smooth operator", 11, "7A")
    # r3 = ClimbingRoute("Synchro", 14, "8C+")
    # r4 = ClimbingRoute("Small steps", 12, "6A+")

    # routes = [r1, r2, r3, r4]   

    # for route in sort_by_length(routes):
    #     print(route.length)
    #     print(route)

    # Part 2 sort by difficulty
    r1 = ClimbingRoute("Edge", 38, "6A+")
    r2 = ClimbingRoute("Smooth operator", 11, "7A")
    r3 = ClimbingRoute("Synchro", 14, "8C+")
    r4 = ClimbingRoute("Small steps", 12, "6A+")

    routes = [r1, r2, r3, r4]
    for route in sort_by_difficulty(routes):
        print(route)