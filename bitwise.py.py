#Bitwise operators Tasks(1-8)
#Task 1
a = 10
b = 6

print(a & b) #2

#Task2
x = 12
y = 5

print(x | y) # 13

#Task3
num = 8
print(~num) # -9

#Task4
a = 15
b = 9

print(a ^ b) # 6

#Task5
#Left shift operator
num = 7
print(num << 2) # 28

#Task6
#Right shift operator
num = 20
print(num >> 1) # 10

#Task7
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = a & b
print("AND result:", result) # 2

#Task8
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = a ^ b
print("XOR result:", result) # 9

#String Tasks(9-14)

#Task9
text = "hi"
print(text * 4) # hihihihi

#Task10
text = "python"
print(text * 3) # pythonpythonpython

#Task11
a = "super"
b = "man"

print(a + b) # superman

#Task12
a = "hello"
print(a + b ) # hello world

#Task13
name = input("Enter your name: ")
print(name * 5) # sharonsharonsharonsharonsharon

a = input("Enter first string: ")
b = input("Enter second string: ")

#Task14
result = a + b
print("Concatenated string:", result) # helloworld

#Input & Tpye casting Tasks(15-20)

#Task15
name = input("Enter your name: ")
print(type(name)) # sharon <class 'str'>

#Task16
age = int(input("Enter your age: "))
print(age) # 22

#Task17
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b
print("Sum:", sum) # 12

#Task18
mark1 = float(input("Enter first mark: "))
mark2 = float(input("Enter second mark: "))

average = (mark1 + mark2) / 2
print("Average:", average) # 85.0

#Task 19
a = int(input("Enter first number: "))
b = int(input("Enter second number: ")) 

3*a*2 + b - 2.

result = 3 * a * 2 + b - 2
print("Result:", result) # 27

#Task 20
num = input("Enter a number: ")

print("Before type casting:", type(num))

num = int(num)

print("After type casting:", type(num)) # 25 Before type casting:<class 'str'> After type casting:<clas 'int'>

#Unit Digit Tasks(21-25)
 
 #Task 21
num = input("Enter a number: ")
print("Last digit:", num[-1]) # 7

#Task 22
num = int(input("Enter a number: "))
print("Unit digit:", num % 10) # 7

#Task 23
num = int(input("Enter a number: "))
print("Number after removing last digit:", num // 10) # 45

#Task 24
num = int(input("Enter a number: "))
second_last = (num // 10) % 10
print("Second last digit:", second_last) # 5

#Task 25
num = int(input("Enter a 5 digit number: "))
print("Last digit:", num % 10) # 5

#Task 26
if 10 >= 5:
    print("10 is greater than or equal to 5") # 10 is greater than or equal to 5

#Task 27
num = int(input("Enter a number: "))

if num > 50:
    print("The number is greater than 50")
else:
    print("The number is not greater than 50") # Enter a number:60 The number is greater than 50

#Task 28
age = int(input("Enter your age: "))

if age >= 18:
    print("Age is greater than or equal to 18")
else:
    print("Age is less than 18") # Enter your age: 20 Age is greater than or equal to 18

#Task 29
num = int(input("Enter a number: "))

if num > 100:
    print("The number is greater than 100")
else:
    print("The number is not greater than 100") # Enter a number:150 The number is greater than 100


#Task 30
num = int(input("Enter a number: "))

if num >= 0:
    print("The number is greater than or equal to 0")
else:
    print("The number is less than 0") # Enter a number:-5 The number is less than 0

#If-Else Tasks(31-34)


#Task 31
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd") # Enter a number 7 The number is odd


#Task 32
marks = int(input("Enter marks: "))

if marks >= 35:
    print("Pass")
else:
    print("Fail") # Enter marks:40 Pass

#Task 33
num = int(input("Enter a number: "))

if num > 0:
    print("The number is Positive")
else:
    print("The number is Negative") # Enter a number:-8 The number is negative

#Task 34
num = int(input("Enter a number: "))
if num > 10:
    print("The number is greater than 10")
else:
    print("The number is not greater than 10") # Enter a number 15 The number is greater than 10

#Nested If Tasks(35-37)

#Task 35
age = int(input("Enter age: "))
height = int(input("Enter height (cm): "))
weight = int(input("Enter weight (kg): "))

if age >= 18 and height >= 160 and weight >= 60:
    print("Selected")
else:
    print("Rejected") # Enter age:20 Enter height(cm):165 Enter weight (kg):65  Selected

#Task 36
marks = int(input("Enter marks: "))
age = int(input("Enter age: "))

if marks >= 60 and age >= 17:
    print("Admission Granted")
else:
    print("Admission Denied") # Enter marks:70 Enter age:18 admission Granted

#Task 37
age = int(input("Enter age: "))
height = int(input("Enter height (cm): "))
weight = int(input("Enter weight (kg): "))

if age >= 16 and height >= 150 and weight >= 50:
    print("Selected for sports")
else:
    print("Not selected") # Enter age:17 Enter height (cm):155 Enter weight (kg):52 selected for sports


#Match statement Tasks(38-40)

#Task 38
day = int(input("Enter a number (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid number") # Enter a number(1-7):3 wednesday


#Task 39
num = int(input("Enter a number (1-3): "))

match num:
    case 1:
        print("Red")
    case 2:
        print("Blue")
    case 3:
        print("Green")
    case _:
        print("Invalid number") # Enter a number (1-3):2 Blue


#Task 40
num = int(input("Enter a number (1-4): "))

match num:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")
    case _:
        print("Invalid number") # Enter a number (1-4): 3 Orange





