# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle:
    def __init__(self, pass, price):
        this.price = price
        this.pass = pass

# Vehicle is the base class
class GroundVehicle(Vehicle):
    def __init__(self, pass, price, transmission):
        super().__init__(pass, price)
        this.transmission = transmission

class Car(GroundVehicle):
    def __init__(self, pass, price, transmission, brand, model):
        super().__init__(self, pass, price, transmission)
        this.brand = brand
        this.model = model