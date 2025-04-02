#print() in python examples 
print("Hello, Mufakosi!")

name = "Tatenda"
age = 25
print("Name:", name, "Age:", age)

print("The result is: " + str(22))

bread_price = 1.5
quantity = 3
print(f"Total: ${bread_price * quantity:.2f}")

print("Solo_leveling", "is", "awesome", sep="-")

print ("This is why", end="")
print (" you left me")

with open("output.txt", "w") as f:
    print("This goes to a file", file=f)

print("{} scored {} out of {}".format("Nyasha", 64, 100)) 

fruits = ["apple", "banana", "cherry"]
print(*fruits, sep=", ")

print("She said, \"Hello!\"\nAnd then left.\t(Goodbye)")

# Python Input Examples - Terminal Session
print("=== Python Input Examples ===")

# Example 1: Basic 
print("\n1. Basic String Input")
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Example 2: Numeric Input
print("\n2. Numeric Input")
age = int(input("Enter your age: "))
print(f"Next year you'll be {age + 1}")

# Example 3: Float Input with Validation
print("\n3. Float Input with Validation")
while True:
    try:
        weight = float(input("Enter weight (kg): "))
        break
    except ValueError:
        print("Invalid! Enter numbers only")
print(f"Weight: {weight}kg")

# Example 4: Multiple Values
print("\n4. Multiple Values")
x, y = input("Enter two numbers (space-separated): ").split()
print(f"Sum: {int(x) + int(y)}")

# Example 5: Menu Selection
print("\n5. Menu Selection")
print("1. Option A\n2. Option B\n3. Option C")
choice = input("Select (1-3): ")
print(f"You chose option {choice}")

# Example 6: Password Input
print("\n6. Password Input (simulated)")
password = input("Enter password (displayed for demo): ")
print("Password accepted!")

# Example 7: Yes/No Confirmation
print("\n7. Yes/No Confirmation")
response = input("Continue? (y/n): ").lower()
print("Continuing..." if response == 'y' else "Exiting")

# Example 8: List Input
print("\n8. List Input")
numbers = [int(n) for n in input("Enter numbers (comma-separated): ").split(',')]
print(f"List: {numbers}\nSum: {sum(numbers)}")

# Example 9: Date Validation
print("\n9. Date Validation")
from datetime import datetime
while True:
    date_str = input("Enter date (YYYY-MM-DD): ")
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        break
    except ValueError:
        print("Invalid format! Try again.")
print(f"Valid date: {date.date()}")

# Example 10: Continuous Input
print("\n10. Continuous Input")
items = []
print("Enter items ('done' to finish):")
while True:
    item = input("> ")
    if item.lower() == 'done':
        break
    items.append(item)
print(f"You entered: {', '.join(items)}")

print("\n=== All examples complete ===")

#variables
username = "tendy670"
print("Welcome,", username)

books = 8
pens = 5
total_stationery = books + pens
print("Total stationery:", total_stationery)

pi = 3.14159
radius = 5
area = pi * (radius ** 2)
print("Circle area:", area)

is_raining = True
if is_raining:
    print("Bring an umbrella!")
else:
    print("Enjoy the sunshine!")

colors = ["red", "green", "blue"]
colors.append("yellow")
print("Available colors:", colors)

dimensions = (1920, 1080)
print("Screen resolution:", dimensions[0], "x", dimensions[1])

user = {"name": "Jeff", "age": 28, "premium": True}
print(user["name"], "is premium member?", user["premium"])

status = "active"
print("Initial status:", status)
status = "inactive"
print("Updated status:", status)

x, y, z = 10, 20, 30
print("Before swap:", x, y, z)
x, y, z = z, x, y  # Rotate values
print("After swap:", x, y, z)

price = "19.99"  # String
actual_price = float(price)  # Convert to float
print("Price + tax:", actual_price * 1.1)

#maths in pyt

# 1. Basic arithmetic operations
print("1. 5 + 3 * 2 =", 5 + 3 * 2)  # Output: 11 (PEMDAS rule)

