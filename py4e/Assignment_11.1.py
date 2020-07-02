import re

fname = 'regex_sum_702244.txt'

file = open(fname , 'r')

print('Sum :', sum([int(number for number in re.findall('[0-9]+' , file.read()))]))

numbers = list()
total_num = list()

for line in file :
    line = line.rstrip()
    numbers = re.findall('[0-9]+' , line)

    for num in numbers :
        try :
            x = int(num)
        except :
            print('Not a number')

        total_num.append(x)

#print(total_num)
print('Sum :' , sum(total_num))
