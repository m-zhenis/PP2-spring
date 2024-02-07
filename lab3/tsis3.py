#1
class toUPPER:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())

b = toUPPER()
b.getString()
b.printString()

#2
class Shape:
    def __init__(self):
        pass

    def calculate_area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.side_length = length

    def calculate_area(self):
        return self.side_length * self.side_length

s = Square(int(input()))
print( s.calculate_area())

shape = Shape()
print(shape.calculate_area())

#3
class Rectangle:
    def __init__(self):
        pass

    def calculate_area(self):
        return 0

class Rarea(Rectangle):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


n , m = map(int, input().split())
r = Rarea(n, m)
print(r.calculate_area())

#4 Didn't understand how to do it

#5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} . New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Something went wrong")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} . New balance: {self.balance}")


n = int(input())
account = Account("Someone", n)

account.deposit(int(input()))
account.withdraw(int(input()))
account.withdraw(int(input()))  

#6
nums = range(1, 100 )
def is_prime (num) :
    for x in range(2, num):
        if (num%x) == 0:
            return False 
        return True
prime = list(filter(is_prime, nums))
print (prime)