# Question (Constructor, self, Methods only):
# Create a class BankAccount that:
# Uses a constructor to take name and balance
# Has a method deposit(amount) to add money
# Has a method withdraw(amount) that subtracts money only if enough balance exists
# Has a method show_balance() to display the current balance
# Create one object and call all methods.

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(f"Current balance: {self.balance}")

# Creating an object of BankAccount
account = BankAccount("John Doe", 1000)
# Calling all methods
account.show_balance()  
account.deposit(500)
account.withdraw(200)
account.show_balance()
# Create a class LibraryBook that:
# Uses a constructor to take title, author, and copies (number of copies available).
# Has a method borrow_book() that decreases copies by 1 if copies are available, otherwise prints "No copies left".
# Has a method return_book() that increases copies by 1.
# Has a method show_details() to display the book’s title, author, and available copies.
# Create one object of LibraryBook and call all its methods at least once.
class LibraryBook():
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
    def borrow_book(self):
        if self.copies > 0:
            self.copies -= 1
            print(f"You have borrowed '{self.title}'. Copies left: {self.copies}")
        else:
            print("No copies left")
    def return_book(self):
        self.copies += 1
        print(f"You have returned '{self.title}'. Copies available: {self.copies}") 
    def show_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Available copies: {self.copies}")   
# Creating an object of LibraryBook
book = LibraryBook("1984", "George Orwell", 3)
# Calling all methods
book.show_details()
book.borrow_book()  
book.return_book()
book.show_details()

# Create a class Student that:
# Uses a constructor to take name and grades (a list of grades).
# Has a method add_grade(grade) to add a new grade to the list.
# Has a method calculate_average() that returns the average of the grades. 
# Has a method show_details() to display the student’s name and grades.
# Create one object of Student and call all its methods at least once.

class Student():
    def __init__(self, name, grades):
        self.name=name
        self.grades=grades
    def add_grade(self, grades):
        self.grades.append(grades)
        print(f"Added grade: {grades}. Current grades: {self.grades}")   
    def calculate_average(self):
        if self.grades:
            average = sum(self.grades) / len(self.grades)
            print(f"Average grade: {average}")
        else:
            print("No grades available to calculate average")

    def show_details(self):
        print(f"Student Name: {self.name}, Grades: {self.grades}")  
# Creating an object of Student
student = Student("Alice", [85, 90, 78])    
# Calling all methods
student.show_details()
student.add_grade(92)
student.calculate_average()