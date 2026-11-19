# Q1
def apply_discount(price):
    a = price - price * 0.1
    return a
def add_gst(final_price):
    return final_price + final_price * 0.18
x = int(input())
print(add_gst(apply_discount(x)))    

# Q2
def add_bonus(marks):
    return marks + 5
def double_marks(final_marks):
    return final_marks * 2
x = int(input("Enter Marks: "))
print(f"final_price: {double_marks(add_bonus(x))}")


#Q3
def salary(x):
    return x + x * 0.20
def final_salary(y):
    return y - y * 0.10
a = int(input("ENter Ypur Salary: "))
print(f"Final_Salary: {final_salary(salary(a))}")


#Q4
import math
def add_ten(x):
    return x + 10
def square(y):
    return math.pow(y, 2)
a = int(input())
print(square(add_ten(a)))


#Q5
class car:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def show_speed(self):
        print("Top speed of " + self.name + " is 150 km/hr.")
    def car_color(self):
        print("The color of " + self.name + " car is " + self.color + ".")

honda = car("Honda city", "Red")
honda.show_speed()
honda.car_color()

#Q6
def double(x):
    return x * 2
def add_five(y):
    return y + 5

a = int(input("Enter Number: "))
print(f"Result: {add_five(double(a))}")
