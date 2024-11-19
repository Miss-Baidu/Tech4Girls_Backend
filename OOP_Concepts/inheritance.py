class Employee:
    def __init__(self, name, position):
        """Initialize employee's name and position."""
        self.name = name
        self.position = position

    def get_details(self):
        """Display employee's details."""
        print(f"Name: {self.name}, Position: {self.position}")    


class Manager(Employee):
    def __init__(self, name, position, department):
        """Initialize manager's attributes, including inherited ones."""
        super().__init__(name, position)  
        self.department = department

    def get_details(self):
        """Display manager's details, including department."""
        print (f"Name: {self.name}, Position: {self.position}, Department: {self.department}")



employee1 = Employee("Biggles", "Developer")
print("Employee Details:")
print(employee1.get_details())


manager1 = Manager("Sarah", "Senior Manager", "IT")
print("\nManager Details:")
print(manager1.get_details())