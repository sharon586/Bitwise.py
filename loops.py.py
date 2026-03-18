# Section 1: Loop Basics (1–10)
# Print numbers from 1 to 50 using for loop
for i in range(1,51):
    print(i)

# Print even numbers from 1 to 100
for i in range(1,101):
    if i%2 == 0:
        print(i)

# Print odd numbers from 1 to 100
for i in range(1,101):
    if i%2 != 0:
        print(i)

# Print multiplication table of 7
n = 7
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

# Find sum of numbers from 1 to 100
total = 0
for i in range(1,101):
    total +=i
print(total)

# Print numbers in reverse from 50 to 1
n = 50
while n>=1:
    print(n)
    n-=1

# Count how many numbers are divisible by 3 (1–100)
list1 = []
for i in range(1,100):
    if i%3 == 0:
        list1.append(i)
print(list1)
print("The Numbers divisible by 3 from 1-100 are : ",len(list1))

# Print squares of numbers from 1 to 10
for i in range(1,11):
    print(i**2)

# Print cube of first 10 numbers
for i in range(1,11):
    print(i**3)

# Take input n, print numbers from 1 to n
n = int(input("Enter the number: "))
for i in range(1,n):
    print(i)

#  Section 2: While Loop (11–15)

# Print numbers from 1 to 20 using while
n = 1
while n<=20:
    print(n)
    n+=1

# Find factorial of a number using while
n = int(input("Enter a number: "))
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print(f"Factorial of {n} is {factorial}")

# Reverse a number using while
n = int(input("Enter a number: "))
original = n
reversed_num = 0

while n > 0:
    digit = n % 10
    reversed_num = reversed_num * 10 + digit
    n = n // 10

print(f"Original number  : {original}")
print(f"Reversed number  : {reversed_num}")

# Count digits in a number
n = int(input("Enter a number: "))
count = 0
temp = abs(n)
while temp > 0:
    temp = temp // 10
    count += 1

print(f"Number of digits in {n} : {count}")
# Keep asking input until user enters "stop"
while True:
    user = input("Enter something (type 'stop' to quit): ")
    if user == "stop":
        print("User Stopped!")
        break
    print(f"You entered: {user}")




#  Section 3: Nested Loop (16–20)

# Print pattern:
# *
# **
# ***
# ****
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()

# Print pattern:
# 1
# 12
# 123
# 1234
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Print multiplication table (1 to 5) using nested loop
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:4}", end="")
    print()

# Print:
# A B C
# A B C
# A B C
for i in range(3):
    for j in range(3):
        print(chr(65 + j), end=" ")
    print()

# Print:
# 1 2 3
# 4 5 6
# 7 8 9
num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()




# Section 4: String Basics (21–25)

# Count total characters in a string
text = input("Enter a string: ")
count = 0
for char in text:
    count += 1
print(f"Total characters: {count}")

# Count vowels in a string
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(f"Number of vowels: {count}")

# Count consonants in a string
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char.isalpha() and char not in vowels:
        count += 1

print(f"Number of consonants: {count}")

# Reverse a string using loop
text = input("Enter a string: ")
reversed_str = ""

for char in text:
    reversed_str = char + reversed_str

print(f"Original : {text}")
print(f"Reversed : {reversed_str}")

# Check if string is palindrome
text = input("Enter a string: ").lower()
reversed_str = text[::-1]

if text == reversed_str:
    print(f"'{text}' is a Palindrome.")
else:
    print(f"'{text}' is not a Palindrome.")




# Section 5: String Slicing (26–30)

# Print first 5 characters of a string
char = input("Enter a string: ")
print(f"First 5 characters: {char[:5]}")

# Print last 3 characters
char = input("Enter a string: ")
print(f"Last 3 characters: {char[-3:]}")

# Print string in reverse using slicing
char = input("Enter a string: ")
print(f"Reverse string: {char[::-1]}")

# Print every 2nd character
char = input("Enter a string: ")
print(f"Every 2nd  character: {char[::2]}")

# Remove first and last character from string
char = input("Enter a string: ")
print(f"Original string  : {char}")
print(f"After removing   : {char[1:-1]}")




# Section 6: List Basics (31–35)

# Create a list of 5 numbers and print sum
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(f"Sum : {total}")

# Find maximum value in list
numbers = [10, 45, 23, 67, 32]
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print(f"Maximum value : {maximum}")

# Find minimum value in list
numbers = [10, 45, 23, 67, 32]
minimum = numbers[0]
for num in numbers:
    if num < minimum:
        minimum = num
print(f"Minimum value : {minimum}")

# Count total elements in list
numbers = [10, 45, 23, 67, 32]
count = 0
for num in numbers:
    count += 1
print(f"Total elements : {count}")

# Check if element exists in list
numbers = [10, 45, 23, 67, 32]
search = int(input("Enter the number: "))
found = False
for num in numbers:
    if num == search:
        found = True
        break
print(f"{search} {' Found' if found else  'Not found'} in list")




# Section 7: List Operations (36–40)

# Add 3 elements using append()
fruits = ["Apple", "Banana"]
print(f"Original list : {fruits}")

fruits.append("Mango")
fruits.append("Orange")
fruits.append("Grapes")

print(f"After append  : {fruits}")

# Insert element at specific index
fruits = ["Apple", "Banana", "Mango"]
print(f"Original list : {fruits}")

fruits.insert(1, "Orange")
print(f"After insert  : {fruits}")

# Remove element using remove()
fruits = ["Apple", "Banana", "Mango", "Orange", "Banana"]
print(f"Original list : {fruits}")

fruits.remove("Mango")
print(f"After remove  : {fruits}")

# Reverse list without using .reverse()
numbers = [1, 2, 3, 4, 5]
print(f"Original list : {numbers}")
reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])
print(f"Reversed      : {reversed_list}")

# Sort list without using .sort()
numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"Original list : {numbers}")
n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print(f"Sorted (Asc)  : {numbers}")