# 2. Using math module functions
import math
print("2. Square root of 16:", math.sqrt(16))  # Output: 4.0

# 3. Working with exponents
print("3. 2 to the power 5:", 2**5)  # Output: 32
print("   Using math.pow:", math.pow(2, 5))  # Output: 32.0

# 4. Trigonometric functions (angles in radians)
angle = math.radians(60)  # Convert 60 degrees to radians
print("4. Sine of 60°:", round(math.sin(angle), 2))  # Output: 0.87

# 5. Working with constants
print("5. Value of π:", math.pi)  # Output: 3.141592653589793
print("   Value of e:", math.e)   # Output: 2.718281828459045

# 6. Random number generation
import random
print("6. Random number between 1-100:", random.randint(1, 100))

# 7. Logarithmic calculations
print("7. Natural log of 10:", math.log(10))  # Output: ~2.302585
print("   Log base 10 of 100:", math.log10(100))  # Output: 2.0

# 8. Practical geometry: Circle calculations
radius = 7
circumference = 2 * math.pi * radius
area = math.pi * radius**2
print("8. Circle with radius 7:")
print(f"   Circumference: {round(circumference, 2)}")
print(f"   Area: {round(area, 2)}")

# 9. Working with complex numbers
c = 3 + 4j
print("9. Complex number operations:")
print("   Magnitude:", abs(c))  # Output: 5.0
print("   Real part:", c.real)  # Output: 3.0
print("   Imaginary part:", c.imag)  # Output: 4.0

# 10. Precision calculations with decimal
from decimal import Decimal, getcontext
getcontext().prec = 6  # Set precision to 6 digits
print("10. Precise decimal calculation:")
print("   0.1 + 0.2 (normal):", 0.1 + 0.2)  # Output: 0.30000000000000004
print("   0.1 + 0.2 (Decimal):", Decimal('0.1') + Decimal('0.2'))  # Output: 0.3

#typecasting 
# Example 1: Boolean to Integer
true_val = True
false_val = False
print(f"True to integer: {int(true_val)}")  # Output: 1
print(f"False to integer: {int(false_val)}")  # Output: 0

# Example 2: String (binary) to Integer
binary_str = "1010"
print(f"Binary '1010' to integer: {int(binary_str, 2)}")  # Output: 10

# Example 3: List to Set (removes duplicates)
colors = ["red", "blue", "red", "green"]
print(f"List to set: {set(colors)}")  # Output: {'red', 'blue', 'green'}

# Example 4: Integer to Hexadecimal String
num = 255
print(f"255 to hex string: {hex(num)}")  # Output: '0xff'

# Example 5: Float to Integer with rounding
price = 9.99
print(f"Float 9.99 to integer (rounded): {round(price)}")  # Output: 10

# Example 6: Tuple to List
coordinates = (10, 20, 30)
print(f"Tuple to list: {list(coordinates)}")  # Output: [10, 20, 30]

# Example 7: ASCII Character to Integer
char = 'A'
print(f"Character 'A' to ASCII code: {ord(char)}")  # Output: 65

# Example 8: Integer to ASCII Character
code = 97
print(f"ASCII code 97 to character: {chr(code)}")  # Output: 'a'

# Example 9: String Number to Complex
complex_str = "3+4j"
print(f"String '3+4j' to complex: {complex(complex_str)}")  # Output: (3+4j)

# Example 10: Dictionary to List of Keys
person = {"name": "Alice", "age": 25, "city": "Paris"}
print(f"Dict keys to list: {list(person.keys())}")  # Output: ['name', 'age', 'city']

#interger
# 1. Basic integer
age = 25
print(age)  # Output: 25

# 2. Negative integer
temperature = -10
print(temperature)  # Output: -10

# 3. Large integer
population = 7_900_000_000  # Underscores for readability
print(population)  # Output: 7900000000

# 4. Integer operations
sum = 5 + 3
print(sum)  # Output: 8

# 5. Integer division (floor division)
result = 7 // 2
print(result)  # Output: 3

# 6. Modulus (remainder)
remainder = 10 % 3
print(remainder)  # Output: 1

