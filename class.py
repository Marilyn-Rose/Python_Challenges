# Write a python program that simultates a simple car class, allowing you 
# to create car instance, accelerate them, and displa their curren speeds.

# first define the car class
class Car:
    #the class attribute for its max speed
    max_speed = 120 
    
    # the constructor method with the parameters
    def __init__(self, car_make, model, color, speed=0):
        self.car_make = car_make
        self.model = model
        self.color = color
        self.speed = speed
    
    # instance methods that allows the car to accelerate. and if the accelerate
    # does not exceed the max speed, then update the car's speed attribute
    # otherwise set speed to the max speed   
    def accelerate(self, acceleration):
        if self.speed + acceleration <= Car.max_speed:
            self.speed += acceleration
        else:
            self.speed = Car.max_speed
    
    # instance method that returns the current speed of the car
    def get_speed(self):
        return self.speed

# instantiate two objects of the Car class 
car1 = Car("Toyota", "Camry", "Blue")
car2 = Car("Honda", "Civic", "Red")

# using the accelerate method, increse the speed of car1 by 30km/h
# and car2 by 20km/h
car1.accelerate(30)
car2.accelerate(20)

# display the current speed of each car by utitlizing the ger_speed method
print(f" The {car1.color} {car1.car_make} {car1.model} is currently at {car1.get_speed()} km/h.")
print(f" The {car2.color} {car2.car_make} {car2.model} is currently at {car2.get_speed()} km/h.")