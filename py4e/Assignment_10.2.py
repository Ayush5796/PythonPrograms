'''10.2 Write a program to read through the mbox-short.txt and figure out the
distribution by hour of the day for each of the messages. You can pull the hour
out from the 'From ' line by finding the time and then splitting the string a
second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts,
sorted by hour as shown below.'''

fname = 'mbox-short.txt'
try :
    file = open(fname , 'r')
except :
    print("File cannot be found!! :", fname)
    quit()

words = list()
all_hrs = dict()
for line in file :
    new_line = line.rstrip()

    if not new_line.startswith('From ') :
        continue

    words = new_line.split()

    hours = words[5]
    hrs = hours.split(':')
    hh = hrs[0]

    #Creating the dictionary to get all hours and their count
    all_hrs[hh] = all_hrs.get(hh , 0) + 1

get_hours = list()
for (h,c) in all_hrs.items() :
    newtup = (h,c)
    get_hours.append(newtup)

get_hours = sorted(get_hours)

for h,c in get_hours :
    print(h,c)
print('********************************************************************')
print(sorted([(h,c) for (h,c) in all_hrs.items()]))
