class Vehicles():
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def seat_capacity(self, seat_capacity):
        self.seat_capacity = seat_capacity

    def display_properties(self):
        print("Color: ", self.color)
        print("maximum speed: ", self.max_speed)
        print("mileage: ", self.mileage)
        print("Seating Capacity: ", self.seat_capacity)

vehicles1 = Vehicles(200, 20)
vehicles1.seat_capacity(5)
vehicles1.display_properties()
    
vehicles2 = Vehicles(180, 25)
vehicles2.seat_capacity(4)
vehicles2.display_properties()