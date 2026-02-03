# Dataclasses
# In python, a dataclass is a decorator and a function that 
# automatically generates special methods like `__init__()`
# , `__repr__()`, and `__eq__()` for user-defined classes. 
# This is particularly useful for classes that are primarily
# used to store data, as it reduces boilerplate code and
# makes the code more readable.
# To use dataclasses, you need to import the `dataclass`

from dataclasses import dataclass
# decorator from the `dataclasses` module.
@dataclass
class Point:
    x: int
    y: int
# The `Point` class above is a simple dataclass with two
# attributes: `x` and `y`. The `@dataclass` decorator automatically     
# generates the `__init__`, `__repr__`, and `__eq__` methods for this class.
# You can create instances of the `Point` class like this:
p1 = Point(1, 2)
p2 = Point(1, 2)
# You can also compare instances of the `Point` class:  
print(p1 == p2)  # Output: True
# And you can get a string representation of the instance:
print(p1)        # Output: Point(x=1, y=2)

@dataclass
class Person:
    name: str
    age: int
    email: str  # Default value for email
# The `Person` class above is another dataclass with three
# attributes: `name`, `age`, and `email`.
person1 = Person("Alice", 30, "alice@example.com")
print(person1.age)

@dataclass
class Rectangle:
    width: float
    height: float

    def area(self) -> float:
        return self.width * self.height
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
# The `Rectangle` class above is a dataclass with two
# attributes: `width` and `height`. It also includes    
# methods to calculate the area and perimeter of the rectangle.
rect = Rectangle(4.0, 5.0)
print(rect.area())       # Output: 20.0
print(rect.perimeter())  # Output: 18.0
# In summary, dataclasses in Python provide a convenient
# way to define classes that are primarily used to store data,
# reducing boilerplate code and enhancing readability.


#inheritance with dataclasses
@dataclass
class Person:
    name: str
    age: int
@dataclass
class Employee(Person):
    employee_id: int
    position: str
employee = Employee("Bob", 28, 12345, "Developer")
print(employee)  # Output: Employee(name='Bob', age=28, employee_id=12345, position='Developer')

# Nested dataclasses
@dataclass
class Address:
    street: str
    city: str
    zip_code: str
@dataclass
class Person:
    name: str
    address: Address

address = Address("123 Main St", "Springfield", "12345")
person = Person("Charlie", address) 
print(person)  # Output: Person(name='Charlie', address=Address(street='123 Main St', city='Springfield', zip_code='12345'))
# You can also create nested dataclasses, where one dataclass
# contains another dataclass as an attribute. In the example    
# above, the `Person` class contains an `Address` dataclass as
# an attribute.
print(person.address.city) # Output: 'Springfield'
print(person.address.street) # Output: '123 Main St'