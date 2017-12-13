import json

tasks = []

class Task(object):
    def __init__(self,title,priority):
        self.title = title
        self.priority = priority

    def toDictionary(self):
        return {"title":self.title,"priority":self.priority}

def load_all_tasks():
    # load the contents of json file into an array
    with open('tasks.json') as file_object:
        tasks = json.load(file_object)

# populate tasks
load_all_tasks()

while True:

    choice = raw_input("Enter 1 to add task, 2 to delete task, q to quit")

    if choice == "1":
        title = raw_input("Enter title: ")
        priority = int(raw_input("Enter priority "))
        task = Task(title,priority)
        tasks.append(task.toDictionary())

        with open('tasks.json','w') as file_object:
            json.dump(tasks,file_object)

    elif choice == "2":
        idToDelete = int(raw_input("Enter id to delete "))

        for task in tasks:
            if task["id"] == idToDelete:
                tasks.remove(task)
                break

        # save to the file again
        with open('tasks.json','w') as file_object:
            json.dump(tasks,file_object)


    elif choice == "q":
        break
