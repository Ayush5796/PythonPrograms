import re

fname = 'mbox-short.txt'
file = open(fname , 'r')

result = list()
for line in file :
    new_line = line.rstrip()
    if not new_line.startswith('From ') : continue
    result.append((re.findall('\S+?@\S+' , new_line)))

print(result)
