import json

filename = "D:\\PythonPrograms\\JSON_File\\username.json"

with open(filename,'r') as file_object:
    username = json.load(file_object)

print("Welcome back!! " + username)