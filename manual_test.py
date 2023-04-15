from Car import *
from Tire import *

tire = Tire(tire_type="tier type 1", description="this is a tire")
car = Car(base_price=1000, mileage=10, year=2010, maximum_speed=200, color="blue", tire=tire)
car = Car(base_price=5000, mileage=20000, year=2009, maximum_speed=100, color="red", tire=tire)

"""-------------------------------------------------------------------------------------------------------"""
"""-------------------------------------------- Car ------------------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------"""

# print(car.all_cars)
# print(car.number_of_tires)
# print(car._default_discount)
#
# car.description()
# print(car.get_price())
# car.horn()
# car.set_discount(10)
# car.set_mileage(0)
# print(car.get_price())
# print(car.all_cars)
# print(car.accelerate())
# print(car.is_used())
# car.description()
# print(car.get_all_cars())
# print(car.__dict__)
#

"""-------------------------------------------------------------------------------------------------------"""
"""-------------------------------------------- Electric Cars --------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------"""

# electric = ElectricCar(engine_description="electric car engine", base_price=1000, mileage=10, year=2010,
#                        maximum_speed=200, color="blue", tire=tire)
# print(electric.engine.__dict__)
# print(electric.get_all_cars())
# electric.set_mileage(1000)
# electric.description()
# electric.accelerate()
# print(electric.get_price())
# print(electric.get_all_cars()[-1])

# tesla = Tesla(engine_description="electric car engine", base_price=1000, mileage=10, year=2010,
#               maximum_speed=200, color="blue", tire=tire)
# tesla.description()

# zoox = Zoox(engine_description="electric car engine", base_price=1000, mileage=10, year=2010,
#             maximum_speed=200, color="blue", tire=tire)
#
# zoox.description()

# poleStar = PoleStar(engine_description="electric car engine", base_price=1000, mileage=10, year=2010,
#                     maximum_speed=200, color="blue", tire=tire)
#
# poleStar.description()

# nissan = Nissan(engine_description="electric car engine", base_price=1000, mileage=10, year=2010,
#                 maximum_speed=200, color="blue", tire=tire)

# nissan.description()

"""-------------------------------------------------------------------------------------------------------"""
"""-------------------------------------------- Diesel Cars ----------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------"""

# diesel = DieselCar(engine_description="diesel car engine", base_price=1000, mileage=10, year=2010,
#                    maximum_speed=200, color="blue", tire=tire)
# print(diesel.engine.__dict__)
# print(diesel.get_all_cars())
# diesel.set_mileage(1000)
# diesel.description()
# diesel.accelerate()
# print(diesel.get_price())
# print(diesel.get_all_cars()[-1])

# tata = Tata(engine_description="Diesel car engine", base_price=1000, mileage=10, year=2010,
#             maximum_speed=200, color="blue", tire=tire)
#
# tata.description()
#
# citreon = Citroen(engine_description="Diessel car engine", base_price=1000, mileage=10, year=2010,
#                   maximum_speed=200, color="blue", tire=tire)
#
# citreon.description()

"""-------------------------------------------------------------------------------------------------------"""
"""------------------------------------------ Gasoline Cars ----------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------"""

# gasoline = GasolineCar(engine_description="gasoline car engine", base_price=1000, mileage=10, year=2010,
#                        maximum_speed=200, color="blue", tire=tire)
# print(gasoline.engine.__dict__)
# print(gasoline.get_all_cars())
# gasoline.set_mileage(1000)
# gasoline.description()
# gasoline.accelerate()
# print(gasoline.get_price())
# print(gasoline.get_all_cars()[-1])

# hyundai = Hyundai(engine_description="Gasoline car engine", base_price=1000, mileage=10, year=2010,
#                   maximum_speed=200, color="blue", tire=tire)
#
# hyundai.description()
# print(hyundai.all_cars[-1].__dict__)
#
# chevrolet = Chevrolet(engine_description="Gasoline car engine", base_price=1000, mileage=10, year=2010,
#                       maximum_speed=200, color="blue", tire=tire)
#
# chevrolet.description()
# print(chevrolet.all_cars[-1].__dict__)
#
# toyota = Toyota(engine_description="Gasoline car engine", base_price=1000, mileage=10, year=2010,
#                 maximum_speed=200, color="blue", tire=tire)
#
# toyota.description()
# print(toyota.all_cars[-1].__dict__)
