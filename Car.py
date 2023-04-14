from Engine import Engine, EngineTypeEnum
from Tire import Tire


class Car:
    _default_discount = 5  # Percentage
    number_of_tires = 4
    all_cars = []

    def __init__(self, base_price: float, mileage: float, year: int, maximum_speed: int, color: str,
                 tire: Tire):
        self.__car_id = len(Car.all_cars) + 1
        self.year = year
        self.color = color
        self.maximum_speed = maximum_speed
        self.discount = Car._default_discount

        # Encapsulation
        self._mileage = mileage  # Kilometers
        self.__base_price = base_price

        # Aggregation
        self.tire = tire

        # Append Car
        Car.all_cars.append(self)

    def get_price(self) -> float:
        price_with_discount = self.__base_price * (1 - self.discount / 100)
        final_price = price_with_discount - self._mileage / 100
        return final_price

    def is_used(self) -> bool:
        if self._mileage != 0:
            return False
        return True

    def update(self) -> None:
        for index in range(len(Car.all_cars)):
            if Car.all_cars[index].__car_id == self.__car_id:
                Car.all_cars[index] = self
                break

    def description(self) -> None:
        print(f"This Car is created at {self.year}.")
        print(f"Color Of the car is {self.color}.")
        print(f"Maximum speed that you can drive is {self.maximum_speed} KM/H.")
        print(f"Mileage of this car is {self._mileage}.")
        print(f"Type of tiers is: {self.tire.type}.")
        print(f"You can buy it by: {self.get_price()}$ !")

    def set_discount(self, discount) -> None:
        self.discount = discount
        self.update()

    def set_mileage(self, mileage) -> None:
        self._mileage = mileage
        self.update()

    @staticmethod
    def accelerate() -> None:
        print("Vroom!")

    @staticmethod
    def horn() -> None:
        print("Beep!")

    @classmethod
    def get_all_cars(cls) -> list:
        return cls.all_cars


"""-------------------------------------------------------------------------------------------------------"""
"""--------------------------------------- Electric Cars -------------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------"""


class ElectricCar(Car):
    def __init__(self, engine_description, **car_values):
        super().__init__(**car_values)
        self.engine = Engine(engine_type=EngineTypeEnum.ELECTRIC, description=engine_description)  # Composition

        # We should append car with updated values into the list
        super(Car, self).all_cars[-1] = self

    def get_price(self) -> float:
        price_with_discount = self.__base_price * (1 - self.discount / 100)
        final_price = price_with_discount - self._mileage / 1000
        return final_price

    def description(self) -> None:
        print(f"This is an electric car.")
        super(self).description()
        print(f"This is the description Of it's engine: {self.engine.description}")

    @staticmethod
    def accelerate() -> None:
        print("Silence ;)")


class Tesla(ElectricCar):

    def __init__(self, **electric_car_values):
        super().__init__(**electric_car_values)

    def description(self) -> None:
        print(f"This is tesla from Elon Mask!")
        super(ElectricCar, self).description()


class Nissan(ElectricCar):

    def __init__(self, **electric_car_values):
        super().__init__(**electric_car_values)

    def description(self) -> None:
        print(f"This is a nissan!")
        super(ElectricCar, self).description()


class PoleStar(ElectricCar):

    def __init__(self, **electric_car_values):
        super().__init__(**electric_car_values)

    def description(self) -> None:
        print(f"This is a pole star car!")
        super(ElectricCar, self).description()


class Zoox(ElectricCar):

    def __init__(self, **electric_car_values):
        super().__init__(**electric_car_values)

    def description(self) -> None:
        print(f"This is a zoox car!")
        super(ElectricCar, self).description()


"""-------------------------------------------------------------------------------------------------------"""
"""--------------------------------------- Diesel Cars ---------------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------"""


class DieselCar(Car):
    def __init__(self, engine_description, **car_values):
        super().__init__(**car_values)
        self.engine = Engine(engine_type=EngineTypeEnum.DIESEL, description=engine_description)  # Composition

        # We should append car with updated values into the list
        super(Car, self).all_cars[-1] = self

    def get_price(self) -> float:
        price_with_discount = self.__base_price * (1 - self.discount / 100)
        final_price = price_with_discount - self._mileage / 500
        return final_price

    def description(self) -> None:
        print(f"This is a diesel car.")
        super(self).description()
        print(f"This is the description Of it's engine: {self.engine.description}")

    @staticmethod
    def accelerate() -> None:
        print("Boom @-@")


class Citroen(DieselCar):

    def __init__(self, **diesel_car_values):
        super().__init__(**diesel_car_values)

    def description(self) -> None:
        print(f"This is a hyundai car!")
        super(DieselCar, self).description()


class Tata(DieselCar):

    def __init__(self, **diesel_car_values):
        super().__init__(**diesel_car_values)

    def description(self) -> None:
        print(f"This is a hyundai car!")
        super(DieselCar, self).description()


"""-------------------------------------------------------------------------------------------------------"""
"""--------------------------------------- Gasoline Cars -------------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------"""


class GasolineCar(Car):
    def __init__(self, engine_description, **car_values):
        super().__init__(**car_values)
        self.engine = Engine(engine_type=EngineTypeEnum.GASOLINE, description=engine_description)  # Composition

        # We should append car with updated values into the list
        super(Car, self).all_cars[-1] = self

    def get_price(self) -> float:
        price_with_discount = self.__base_price * (1 - self.discount / 100)
        final_price = price_with_discount - self._mileage / 2000
        return final_price

    def description(self) -> None:
        print(f"This is a gasoline car.")
        super(self).description()
        print(f"This is the description Of it's engine: {self.engine.description}")


class Hyundai(GasolineCar):

    def __init__(self, **gasoline_car_values):
        super().__init__(**gasoline_car_values)

    def description(self) -> None:
        print(f"This is a hyundai car!")
        super(GasolineCar, self).description()


class Chevrolet(GasolineCar):

    def __init__(self, **gasoline_car_values):
        super().__init__(**gasoline_car_values)

    def description(self) -> None:
        print(f"This is a chevrolet car!")
        super(GasolineCar, self).description()


class Toyota(GasolineCar):

    def __init__(self, **gasoline_car_values):
        super().__init__(**gasoline_car_values)

    def description(self) -> None:
        print(f"This is a toyota car!")
        super(GasolineCar, self).description()
