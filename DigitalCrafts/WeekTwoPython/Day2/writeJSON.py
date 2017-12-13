##This is a built in part of python that you can use when you import it
import json

filename = 'task.json'

task1 = {"title":"Wash the car"}
task2 = {"title":"Feed the Cat"}

tasks = [task1, task2]

#storing contents in json file
#with open(filename,'w') as file_object:
#    json.dump(tasks, file_object)

#reading contents from json.file
with open(filename) as file_object:
    contents = json.load(file_object)
    print(contents[0])
    print(contents)
