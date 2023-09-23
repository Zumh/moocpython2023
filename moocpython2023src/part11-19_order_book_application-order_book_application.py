# Write your solution here
# If you use the classes made in the previous exercise, copy them here

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
 
    def mark_finished(self, id: int)->bool:
        for task in self.__tasks:
            if task.id == id:
                task.mark_finished()
                return True
        return False 
        # not incorrect
        #raise ValueError("wrong id")
    
    def unfinished_orders(self):
        return [t for t in self.__tasks if not t.is_finished()]
 
    def finished_orders(self):
        return [t for t in self.__tasks if t.is_finished()]
 
    def status_of_programmer(self, programmer: str)->tuple:
        is_exist = True
        if programmer not in self.programmers():
            #raise ValueError("Programmer does not exists")
            is_exist = False
        else:
            finished_tasks = [t for t in self.__tasks if t.programmer == programmer and t.is_finished() ]
            not_finished_tasks = [t for t in self.__tasks if t.programmer == programmer and not t.is_finished() ]
    
            finished_hours = sum(t.workload for t in finished_tasks)
            not_finished_hours = sum(t.workload for t in not_finished_tasks)
    
            return (len(finished_tasks), len(not_finished_tasks), finished_hours, not_finished_hours, is_exist)
        return (0,0,0,0,is_exist)

class OrderApplication:

    def __init__(self) -> None:

        self.order = OrderBook()

    def help(self):
        print(f"commands: \n\
        0 exit\n\
        1 add order\n\
        2 list finished tasks\n\
        3 list unfinished tasks\n\
        4 mark task as finished\n\
        5 programmers\n\
        6 status of programmer")
    def add_order(self):
        description = input("description: ")
        try:
            programmer, workload = input("programer and workload estimate: ").split(' ')
            # parse programmer and workload 
            self.order.add_order(description, programmer, int(workload))
            print("added!")
        except:
            self.__error()

          
    
    def finished_orders(self):
        orders = self.order.finished_orders()
        if orders == []:
            print("no finished tasks")
        else:
            for order in orders:
                print(order)
    
    def unfinished_orders(self):
        orders = self.order.unfinished_orders()
        if orders != []:
            for order in orders:
                print(order)

    def mark_finished(self):
        # ask user for id number 
        input_id = input("id: ")
        try:
            if self.order.mark_finished(int(input_id)):
                print("marked as finished")
            else:
                self.__error()
        except:
            self.__error()

    def programmers(self):
        for programmer in self.order.programmers():
            print(programmer)

    def __error(self):
        print("erroneous input")

    def status_of_programmer(self):
        programmer = input("programmer: ")
        finished_tasks_len, not_finished_tasks_len, finished_hours, not_finished_hours, is_exist = self.order.status_of_programmer(programmer)
        if is_exist:
            print(f"tasks: finished {finished_tasks_len} not finished {not_finished_tasks_len}, hours: done {finished_hours} scheduled {not_finished_hours}")
        else:
            self.__error()
    def execute(self):
        
        self.help()
        while True:
            user_input = input("command: ")
            if user_input == '0':
                break 
            elif user_input == '1':
                self.add_order()
            elif user_input =='2':
                self.finished_orders()
            elif user_input == '3':
                self.unfinished_orders()
            elif user_input == '4':
                self.mark_finished()
            elif user_input == '5':
                self.programmers()
            elif user_input == '6':
                self.status_of_programmer()
            else:
                self.help()

order = OrderApplication()
order.execute()


'''
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
 
class Application:
    def __init__(self):
        self.orders = OrderBook()
 
    def instructions(self):
        # Defining multiline string is possible with triple apostrophes
        instructions_str = """
commands:
0 exit
1 add order
2 list finished tasks
3 list unfinished tasks
4 mark task as finished
5 programmers
6 status of programmer"""
        print(instructions_str)
 
    def add(self):
        description = input("description: ")
        programmer_and_estimate = input("programmer and workload estimate: ")
        try:
            programmer = programmer_and_estimate.split(' ')[0]
            workload = int(programmer_and_estimate.split(' ')[1])
            self.orders.add_order(description, programmer, workload)
            print("added!")
        except:
            print("erroneous input")
 
    def unfinished(self):
        for task in self.orders.unfinished_orders():
            print(task)
 
    def finished(self):
        finished_orders = self.orders.finished_orders()
        if len(finished_orders)==0:
            print("no finished tasks")
            return
 
        for task in finished_orders:
            print(task)
 
    def programmers(self):
        for programmer in self.orders.programmers():
            print(programmer)
 
    def mark_finished(self):
        try:
            order_id = int(input("id: "))
            self.orders.mark_finished(order_id)
            print("marked as finished")
        except:
            print("erroneous input")
 
    def programmers_status(self):
        programmer = input("programmer: ")
        if not programmer in self.orders.programmers():
            print("erroneous input")
            return
 
        status = self.orders.status_of_programmer(programmer)
        print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}")
 
    def run(self):
        self.instructions()
        while True:
            command = input("command: ")
            if command == "0":
                return
            elif command == "1":
                self.add()
            elif command == "2":
                self.finished()
            elif command == "3":
                self.unfinished()
            elif command == "4":
                self.mark_finished()
            elif command == "5":
                self.programmers()
            elif command == "6":
                self.programmers_status()
 
Application().run()
'''