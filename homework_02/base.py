from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):

    def __init__(self, weight = 0, fuel = 0, fuel_consumption = 0):


        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False


    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError
        else:
             return True


    def move(self, distance: int):
        required_fuel = distance * self.fuel_consumption

        if  required_fuel  <= self.fuel:

           self. fuel -= required_fuel
        else:
            raise NotEnoughFuel
