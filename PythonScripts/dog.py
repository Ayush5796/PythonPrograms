class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print("The dog " + self.name.title() + " is sitting")
    
    def roll_over(self):
        print(
            "The dog named " + self.name.title() + " whose age is " + 
            str(self.age) + " is rolling over"
            )

my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title())
print("His age is " + str(my_dog.age))

your_dog = Dog('Lucy', 8)
print("My dog's name is " + your_dog.name.title())
print("His age is " + str(your_dog.age))


my_dog.sit()
my_dog.roll_over()

your_dog.sit()
your_dog.roll_over()
