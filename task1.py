class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model},Year: {self.year}")
    
     
car1 = Car("Toyota", "Vios", 2013)
car2 = Car("Toyota", "Hiace", 1967)

print("Car 1:")
car1.display_info()
print("Car 2:")
car2.display_info()