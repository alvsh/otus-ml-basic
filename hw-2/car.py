# Cоздайте класс Car
# - класс Car должен быть наследником Vehicle
# - добавьте атрибут engine классу Car
# - объявите метод set_engine, который принимает в себя экземпляр объекта Engine и устанавливает на текущий экземпляр Car

from vehicle import Vehicle
from engine import Engine


class Car(Vehicle):
    DEFAULT_WEIGHT = 1700
    DEFAULT_FUEL = 55.0
    DEFAULT_FUEL_CONSUMPTION = 11.0

    def __init__(self, weight=DEFAULT_WEIGHT, fuel=DEFAULT_FUEL, fuel_consumption=DEFAULT_FUEL_CONSUMPTION):
        super().__init__(weight, fuel, fuel_consumption)
        self._engine = None

    @property
    def engine(self):
        return self._engine

    def set_engine(self, engine):
        assert isinstance(engine, Engine)
        self._engine = engine
