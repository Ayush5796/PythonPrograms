import json

filename = "D:\\PythonPrograms\\JSON_File\\numbers.json"

with open(filename, 'r') as file_object:
    numbers = json.load(file_object)

print(numbers)