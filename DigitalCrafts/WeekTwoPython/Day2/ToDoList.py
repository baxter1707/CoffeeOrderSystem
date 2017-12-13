

class Todo(object):
    def __init__(self,title,description):
        self.title = title
        self.description = description
        self.ToDoList = []

    def view_tasks(self):
        print("{0} = {1}.".format(self.title,self.description))

    def add_list(self):
        self.ToDoList.append(self.title)

    def view_list(self):
        print("You added {0} to the To Do List.".format(self.ToDoList))



item1 = Todo("EAT","Eat dinner")
item2 = Todo("HOMEWORK","Study and finish homework")
item3 = Todo("SLEEP","Go to sleep")

item1.view_tasks()
item2.view_tasks()
item3.view_tasks()


while True:
    choice = raw_input("Please choose the item you would like to add...EAT, HOMEWORK, SLEEP .")
    quit = raw_input("Press q to quit")


    if choice == "EAT":
        item1.add_list()
        print(item1.view_list())

    elif choice == "HOMEWORK":
        item2.add_list()
        print(item2.view_list())

    elif choice == "SLEEP":
        item3.add_list()
        print(item3.view_list())

    elif quit == "q":
        break
