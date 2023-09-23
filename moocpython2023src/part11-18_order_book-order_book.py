# Write your solution here:

class Task:
    """
    a description
    an estimate of the hours required for completing the task
    the name of the programmer assigned to the task
    a field for keeping track of whether the task is finished
    a unique identifier

    Some clarifications:

    the state of the task (finished or not yet finished) can be checked 
    with the function is_finished(self) which returns a Boolean value
    a task is not finished when it is created
    a task is marked as finished by calling the method mark_finished(self)
    the id of a task is a running number which starts with 1. The id of the first task is 1, the id of the second is 2, and so forth.
    """
    code = 0

    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        # code number increase as object instances created
        # we only initialize id for each object.
        # which make each object id unique
        Task.code += 1
        self.id = Task.code 
        
        self.__finished = False
    
    def __str__(self)->str:
        if self.__finished:
            return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} NOT FINISHED"

    def is_finished(self)->bool:
        return self.__finished
    def mark_finished(self)->bool:
        self.__finished = True 

class OrderBook:
    """
    At this stage your OrderBook should provide three methods:

    add_order(self, description, programmer, workload) which adds a new order to the OrderBook. An OrderBook stores the orders internally as Task objects. NB: the method should take exactly the arguments mentioned, or else the automated tests will not work correctly.
    all_orders(self) returns a list of all the tasks stored in the OrderBook
    programmers(self) returns a list of the names of all the programmers with tasks stored in the OrderBook. The list should contain each programmer only once
    Hint: an easy method for removing duplicates is handling the list initially as a set. A set is a collection of items where each unique item appears only once. A set can be then converted back into a list, and we can then be sure each item is now unique:
    """
    def __init__(self):
        self.tasks = []
    
    def add_order(self, description: str, programmer: str, workload: int):
        self.tasks.append(Task(description, programmer, workload))
    def all_orders(self)->list[Task]:
        return self.tasks
    def programmers(self)->list[str]:
        coders = []
        for task in self.tasks:
            if task.programmer not in coders:
                coders.append(task.programmer)
        return coders
    def mark_finished(self, id: int):
        for task in self.tasks:
            if task.id == id:
                task.mark_finished()
                break

        else:
            raise ValueError("No task id found")
    def unfinished_orders(self)->list[Task]:
        return [task for task in self.tasks if not task.is_finished()]
    
    def finished_orders(self)->list[Task]:
        return [task for task in self.tasks if task.is_finished()]

    def status_of_programmer(self, programmer: str)->tuple:
        finished_tasks = 0
        unfinished_tasks = 0
        work_load_unfinished =0
        work_load_finished = 0
        if programmer not in self.programmers():
            raise ValueError("Programmer not found")
        else:
            for task in self.tasks:
                if programmer == task.programmer:
                    if task.is_finished():
                        finished_tasks += 1
                        work_load_finished += task.workload
                    else:
                        unfinished_tasks += 1
                    
                        work_load_unfinished += task.workload
        return(finished_tasks, unfinished_tasks, work_load_finished, work_load_unfinished)




if __name__ == "__main__":
    # Part 1 - Task
    # t1 = Task("program hello world", "Eric", 3)
    # print(t1.id, t1.description, t1.programmer, t1.workload)
    # print(t1)
    # print(t1.is_finished())
    # t1.mark_finished()
    # print(t1)
    # print(t1.is_finished())
    # t2 = Task("program webstore", "Adele", 10)
    # t3 = Task("program mobile app for workload accounting", "Eric", 25)
    # print(t2)
    # print(t3)

    # Part 2 - order book 
    # orders = OrderBook()
    # orders.add_order("program webstore", "Adele", 10)
    # orders.add_order("program mobile app for workload accounting", "Eric", 25)
    # orders.add_order("program app for practising mathematics", "Adele", 100)

    # for order in orders.all_orders():
    #     print(order)

    # print()

    # for programmer in orders.programmers():
    #     print(programmer)

    # Part 3 - mark_finished(id)
    # orders = OrderBook()
    # orders.add_order("program webstore", "Adele", 10)
    # orders.add_order("program mobile app for workload accounting", "Eric", 25)
    # orders.add_order("program app for practising mathematics", "Adele", 100)

    # orders.mark_finished(1)
    # orders.mark_finished(2)

    # for order in orders.all_orders():
    #     print(order)

    # Part 4 - status of a programmers
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)

    """
    1: program webstore (10 hours), programmer Adele FINISHED
    2: program mobile app for workload accounting (25 hours), programmer Eric FINISHED
    3: program app for practising mathematics (100 hours), programmer Adele NOT FINISHED
    """

    """
    class Task:
    id = 0
    @classmethod 
    def new_id(cls):
        Task.id += 1
        return Task.id
 
    def __init__(self, description, programmer, workload):
        self.programmer = programmer
        self.description = description
        self.workload = workload
        self.id = Task.new_id()
        self.finished = False
    
    def is_finished(self):
        return self.finished 
 
    def mark_finished(self):
        self.finished = True
 
    def __str__(self):
        status = "NOT FINISHED" if not self.finished else "FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"
 
class OrderBook:
    def __init__(self):
        self.__tasks = []
 
    def add_order(self, description, programmer, workload):
        self.__tasks.append(Task(description, programmer, workload))
 
    def all_orders(self):
        return self.__tasks
 
    def programmers(self):
        return list(set([t.programmer for t in self.__tasks]))
 
    def mark_finished(self, id: int):
        for task in self.__tasks:
            if task.id == id:
                task.mark_finished()
                return
        
        # not incorrect
        raise ValueError("wrong id")
    
    def unfinished_orders(self):
        return [t for t in self.__tasks if not t.is_finished()]
 
    def finished_orders(self):
        return [t for t in self.__tasks if t.is_finished()]
 
    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError("Programmer does not exists")
        
        finished_tasks = [t for t in self.__tasks if t.programmer == programmer and t.is_finished() ]
        not_finished_tasks = [t for t in self.__tasks if t.programmer == programmer and not t.is_finished() ]
 
        finished_hours = sum(t.workload for t in finished_tasks)
        not_finished_hours = sum(t.workload for t in not_finished_tasks)
 
        return (len(finished_tasks), len(not_finished_tasks), finished_hours, not_finished_hours)
# Write your solution here:

    """