# 7. Exponentiation
power = 2 ** 3
print(power)  # Output: 8

# 8. Converting string to integer
num_str = "42"
num_int = int(num_str)
print(num_int)  # Output: 42

# 9. Binary literal
binary = 0b1010
print(binary)  # Output: 10

# 10. Hexadecimal literal
hex_num = 0xFF
print(hex_num)  # Output: 255

#float
# 1. Basic float
pi = 3.14159
print(pi)  # Output: 3.14159

# 2. Scientific notation
avogadro = 6.022e23
print(avogadro)  # Output: 6.022e+23

# 3. Negative float
temp = -20.5
print(temp)  # Output: -20.5

# 4. Float operations
result = 10.5 / 2.5
print(result)  # Output: 4.2

# 5. Rounding
rounded = round(3.14159, 2)
print(rounded)  # Output: 3.14

# 6. Float from string
float_str = "7.5"
float_num = float(float_str)
print(float_num)  # Output: 7.5

# 7. Infinity
infinity = float('inf')
print(infinity)  # Output: inf

# 8. Not a Number (NaN)
nan = float('nan')
print(nan)  # Output: nan

# 9. Float precision issue (common in many languages)
weird_math = 0.1 + 0.2
print(weird_math)  # Output: 0.30000000000000004

# 10. Converting integer to float
x = 5
x_float = float(x)
print(x_float)  # Output: 5.0

#string
# 1. Basic string
name = "Alice"
print(name)  # Output: Alice

# 2. Multiline string
poem = """Roses are red,
Violets are blue"""
print(poem)  # Output: Roses are red\nViolets are blue

# 3. String concatenation
greeting = "Hello" + " " + "World"
print(greeting)  # Output: Hello World

# 4. String repetition
laugh = "ha" * 3
print(laugh)  # Output: hahaha

# 5. String indexing
word = "Python"
print(word[0])  # Output: P

# 6. String slicing
print(word[2:4])  # Output: th

# 7. String methods
message = "hello world"
print(message.upper())  # Output: HELLO WORLD

# 8. String formatting (f-strings)
age = 30
print(f"I am {age} years old")  # Output: I am 30 years old

# 9. Escape characters
print("Line1\nLine2")  # Output: Line1\nLine2

# 10. Raw strings (ignores escape characters)
path = r"C:\new\folder"
print(path)  # Output: C:\new\folder

# list
# 1. Basic list
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# 2. List indexing
print(fruits[1])  # Output: banana

# 3. List slicing
print(fruits[0:2])  # Output: ['apple', 'banana']

# 4. Modifying list
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# 5. List methods
fruits.append("orange")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

# 6. List concatenation
vegetables = ["carrot", "potato"]
print(fruits + vegetables)  # Output: ['apple', 'blueberry', 'cherry', 'orange', 'carrot', 'potato']

# 7. Nested lists
matrix = [[1, 2], [3, 4]]
print(matrix[1][0])  # Output: 3

# 8. List comprehension
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# 9. Sorting
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4]

# 10. Copying lists
original = [1, 2, 3]
copy = original.copy()
copy.append(4)
print(original)  # Output: [1, 2, 3]
print(copy)     # Output: [1, 2, 3, 4]

#dictinary
# 1. Basic dictionary
person = {"name": "Alice", "age": 25}
print(person)  # Output: {'name': 'Alice', 'age': 25}

# 2. Accessing values
print(person["name"])  # Output: Alice

# 3. Adding new key-value pair
person["city"] = "New York"
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# 4. Dictionary methods
print(person.keys())  # Output: dict_keys(['name', 'age', 'city'])

# 5. Dictionary comprehension
squares = {x: x**2 for x in range(5)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 6. Nested dictionaries
contacts = {
    "Alice": {"phone": "123-4567", "email": "alice@example.com"},
    "Bob": {"phone": "890-1234"}
}
print(contacts["Alice"]["email"])  # Output: alice@example.com

# 7. Merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {**dict1, **dict2}
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}

# 8. Checking key existence
print("age" in person)  # Output: True

