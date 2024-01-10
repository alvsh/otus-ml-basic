# Создайте датакласс Engine, добавьте атрибуты volume и pistons
from dataclasses import dataclass


@dataclass
class Engine:
    volume: float
    pistons: int
