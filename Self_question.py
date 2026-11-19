# =========  Def dunction (unit-4)  ============

# Q1
def add(a,b):
    """Returns the sum of two integers"""
    return a + b

a = int(input())
b = int(input())

print("Docstring:", add.__doc__)
print("sum:", add(a,b))


# Q2
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


#Q3
def log_value(x):
    print(f"logging: {x}")

def postive(x):
    if x > 0:
        return x
    return "None"
x = int(input())
print(f"log_value returned: {log_value(x)}")
print(f"check_postive returned: {postive(x)}")


# Q4
def greet(name,age):
    return f"Hello {name}, you are {age} years old"

name = input()
age = int(input())

print(greet(name,age))
print(greet(name,age))
print(greet(name,age))


#Q5
def nameage(*,name,age):
    return f"{name} {age}"

name1 = input()
age1 = int(input())
name2 = input()
age2 = int(input())

print(nameage(name = name1,age = age1))
print(nameage(name=name2,age=age2))


#Q6
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


#Q7
def fun1(name="padma", age=12):
    print(f"{name} is {age} years old")

name_0 = input()
age_0 = int(input())

fun1(name = name_0, age = age_0)
fun1(name = name_0,age = 16)
fun1(age = age_0)
fun1(name = name_0)
fun1()


#Q8
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


#Q9
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


#Q10
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



# Question 11
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


# question 12
Double_the_value = lambda x: x * 2
enter = int(input("Enter any Number: "))
print(Double_the_value(enter))
print(f"Function name: {Double_the_value.__name__}")


# Question 13
Total = lambda x,m,c: m * x + c

x = int(input("Enter value_1: "))
m = int(input("enter value_2: "))
c = int(input("Enter value_3: "))
print(f"Result: {Total(x,m,c)}")


#  question 14
classify = lambda n: ("Positive Even" if n % 2 == 0 else "Positive Odd") if n > 0 else "Non-Positive"

numbers = list(map(int, input("Enter Numbers: ").split()))
print(f"Result: {[classify(n) for n in numbers]}")


# question 15
numbers = list(map(int, input("Enter Numbers: ").split()))
double_the_values = list(map(lambda x: x ** 2, numbers))
print(f"Result: {double_the_values}")
