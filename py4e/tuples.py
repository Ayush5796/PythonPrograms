fname = 'romeo.txt'
try :
    file = open(fname ,'r')
except :
    print("File can not be found!! :", fname)
    quit()

word = list()
all_words = dict()
for line in file :
    new_line = line.rstrip()
    words = new_line.split()

    for word in words:
        if word not in all_words :
            all_words[word] = all_words.get(word , 0) + 1

# lst = list()
#
# for (k,v) in all_words.items() :
#     newtup = (v,k)
#     lst.append(newtup)
#
# lst = sorted(lst, reverse=True)
#
# for (v,k) in lst[:10] :
#     print(k,v)

print(sorted([(v,k) for (k,v) in all_words.items()], reverse=True))
