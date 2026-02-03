# Python Dataclass Example

This project demonstrates the basic usage of Python’s `@dataclass` decorator to create data-oriented classes with minimal boilerplate code.

## Example

```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    roll_no: int
    gpa: float

student = Student("Manal", 101, 3.8)
print(student)
