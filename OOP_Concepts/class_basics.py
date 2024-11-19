class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")

my_car1 = Car("Benz", "GLE", 2023)
my_car1.display_info()

my_car2 = Car("Rolls-Royce", "Phantom", 2023)
my_car2.display_info()

my_car3 = Car("BMW", "7 Series", 2023)
my_car3.display_info()