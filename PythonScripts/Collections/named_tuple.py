from collections import namedtuple

Student = namedtuple('Student', 'fname, lname, age')
s1 = Student('John', "Clarke", 14)
print(s1)
print(s1.fname)
print(s1.lname)
print(s1.age)

s2 = Student._make(['Andreas', 'Wallman', 20])
print(s2)
print(s2.fname)
print(s2.lname)
print(s2.age)

s3 = s1._asdict()
print(s3)

s4 = s2._replace(age = 25)

print(s2)
print(s4)
