#从一个模块中导入多个类
from car import Car, ElectricCar

my_beetle = Car("volkswagen", "beetle", 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar("tesla", "roadster", 2016)
print(my_tesla.get_descriptive_name())


print("\n")
#导入整个模块
import car
my_beetle = car.Car("wolkswagen", "beetle", 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.Car("tesla", "roadster", 2016)
print(my_tesla.get_descriptive_name())


print("\n")
#导入模块中的所有类
from car import *
my_beetle = Car("wolkswagen", "beetle", 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar("tesla", "roadster", 2016)
print(my_tesla.get_descriptive_name())