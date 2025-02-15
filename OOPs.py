#OOPS concept in Python
class Car:    #class name should always have capital letter
    def __init__(self, brand, fuel_type):
        self.brand=brand
        self.fuel_type=fuel_type

    def drive(self, millage: float):
        print(f"{self.brand} has a millage of {millage}")

    def car_details(self):
        print(f"Car is {self.brand} and has {self.fuel_type} engine")

car1: Car=Car(brand="BMW", fuel_type="Diesel")
car2 =Car(brand="Benz", fuel_type="Petrol")

print(car1.brand)
car1.car_details()
