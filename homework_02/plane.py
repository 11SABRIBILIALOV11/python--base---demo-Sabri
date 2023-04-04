"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self,
                 weight: int,
                 fuel: int,
                 fuel_consuption: int,
                 max_cargo: int):
        super().__init__(weight,fuel,fuel_consuption)
        self.cargo = 0
        self.max_cargo = max_cargo





    def load_cargo(self,added_load: int):


        if self.cargo + added_load > self.max_cargo:
            raise CargoOverload
        self.cargo += added_load


    def remove_all_cargo(self) -> int:


        result = self.cargo
        self.cargo = 0
        return result


