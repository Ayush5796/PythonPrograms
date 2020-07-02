'''9.4 Write a program to read through the mbox-short.txt and figure out who
has sent the greatest number of mail messages. The program looks for 'From '
lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to
a count of the number of times they appear in the file. After the dictionary is
produced, the program reads through the dictionary using a maximum loop to find
the most prolific committer.'''

fname = 'mbox-short.txt'
try :
    file = open(fname,'r')
except :
    print("File can not be found!!", fname)

mail_address = dict()

for line in file :

    if not line.startswith('From '):
        continue

    found_line = line.split()
    sender = found_line[1]

    mail_address[sender] = mail_address.get(sender , 0) + 1

bigcount = None
bigword = None

for word , count in mail_address.items() :

    if bigword is None or count > bigcount :
        bigword = word
        bigcount = count

print(bigword,bigcount)
