import json

tasks =[]  ###This is the empty array that the user input tasks will be added to
taskId = 0  ###Still not 100% sure what this does ?????????????

class Task(object):
    def __init__(self,title,priority):
        self.title = title
        self.priority = priority
        self.id = 0

##This method is going to display all the tasks the user has input
def display_all_tasks():
    for task in tasks:
        print("{0} - {1} - {2}".format(task.id,task.title,task.priority))

##This function is is adding a task to the "tasks array" and assigning the self.id number
def add_task(title,priority):
    task = Task(title,priority)
    task.id = taskId     ###Dont understand how/or what this does#########?????????
    tasks.append(task) ##This adds the user input title and priority to the "tasks array"
    display_all_tasks() ##This calls the above method, which prints the "tasks array"

##This method will identify the index using a loop and then match the userinput to the index and delete that item from the array
def removeTaskById(taskIdToRemove):
    for index in range(0, len(tasks)):  ###Taking the index from 0-end of the tasks array
        if tasks[index].id == taskIdToRemove: ###if the array index is equal to the
        ## userinput (taskIdToRemove) then move to the next step.
            del tasks[index] ##This deletes the index/item from the array
            display_all_tasks()
            break ### Not sure why this is needed. ???????????

##This method/function will be called when userinput needs to be gathered, and then return that collected input.
def prompt_for_input():
    ###
    title = raw_input("Please enter the task you would like to add.")#userinput = title
    priority = raw_input("Please enter Prioirty level:   Low, Medium, High   .") #userinput = priority
    return title,priority  ##this is returned as a tupule. title = user input and priority = userinput



##This section below begins the User interation.

while True:         ##This begins a while loop.???Still dont understant while what is true????? is it, while the input entered by user is true continue running the loop?

    choice = raw_input("Please select 1 to add a new task, 2 to delete a task, or press q to quit.") ###This line is asking the user for the first time to input a command that will correlate with what they want to do.

##This is the first part of the loop to check the userinput. If what the user input matches "1" then the remaining code will execute, otherwise it continues to the next section.
    if choice == "1":
        taskId += 1 ##Takes the global taskId var and increases it by 1.
        (title, priority) = prompt_for_input() #this assigns the var title,priority. It runs the prompt_for_input method and assigns the var what it returns.
        add_task(title,priority) #this runs the add_task function

##This is the second part of the loop to check userinput. It is only run, if userinput does not match the first choice above.
    elif choice == "2":
        taskIdToRemove = int(raw_input("Enter Task Id to remove."))##this assigns the var to the userinput data, and does so as a string.
        removeTaskById(taskIdToRemove)##This is calling the removeTaskById method and using the collected user input (taskIdToRemove) to run that method.

##This is the final part of the loop that is run. If the userinput does not match either above choice, but does equal "q" it stop the loop completly.
    elif choice == "q":
        break
