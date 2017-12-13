import json

tasklist = []
taskId = 0
filename = "TaskList.json"


class ToDoList(object):
    def __init__ (self,task_title,priority_value):
        self.task_title = task_title
        self.priority_value = priority_value
        self.id = 0

    def toDictionary(self):
        return {"task_title": self.task_title, "priority_value": self.priority_value}



def user_input():
    task_title = raw_input("Please enter the task you would like to add.    ")
    priority_value = raw_input("Please assign priority value to the task...Low, Medium, High   ")
    user_task = ToDoList(task_title,priority_value)
    return user_task

def load_previous_tasks():
    with open(filename) as file_object:
        tasklist = json.load(file_object)
    return tasklist

tasklist = load_previous_tasks()
#print(tasklist)


while True:
    userChoice = raw_input("Please choose 1. To add task, 2. To remove task, and 'q' to Quit. ")

    if userChoice == "1":

        user_task = user_input()
        task_dict = user_task.toDictionary()
        tasklist.append(task_dict)

        with open(filename, 'w') as file_object:
            json.dump(tasklist,file_object)



    elif userChoice == "q":
        break




tasklist = load_previous_tasks()

firsttask = tasklist["task_title"]
priority = tasklist["priority_value"]

    #combined = ToDoList(task_title,priority_value)
    #print(combined)

#sprint("Your current task list is {0}".format(tasklist[1]))
#print(tasklist)

#print(tasklistdef)
