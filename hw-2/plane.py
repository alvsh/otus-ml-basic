# - в модуле plane создайте класс Plane
# - класс Plane должен быть наследником Vehicle
# - добавьте атрибуты cargo и max_cargo классу Plane
# - добавьте max_cargo в инициализатор (переопределите родительский)
# - объявите метод load_cargo, который принимает число, проверяет, что в сумме с текущим cargo не будет перегруза,
#       и обновляет значение, в ином случае выкидывает исключение exceptions.CargoOverload
# - объявите метод remove_all_cargo, который обнуляет значение cargo и возвращает значение cargo,
#       которое было до обнуления

from vehicle import Vehicle
import exceptions


class Plane(Vehicle):

    DEFAULT_WEIGHT = 10000
    DEFAULT_FUEL = 1000.0
    DEFAULT_FUEL_CONSUMPTION = 100.0

    def __init__(self, max_cargo, weight=DEFAULT_WEIGHT, fuel=DEFAULT_FUEL, fuel_consumption=DEFAULT_FUEL_CONSUMPTION):
        super().__init__(weight, fuel, fuel_consumption)
        self._cargo = 0
        self._max_cargo = max_cargo

    @property
    def cargo(self):
        return self._cargo

    @property
    def max_cargo(self):
        return self._max_cargo

    def load_cargo(self, additional_cargo):
        new_cargo = self.cargo + additional_cargo
        if new_cargo > self.max_cargo:
            raise exceptions.CargoOverload
        else:
            self.cargo = new_cargo

    def remove_all_cargo(self):
        old_cargo = self._cargo
        self.cargo = 0
        return old_cargo
