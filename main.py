# -------------------------
# Basic Python Tutorial
# -------------------------

# 1. COMMENTS
# Use the `#` symbol to add comments. Comments are ignored by the Python interpreter and are for human readers only.
# This is a single-line comment.
"""
This is a multi-line comment,
also called a docstring.
"""

# 2. VARIABLES
# Variables store information that can be used later in the code. Use descriptive names!
name = "Alice"          # A string variable (text)
age = 25                # An integer variable (whole number)
height = 5.7            # A float variable (decimal number)
is_student = True       # A boolean variable (True or False)

# Print variables to the console using the `print` function
print(name)             # Output: Alice
print(age)              # Output: 25

# 3. DATA TYPES
# Common data types: string (str), integer (int), float (float), and boolean (bool)

# 4. OPERATORS
# Arithmetic operators: +, -, *, /, % (modulus), ** (exponent)
x = 10
y = 3
sum_result = x + y      # Addition
difference = x - y      # Subtraction
product = x * y         # Multiplication
quotient = x / y        # Division (gives a float)
power = x ** y          # Exponent (10^3)

print(sum_result)       # Output: 13
print(power)            # Output: 1000

# 5. STRINGS
# Strings are text, created using single ('') or double ("") quotes
greeting = "Hello, " + name + "!"  # String concatenation
print(greeting)                    # Output: Hello, Alice!

# String formatting with f-strings
formatted_string = f"{name} is {age} years old."
print(formatted_string)            # Output: Alice is 25 years old.

# 6. CONDITIONALS
# Use `if`, `elif`, and `else` to make decisions in code
if age < 18:
    print("Minor")
elif age == 18:
    print("Just turned adult")
else:
    print("Adult")

# 7. LOOPS
# `for` loops and `while` loops let us repeat actions

# For loop
for i in range(5):          # range(5) generates numbers 0, 1, 2, 3, 4
    print(i)                # Output: 0, 1, 2, 3, 4 (each on a new line)

# While loop
count = 0
while count < 5:
    print(count)            # Output: 0, 1, 2, 3, 4
    count += 1              # Same as count = count + 1

# 8. FUNCTIONS
# Functions are blocks of code that perform a specific task and can be reused

def greet_user(username):
    """This function greets the user by name."""
    return f"Hello, {username}!"

print(greet_user("Bob"))    # Output: Hello, Bob!

# 9. LISTS
# Lists are collections of items that are ordered and changeable
fruits = ["apple", "banana", "cherry"]
fruits.append("date")       # Add a new item
print(fruits)               # Output: ['apple', 'banana', 'cherry', 'date']

# 10. DICTIONARIES
# Dictionaries are collections of key-value pairs
student = {
    "name": "Alice",
    "age": 25,
    "is_student": True
}
print(student["name"])      # Access a value by key, Output: Alice

# 11. IMPORTING MODULES
# Python has many built-in modules. Use `import` to include them in your code
import math

print(math.sqrt(16))        # Square root function from math module, Output: 4.0

# ------------------------------------
# End of Tutorial
# ------------------------------------
