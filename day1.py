print("Hello, python!!")
#This is a single line comment
name = "ananya"
age = 20
height = 504
is_student = True
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
a = 10
b = 3
print(a + b, a - b, a * b, a / b, a % b, a ** b, a // b)
print(a > b, a == b)
print(a > 5 and b < 5)
name = input("Enter your name: ")
print("hello, " + name)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a= a + b
b = a - b
a = a - b
print("After swapping:",a,b)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Ent operation (+ - * /): ")

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    if num2 != 0:
       print("Result:", num1 / num2) 
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid operation")        

celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

for i in range(1, 11):
    print(i, end=" ")
print()

num = float(input("ENter a number: "))

if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")

total_minutes = int(input("Enter total minutes: "))

hours = total_minutes // 60
minutes = total_minutes % 60

print(f"{total_minutes} minutes = {hours} hour(s) and {minutes} minute(s)")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = 0
for i in range(abs(num2)):
    result += num1

if num2 < 0:
    result = -result
print(f"{num1} x {num2} = {result}")

# Program to find the largest of 3 numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"The largest number is {largest}")
