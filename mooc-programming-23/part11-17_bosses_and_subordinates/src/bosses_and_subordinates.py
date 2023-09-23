# WRITE YOUR SOLUTION HERE:
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)
def find_node(find: Employee, value):
    # if we reach the end of a  node we return False because we couldn't find what we looking for on our way
    if find is None:
        return False

    # if we found the value we looking for we return it 
    if value == find.value: 
        return True 
    
    # if none of the above conditions are true then we keep on searching by calling right branch
    if value > find.value:
        return find_node(find.right_child, value)

    # if we couldn't find value on the right branch we keep on searching by calling left branch
    # we preserve the value we search by passing it as agument for a funtion
    return find_node(find.left_child, value)

    

def count_subordinates(employee: Employee):
    total_subordinates = len(employee.subordinates)
 
    for subordinate in employee.subordinates:
        total_subordinates += count_subordinates(subordinate)
 
    return total_subordinates
    

"""
def count_subordinates(employee: Employee):
    if employee is None:
        return 0
    no_of_subordinates = 0
    for subordinate in employee.subordinates:
        no_of_subordinates += count_subordinates(subordinate)+1
    return no_of_subordinates
"""
if __name__ == "__main__":
    t1 = Employee("Sally")
    t2 = Employee("Eric")
    t3 = Employee("Matthew")
    t4 = Employee("Emily")
    t5 = Employee("Adele")
    t6 = Employee("Claire")
    t1.add_subordinate(t4)
    t1.add_subordinate(t6)
    t4.add_subordinate(t2)
    t4.add_subordinate(t3)
    t4.add_subordinate(t5)
    print(count_subordinates(t1))
    # print(count_subordinates(t4))
    # print(count_subordinates(t5))