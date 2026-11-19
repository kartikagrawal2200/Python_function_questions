# =========  Def dunction (unit-4)  ============
# question 1
def display(v):
    print("Hello World")
    print("Good Morning")
    print("have a nice Day")
    print("The Function ends")
v = input()
display(v)

# question 2
def add(a,b):
    """Returns the sum of two integers"""
    return a + b

a = int(input())
b = int(input())

print("Docstring:", add.__doc__)
print("sum:", add(a,b))


# question 3
def addavg(a,b):
    print(f"sum and avg; ({a+b} {(a+b)/2})")
def sub(a,b):
    print(f"subtraction: {a-b}")
def mul(a,b):
    print(f"multiplication: {a*b}")

a = int(input())
b = int(input())

addavg(a,b)
sub(a,b)
mul(a,b)


# question 4
def log_value(x):
    print(f"logging: {x}")

def postive(x):
    if x > 0:
        return x
    return "None"
x = int(input())
print(f"log_value returned: {log_value(x)}")
print(f"check_postive returned: {postive(x)}")


# question 5
def greet(name,age):
    return f"Hello {name}, you are {age} years old"

name = input()
age = int(input())

print(greet(name,age))
print(greet(name,age))
print(greet(name,age))


# question 6
def nameage(*,name,age):
    return f"{name} {age}"

name1 = input()
age1 = int(input())
name2 = input()
age2 = int(input())

print(nameage(name = name1,age = age1))
print(nameage(name=name2,age=age2))


# question 7
def evalute_candidate(*,isRich,isYoung,isHandsome):
    if isRich == 1:
        print("The boy is Rich!")
    if isYoung == 1:
        print("The boy is the Right Age for you")
    if isHandsome == 1:
        print("The boy is GOOD LOOKING")
    if isRich != 1 and isYoung != 1 and isHandsome != 1: 
        print("No criteria met")

isRich = int(input())
isYoung = int(input())
isHandsome = int(input())

evalute_candidate(isRich = isRich, isYoung = isYoung, isHandsome = isHandsome)


# question 8
def fun1(name="padma", age=12):
    print(f"{name} is {age} years old")

name_0 = input()
age_0 = int(input())

fun1(name = name_0, age = age_0)
fun1(name = name_0,age = 16)
fun1(age = age_0)
fun1(name = name_0)
fun1()


# question 9
def append_item(item, target = None):
    if target is None:
        target = []
    target.append(item)
    return target

s1 = input()
s2 = input()
s3 = input()

list1 = append_item(s1) 
list2 = append_item(s2) 
list3 = append_item(s3, [s1]) 

print(list1)
print(list2)
print(list3)


# question 10
def mysum(*args):
    sum = 0
    for i  in range(len(args)):
        sum += int(args[i])
    return sum
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(mysum(a,b,c,d))
print(mysum(a,b,c)) 
print(mysum(a,b))


# question 11
def inspect_student(**kwargs):
    print(f"type: {type(kwargs)}")
    for key in sorted(kwargs):
        print(f"{key} = {kwargs[key]}")


line = input().strip()
pairs = {}

for item in line.split(","):
    if ":" in item:
        k, v = item.split(":", 1)
        pairs[k.strip()] = v.strip()

inspect_student(**pairs)



# Question 12
def build_report(title, *scores, scale=1, **meta):
    scaled_scores = tuple(s * scale for s in scores)
    sorted_meta = sorted(meta.items())
    return (title, scaled_scores, sorted_meta)


title = input().strip()
scores = [int(x) for x in input().split()]
scale = int(input().strip())
meta_line = input().strip()

meta = {}
for item in meta_line.split(","):
    if ":" in item:
        k, v = item.split(":", 1)
        meta[k.strip()] = v.strip()

print(build_report(title, *scores, scale=scale, **meta))


# question 13
Double_the_value = lambda x: x * 2
enter = int(input("Enter any Number: "))
print(Double_the_value(enter))
print(f"Function name: {Double_the_value.__name__}")


# Question 14
Total = lambda x,m,c: m * x + c

x = int(input("Enter value_1: "))
m = int(input("enter value_2: "))
c = int(input("Enter value_3: "))
print(f"Result: {Total(x,m,c)}")


#  question 15
classify = lambda n: ("Positive Even" if n % 2 == 0 else "Positive Odd") if n > 0 else "Non-Positive"

numbers = list(map(int, input("Enter Numbers: ").split()))
print(f"Result: {[classify(n) for n in numbers]}")


# question 16
numbers = list(map(int, input("Enter Numbers: ").split()))
double_the_values = list(map(lambda x: x ** 2, numbers))
print(f"Result: {double_the_values}")


# question 17
lst1 = map(int, input("Enter Numbers: ").split())
lst2 = map(int, input("Enter Numbers: ").split())
result = tuple(map(lambda x,y: x + y,lst1,lst2))
print(f"Result: {result}")


# question 18
lst = map(int, input("Enter Numbers: ").split())
even_numbers = list(filter(lambda x: x % 2 == 0, lst))
print(f"Result: {even_numbers}")


# question 19
lst1 = map(int, input("Enter Numbers: ").split())
lst2 = map(int, input("Enter Numbers: ").split())
common_elements = list(filter(lambda x: x in lst1,lst2))
print(common_elements)


# question 20
from functools import reduce

numbers = list(map(int, input("Enter Numbers: ").split()))

sub_result = reduce(lambda acc, x: acc - x, numbers)
prod_result = reduce(lambda acc, x: acc * x, numbers)

print(f"subtraction: {sub_result}")
print(f"product: {prod_result}")


# question 21
from functools import reduce

numbers = list(map(int, input("Enter Numbers: ").split()))
filtered = list(filter(lambda x: x > 0, numbers))      # reads from nums
mapped = list(map(lambda x: x ** 2, filtered))      # reads from filtered
total = reduce(lambda acc, x: acc + x, mapped)   # reads from mapped

print(f"filtered: {filtered}")
print(f"mapped: {mapped}")
print(f"total: {total}")


# question 22
details = input("Enter name and marks: ").strip()
items = []

for pair in details.split(","):
    if ":" in pair:
        name, score = pair.split(":", 1)
        items.append((name.strip(), int(score.strip())))

sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))
print(sorted_items)



