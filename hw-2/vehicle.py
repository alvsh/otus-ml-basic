# Доработайте базовый класс Vehicle:
#
# добавьте атрибуты weight, started, fuel, fuel_consumption со значениями по умолчанию
# добавьте инициализатор для установки weight, fuel, fuel_consumption

# - добавьте метод start, который, если ещё не состояние started, проверяет, что топлива больше нуля, и обновляет состояние started, иначе выкидывает исключение exceptions.LowFuelError

# - добавьте метод move, который проверяет, что достаточно топлива для преодоления переданной дистанции, и изменяет количество оставшегося топлива, иначе выкидывает исключение exceptions.NotEnoughFuel

from abc import ABC

import exceptions

class Vehicle(ABC):

    DEFAULT_WEIGHT = 1600
    DEFAULT_FUEL = 50.0
    DEFAULT_FUEL_CONSUMPTION = 10.0

    def __init__(self, weight=DEFAULT_WEIGHT, fuel=DEFAULT_FUEL, fuel_consumption=DEFAULT_FUEL_CONSUMPTION):
        self._weight = weight
        self._fuel = fuel
        self._fuel_consumption = fuel_consumption
        self._started = False


    @property
    def weight(self):
        return self._weight

    @property
    def fuel(self):
        return self._fuel

    @property
    def fuel_consumption(self):
        return self._fuel_consumption

    @property
    def started(self):
        return self._started

    def start(self):
        if not self.started:
            if self.fuel > 0.0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    def move(self, distance):

        fuel_dist = distance / self.fuel_consumption

        if self.fuel > fuel_dist:
            self._fuel -= fuel_dist
        else:
            raise exceptions.NotEnoughFuel



