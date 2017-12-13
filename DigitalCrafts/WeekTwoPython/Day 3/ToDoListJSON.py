import json

# list of tasks
tasks = []
taskId = 0

class Task(object):

    def __init__(self,title,priority):

        self.title = title
        self.priority = priority
        self.id = 0


# displaying all the tasks
def display_all_tasks():
    for task in tasks:
        print("{0} - {1} - {2}".format(task.id,task.title,task.priority))

# add new task function
def add_task(title,priority):
    # create new task
    task = Task(title,priority)
    # add the task to the list
    task.id = taskId
    tasks.append(task)
    display_all_tasks()

def removeTaskById(taskIdToRemove):
    for index in range(0,len(tasks)):

        # get the task at particular index
        #task = tasks[index]
        #if task.id == taskIdToRemove:
        #    del tasks[index]

        if tasks[index].id == taskIdToRemove:
            del tasks[index]
            break

def prompt_for_input():
    title = raw_input("Enter title of the task ")
    priority = raw_input("Enter priority: ")
    #returning tuples
    return title,priority

def toDictionary(self):
    return{"title":self.title, "priority":self.priority}

while True:

    choice = raw_input('Enter 1 to add new task, 2 to delete the task, q to quit the app')

    if choice == "1":
        taskId += 1
        (title,priority) = prompt_for_input()
        toDictionary(title, priority)
        # adding new task
        add_task(title,priority)

    elif choice == "2":
        taskIdToRemove = int(raw_input("Enter Task Id to remove"))
        removeTaskById(taskIdToRemove)

    elif choice == "q":
        break

filename = "TaskList.json"


#with open(filename, 'w') as file_object:
#    json.dump(tasks,file_object)
