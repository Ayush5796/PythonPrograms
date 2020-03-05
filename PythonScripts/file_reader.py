"""with open('D:\PythonScripts\pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.lstrip())

file_location = 'D:\PythonScripts\pi_digits.txt'
with open(file_location) as file_object_1:
    for line in file_object_1:
        print(line.rstrip())

"""
file_location = 'D:\PythonScripts\pi_digits.txt'
with open(file_location) as file_object_2:
    lines = file_object_2.readlines()

print(lines)
for new_line in lines:
    print(new_line.rstrip())