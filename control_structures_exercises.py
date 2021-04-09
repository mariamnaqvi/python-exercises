# 1 Conditional Basics
# a. prompt the user for a day of the week, print out whether the day is Monday or not

day_of_week = input('What day is it today? ')
if day_of_week.capitalize() == 'Monday':
     print('Today is Monday')
else:
     print ('Today is not Monday')

# b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
day = input('What day is it today? ')
if day.capitalize() in weekday:
    print ("It is a weekday")
else: 
    print("It's the weekend - yay!")

# simpler:
weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
day = input('What day is it today? ')
if day.lower().startswith('s'):
    print('weekend'))
else:
    print('weekday')


# c. create variables and make up values for

# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

hours_worked = 45
hourly_rate = 10
overtime_rate = 15
week_paycheck = (hours_worked) * (hourly_rate)
hours_overtime = (hours_worked) - 40

if hours_overtime > 0:
    week_paycheck = (hours_worked) * (hourly_rate) + ((hours_overtime) * (overtime_rate))
else:
    week_paycheck = (hours_worked) * (hourly_rate)

print (week_paycheck)


# 2. Loop Basics

# a. While

# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.

# intitializing variable
i = 5
while i <= 15:
    print(i)
    i += 1 

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

i = 2
while i in range (2,101,2):
    print(i)
    i += 2

i = 2
while i < 101:
    print(i)
    i += 2

# Alter your loop to count backwards by 5's from 100 to -10.

i = 100
while i >= -10:
    print(i)
    i -= 5

# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
  
i = 2
while i < 1_000_000:
    print (i)
    i **= 2

# Write a loop that uses print to create the output shown below.
# 100
# 95
# 90
# 85
# 80
# 75
# 70
# 65
# 60
# 55
# 50
# 45
# 40
# 35
# 30
# 25
# 20
# 15
# 10
# 5

i = 100
while i > 0:
    print(i)
    i -= 5

# b. For Loops

# i. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

# For example, if the user enters 7, your program should output:

# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70

proposed_num = int(input('Enter a positive integer: '))

for n in range(1,11):
    print(f'{proposed_num} X {n} = {proposed_num * n}') 


# ii. Create a for loop that uses print to create the output shown below.
proposed_num = input('Enter a positive integer: ')
for n in range(1, int(proposed_num)+1):
    print(str(n) * n)

# c. break and continue

# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

while True:
    num_entered = input('Enter a number between 1 and 50: ')

    if num_entered.isdigit():
        if int(num_entered) % 2 == 1 and (1 < (int(num_entered)) < 50):
            break

for n in range(2,51):
    if n % 2 == 1:
        if n != int(num_entered):
            print(f'Here is an odd number: {n}')
        else:
            print('Skipped your number')

# d. The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

while True:

    num_entered = input('enter a positive number: ')

    if num_entered.isdigit():
        if int(num_entered) > 0:
            break

for n in range(0, int(num_entered) + 1):
    print (n)

# e. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.
while True:

    num_entered = input('Enter a positive number: ')

    if num_entered.isdigit():
        if int(num_entered) > 0:
            break

for n in range(int(num_entered), 0, -1):
    print (n)


# 3. Fizzbuzz
# Write a program that prints the numbers from 1 to 100.

for i in range(1,101):
    print (i)

# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(1,101):
#put most specific first
    if i % 3 == 0 and i % 5 == 0:
        print ("FizzBuzz")
     elif i % 3 == 0:
        print ("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    else:
        print(i)

# 4. Display a table of powers.

while True:
    i = int(input ('What number would you like to go up to? '))
    print('Here is your table!')
    print('number | squared | cubed')
    print('------ | ------- | -----')
    for i in range(1,i + 1):
        print(f'{i: 6} | {i**2: 7} | {i**3: 5}')

    cont = input('Would you like to continue? [y/n]')
    if cont != 'y':
        break
    

# 5. Convert given number grades into letter grades.

while True:
    grade = int(input('Enter a grade from 0 to 100: '))
    # can also use in range
    if grade >= 88:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 67:
        print("C")
    elif grade >= 60:
        print("D")
    else:
        print("F")
    continue_y_n = input("Would you like to continue? [y/n]")
    if not continue_y_n == "y":
        break

# 6. 

bookshelf = [
{'title' : 'Naked Statistics', 'author': 'Charles Wheelan', 'genre' : 'Non Fiction'},
{'title' : 'The Vanishing Half', 'author': 'Brit Bennett', 'genre' : 'Historical Fiction'},
{'title' : 'City of Margins', 'author': 'William Boyle', 'genre' : 'Thriller'},
{'title' : 'The City We Became', 'author': 'N.K. Jemisin', 'genre' : 'Fantasy'}
]
for book in bookshelf:
    [print(key, ': ', book[key]) for key in book]

genre = input("Select a genre: ").capitalize()
book_chosen = [book for book in bookshelf if book['genre'] == genre]

print(book_chosen)