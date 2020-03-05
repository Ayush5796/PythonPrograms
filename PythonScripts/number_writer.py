import json

filename = "D:\\PythonPrograms\\JSON_File\\numbers.json"

numbers = ['1','2','3','4','5']
#help(open)
with open (filename, 'x') as file_object:
    json.dump(numbers, file_object)    



