
tasks = []
taskId = 0

class Todo(object):
    def __init__(self,title,priority):
        self.title = title
        self.priority = priority
        self.id = 0


##Add new task function
def display():
    for task in tasks:
        print(str(task.id) + " " task.title + " " + task.priority)


def add_task(title, priority):
    task = Task(title,priority)
    # add task to the list
    task.id = taskId
    tasks.append(task)
    display()

def removeTaskById(taskIdToRemove):
    for index in range(0, len(tasks)):
        ##get the task at particular index
        ## task = tasks[index]
        ##if task.id == taskIdToRemove
        ##del tasks[index]
        if tasks[index].id == taskIdToRemove:
            del tasks[index]
            break

def prompt_for_input:
    title = raw_input("Enter title of the task")
    priority = raw_input("Enter priority: ")
    #Returning Tupule
    return title,priority





while True:
    choice = raw_input("Enter 1 to add new task, 2 to delete new Task, q to quit")

    if choice = "1":
        taskId += 1
        (title,priority) = prompt_for_input()
        add_task(title,priority)

    elif choice == "2":
        taskIdToRemove = int(raw_input("Enter Task ID to remove"))
        removeTaskById(taskIdToRemove)







    elif choice = "q"
        break
