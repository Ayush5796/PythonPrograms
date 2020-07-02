''' 7.1 Write a program that prompts for a file name, then opens that file and
reads through the file, and print the contents of the file in upper case. Use
the file words.txt to produce the output below.

You can download the sample data at http://www.py4e.com/code3/words.txt'''

# Use words.txt as the file name
fname = input("Enter file name: ")
try :
    file = open(fname , 'r')
except :
    print("File can not be found :",fname)

for line in file :
    newline = line.rstrip()
    print(newline.upper())