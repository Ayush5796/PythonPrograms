from collections import defaultdict

marks = [
    ('Shubham', 89),
    ('Rohit', 78),
    ('JournalDev', 99),
    ('JournalDev', 98)
]

dict_marks = defaultdict(list)

for key, value in marks:
    dict_marks[key].append(value)


print(list(dict_marks.items()))
print(dict_marks['JournalDev'])
print(dict_marks['abc'])
print(list(dict_marks.items()))