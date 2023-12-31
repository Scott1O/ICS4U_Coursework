class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.__mileage = mileage
    
    @property
    def mileage(self):
        return self.__mileage

    def display_info(self):
        print(f"The Car's brand is: {self.brand}\nThe Car's model is: {self.model}\nThe Car's year is: {self.year}\nThe Car's mileage is: {self.mileage}.")

    def drive(self, distance):
        self.__mileage += distance
    

class ElectricCar(Car):
    def __init__(self, brand, model, year, mileage, battery_capacity):
        super().__init__(brand, model, year, mileage)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"The Car's Battery Capacity is: {self.battery_capacity}")

car1 = Car("Toyota", "Kia", 2018, 42069)
car1.display_info()

car1.drive(101)
car1.display_info()

# car2 = ElectricCar("Tesla", "Model S", 2021, 38621, 27)
# car2.display_info()