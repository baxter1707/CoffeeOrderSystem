import json

class Task(object):
    def __init__(self,title):
        self.title = title

    def toDictionary(self):
        return {"title":self.title}

# create task object
newTask = Task('Mail the stuff')

filename = 'tasks.json'

# creating dictionaries
task1 = {"title":"Wash the car","priority":"high"}
task2 = {"title":"Feed the cat","priority":"low"}

tasks = [task1,task2]

# storing contents in json file
with open(filename,'w') as file_object:
    #json.dump(tasks, file_object)
    json.dump(newTask.toDictionary(),file_object)

# reading contents from json file
with open(filename) as file_object:
     #arrayOfDictionaries = json.load(file_object)
     dictionary = json.load(file_object)
     t = Task(dictionary["title"])
     print(t.title)
     # add to the tasks array
     # tasks.append(t)

    #print(contents)
