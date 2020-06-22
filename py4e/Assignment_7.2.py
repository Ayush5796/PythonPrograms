'''
7.2 Write a program that prompts for a file name, then opens that file and
reads through the file, looking for lines of the form:

X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values from each of the lines
and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
when you are testing below enter mbox-short.txt as the file name.
'''
fname = input("Enter the file name : ")
try :
    file = open(fname , 'r')
except :
    print("File can not be found :" , fname)
    quit()
count = 0
add = 0
for line in file :

    if not line.startswith('X-DSPAM-Confidence:') :
        continue

    count = count+1
    pos = line.find(':')
    getline = line[pos+1 : ]
    number = getline.lstrip()
    num = float(number)
    add += num

print('Average spam confidence:', add/count)
