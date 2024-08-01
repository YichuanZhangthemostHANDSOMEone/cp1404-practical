from car import Car
import random

class UnreliableCar(Car):
    """Represent a UnreliableCar object."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = float(reliability)
        self.drive_distance = 0

    def drive(self, distance):
        if random.randint(0, 100) < self.reliability:
            drive_distance = super().drive(distance)
        else:
            drive_distance = 0
        return drive_distance