# 9. Default value with get()
print(person.get("country", "USA"))  # Output: USA

# 10. Removing items
removed = person.pop("age")
print(removed)  # Output: 25
print(person)   # Output: {'name': 'Alice', 'city': 'New York'}

#turples
# 1. Basic tuple
colors = ("red", "green", "blue")
print(colors)  # Output: ('red', 'green', 'blue')

# 2. Single-element tuple (note comma)
single = ("hello",)
print(type(single))  # Output: <class 'tuple'>

# 3. Tuple unpacking
x, y, z = colors
print(y)  # Output: green

# 4. Indexing
print(colors[2])  # Output: blue

# 5. Immutability test
# colors[1] = "yellow"  # Would raise TypeError

# 6. Tuple concatenation
more_colors = colors + ("yellow", "purple")
print(more_colors)  # Output: ('red', 'green', 'blue', 'yellow', 'purple')

# 7. Tuple repetition
print(colors * 2)  # Output: ('red', 'green', 'blue', 'red', 'green', 'blue')

# 8. Nested tuples
matrix = ((1, 2), (3, 4))
print(matrix[1][0])  # Output: 3

# 9. Tuple as dictionary key
locations = {(35.68, 139.76): "Tokyo", (40.71, -74.01): "New York"}
print(locations[(40.71, -74.01)])  # Output: New York

# 10. Converting list to tuple
fruits = ["apple", "banana"]
fruits_tuple = tuple(fruits)
print(fruits_tuple)  # Output: ('apple', 'banana')

#sets 
# 1. Basic set
unique_nums = {1, 2, 3, 3, 2}
print(unique_nums)  # Output: {1, 2, 3}

# 2. Empty set (note: {} makes a dictionary)
empty_set = set()
print(type(empty_set))  # Output: <class 'set'>

# 3. Adding elements
unique_nums.add(4)
print(unique_nums)  # Output: {1, 2, 3, 4}

# 4. Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # Union: {1, 2, 3, 4, 5}
print(a & b)  # Intersection: {3}
print(a - b)  # Difference: {1, 2}

# 5. Set comprehension
squares = {x**2 for x in range(5)}
print(squares)  # Output: {0, 1, 4, 9, 16}

# 6. Removing elements
unique_nums.discard(2)  # No error if missing
print(unique_nums)  # Output: {1, 3, 4}

# 7. Frozen set (immutable)
frozen = frozenset([1, 2, 3])
# frozen.add(4)  # Would raise AttributeError

# 8. Checking subset
print({1, 2}.issubset({1, 2, 3}))  # Output: True

# 9. Removing duplicates from list
duplicates = [1, 2, 2, 3]
unique = list(set(duplicates))
print(unique)  # Output: [1, 2, 3]

# 10. Symmetric difference
print(a ^ b)  # Output: {1, 2, 4, 5}

#booleans 
# 1. Basic booleans
is_active = True
is_admin = False
print(is_active)  # Output: True

# 2. Truthy/falsy values
print(bool(1))    # Output: True
print(bool(0))    # Output: False
print(bool(""))   # Output: False
print(bool([]))   # Output: False

# 3. Logical operators
print(True and False)  # Output: False
print(True or False)   # Output: True
print(not True)        # Output: False

# 4. Comparison operators
print(5 > 3)    # Output: True
print(5 == "5") # Output: False

# 5. Any/All functions
print(any([False, True, False]))  # Output: True
print(all([True, True, False]))  # Output: False

# 6. Boolean conversion
print(int(True))   # Output: 1
print(int(False))  # Output: 0

# 7. Short-circuit evaluation
def check():
    print("Checked!")
    return True
True or check()  # "Checked!" never prints

# 8. In operator
print(3 in [1, 2, 3])  # Output: True

# 9. Boolean algebra
print(True & False)  # Bitwise AND: False
print(True | False)  # Bitwise OR: True

# 10. XOR operation
print(True ^ True)   # Output: False
print(True ^ False)  # Output: True

#typecasting
# Example 1: Float to Integer
print("1. float to int:", int(3.99))  # Truncates (output: 3)

