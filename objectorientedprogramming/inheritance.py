class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hello! My name is {self.name} and I am {self.age} years old."

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Order(Customer):  # Corrected with colon
    def __init__(self, name, age, price):
        super().__init__(name, age)  # Call the parent class initializer
        self.price = price

    def place_order(self):
        print(f"{self.name} has placed an order worth ${self.price}.")


# Create a user for the Customer class
customer1 = Customer("Daniel", 30)
print(customer1)
customer1.display()

# Create a user for the Order class
order1 = Order("Daniel", 30, 100)
print(order1)  # Inherited __str__ method
order1.place_order()
order1.display()  # Inherited method
