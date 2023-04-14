from Tire import Tire


class Car:
    default_discount = 5  # Percentage
    number_of_tires = 4
    all_cars = []

    def __init__(self, base_price: float, mileage: float, year: int, maximum_speed: int, color: str, tire: Tire):
        self.year = year
        self.color = color
        self.maximum_speed = maximum_speed
        self.discount = Car.default_discount

        # Encapsulation
        self._mileage = mileage
        self.__base_price = base_price

        # Aggregation
        self.tire = tire

    def get_price(self) -> float:
        price_with_discount = self.__base_price * (1 - self.discount / 100)
        final_price = price_with_discount - self._mileage / 10000
        return final_price

    def is_used(self) -> bool:
        if self._mileage != 0:
            return False
        return True

    def description(self) -> None:
        print(f"This Car is created at {self.year}.")
        print(f"Color Of the car is {self.color}.")
        print(f"Maximum speed that you can drive is {self.maximum_speed} KM/H.")
        print(f"Mileage of this car is {self._mileage}.")
        print(f"Type of tiers is: {self.tire.type}.")
        print(f"You can buy it by: {self.get_price()}$ !")

    def set_discount(self, discount) -> None:
        self.discount = discount

    def set_mileage(self, mileage) -> None:
        self._mileage = mileage

    @staticmethod
    def accelerate() -> None:
        print("Vroom!")

    @staticmethod
    def horn() -> None:
        print("Beep!")

    @classmethod
    def get_all_cars(cls) -> list:
        return cls.all_cars