# Example 2: String to Integer
print("2. string to int:", int("42"))  # (output: 42)

# Example 3: Integer to Float
print("3. int to float:", float(7))  # (output: 7.0)

# Example 4: String to Float
print("4. string to float:", float("3.14"))  # (output: 3.14)

# Example 5: Integer to String
print("5. int to string:", str(100))  # (output: '100')

# Example 6: Boolean to Integer
print("6. bool to int:", int(True), int(False))  # (output: 1 0)

# Example 7: List to Tuple
print("7. list to tuple:", tuple([1, 2, 3]))  # (output: (1, 2, 3))

# Example 8: String to Boolean
print("8. string to bool:", bool("Hello"), bool(""))  # (output: True False)

# Example 9: Implicit Conversion (Int + Float)
print("9. implicit conversion:", 5 + 2.3)  # (output: 7.3)

# Example 10: Invalid Conversion (Will raise error)
try:
    print("10. invalid conversion:", int("abc"))
except ValueError as e:
    print("10. Error:", e)  # (output: invalid literal for int() with base 10: 'abc')

#function
 # 1. Basic function (no parameters)
def greet():
    print("Hello, Python!")
greet()  # Output: Hello, Python!

# 2. Function with parameters
def add(a, b):
    return a + b
print(add(5, 3))  # Output: 8

# 3. Function with default argument
def power(base, exp=2):
    return base ** exp
print(power(3))    # Output: 9 (default exp=2)
print(power(3, 3)) # Output: 27

# 4. Function returning multiple values
def min_max(nums):
    return min(nums), max(nums)
small, large = min_max([4, 2, 9, 7])
print(small, large)  # Output: 2 9

# 5. Variable-length arguments (*args)
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3))  # Output: 6

# 6. Keyword arguments (**kwargs)
def user_info(**data):
    for key, value in data.items():
        print(f"{key}: {value}")
user_info(name="Alice", age=25)  # Output: name: Alice \n age: 25

# 7. Lambda (anonymous) function
square = lambda x: x ** 2
print(square(4))  # Output: 16

# 8. Recursive function (factorial)
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)
print(factorial(5))  # Output: 120

# 9. Function inside a function
def outer():
    def inner():
        return "Inside inner"
    return inner()
print(outer())  # Output: Inside inner

# 10. Global vs local variables
x = 10  # Global
def modify_x():
    global x
    x = 20
modify_x()
print(x)  # Output: 20 (modified globally)

#loops
# 1. Basic for loop (list)
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Output: apple \n banana \n cherry

# 2. for loop with range()
for i in range(3):
    print(i, end=" ")  # Output: 0 1 2

# 3. for loop with enumerate (index + value)
colors = ["red", "green", "blue"]
for idx, color in enumerate(colors):
    print(idx, color)  # Output: 0 red \n 1 green \n 2 blue

# 4. Nested for loop (multiplication table)
for i in range(1, 3):
    for j in range(1, 3):
        print(f"{i}*{j}={i*j}", end=" ")  # Output: 1*1=1 1*2=2 2*1=2 2*2=4

# 5. for loop with else (executes after loop ends)
for num in [1, 2, 3]:
    print(num, end=" ")
else:
    print("Done!")  # Output: 1 2 3 Done!

# 6. while loop (countdown)
count = 3
while count > 0:
    print(count, end=" ")  # Output: 3 2 1
    count -= 1

# 7. while loop with break (exit early)
x = 0
while True:
    x += 1
    if x == 3:
        break
    print(x, end=" ")  # Output: 1 2

# 8. while loop with continue (skip iteration)
n = 0
while n < 5:
    n += 1
    if n == 3:
        continue
    print(n, end=" ")  # Output: 1 2 4 5

# 9. Loop control with pass (placeholder)
for i in range(2):
    pass  # Does nothing

# 10. Looping through a dictionary
user = {"name": "Bob", "age": 30}
for key, value in user.items():
    print(f"{key}: {value}")  # Output: name: Bob \n age: 30

