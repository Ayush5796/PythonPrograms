import json

filename = "D:\\PythonPrograms\\JSON_File\\username.json"

try:
    with open(filename,'r') as file_object:
        username = json.load(file_object)
except FileNotFoundError:
    username = input("Enter your Name: ")
    print("We will remember when you are back!!!")

    with open(filename, 'x') as file_object:
        json.dump(username, file_object)
else:
    print("Welcome back!!!" + username)