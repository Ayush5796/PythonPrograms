from collections import OrderedDict, Counter

roll_no = OrderedDict([
    (1, 'William'),
    (2, 'John'),
    (3, 'Andrew')
])


for key, value in roll_no.items():
    print(key, value)

roll_no[1] = 'Alexander'

for key, value in roll_no.items():
    print(key, value)

my_dict = {}
my_dict['a'] = 'andreas'
my_dict['b'] = 'johann'
my_dict['c'] = 'peter'
my_dict['d'] = 'richard'

for key, value in my_dict.items():
    print(key, value)


my_dict['a'] = 'robert'

for key, value in my_dict.items():
    print(key, value)

print("---------------------------------------------------------")
mylist = ["a","d","c","c","a","b","a","a","b","c"]
count = Counter(mylist)
print(count.most_common())
my_dict2 = OrderedDict(count.most_common())

for key, value in my_dict2.items():
    print(key, value)





