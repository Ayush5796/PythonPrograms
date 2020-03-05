class Car():
    """This class is a blueprint for a Car model"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    
    def get_descriptive_name(self):
        """Return a neat descriptive name of the car"""
        long_name = self.make + " " + self.model + " " + str(self.year)
        return long_name.title()
    

    def read_odometer(self):
        print("The car has " + str(self.odometer_reading) + " miles on it.")

    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def update_odometer(self, mileage):
        """This method updates the attribute ododmeter_reading"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        
        else:
            print("You can't rollbak the odometer reading!!!")

first_car = Car('audi', 'a4', 2014)

print(first_car.get_descriptive_name())
first_car.update_odometer(2000)
first_car.read_odometer()

used_car = Car('subaru', 'wrx', 2018)

print(used_car.get_descriptive_name())
used_car.update_odometer(23500)
used_car.increment_odometer(700)
used_car.read_odometer()
used_car.update_odometer(500)

class ElectricCar(Car):
    """This is a child class of super class Car"""
    super().__init__(self, make, model, year)
    self.type = "EV"
    self.battery_size = 70


    def describe_battery(self):
        print("This car is of type: " + self.type)
        print("This car has a " + str(self.batter_size) + "kWh battery")

    
my_tesla = ElectricCar('tesla', 'model s' , 2019)

my_tesla.get_descriptive_name()
my_tesla.describe_battery()