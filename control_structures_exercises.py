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
while i in range (-10, 101):
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
while i in range (5, 101):
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

# M code
proposed_num = int(input('Enter a positive integer: '))
for n in range(1,11):
    print (f'{proposed_num} X {n} = {proposed_num * n}')



i = input('Enter a number: ')
for n in range(1, 11):
    print(i, 'x', n, '=', i * n)
print(i)   
# this does not work

# but this does
i = 7
for n in range(1, 11):
   print(i, 'x', n, '=', i * n)

# ii. Create a for loop that uses print to create the output shown below.
proposed_num = input('Enter a positive integer: ')
for n in range(1,10):
    print(str(n) * n)



i = 1
count = 0
for i in range (1,10,1):
    print(i)
    count += 1
print(count)
# dont know how to make it print the number again

for i in range(1, 10):
    print (str(i)*i)
# dont understand how this works

# c. break and continue

# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

while True:
    posited_num = input('Enter an odd number between 1 and 50: ')
    # make sure input is valid as a digit
    if posited_num.isdigit():
        if int(posited_num) % 2 == 0 and int(posited_num) <= 50:
            break

posited_num = int([posited_num])
for num in range(1, 50, 2):
    if num == posited_num:
        print('Yikes!Skipping: ', num)
else:
    print('Here is an odd number: ', num)

# d. The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

while True:
    posited_num = input('Enter an odd number between 1 and 50: ')
    # make sure input is valid as a digit
    if posited_num.isdigit():
        if int(posited_num) > 0:
            break
# range does not include end so pos num + 1
posited_num = int([posited_num])
for num in range(0, posited_num + 1):
    print (num)
# e. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.




# 3. Fizzbuzz
# Write a program that prints the numbers from 1 to 100.

for i in range(1,101):
    print (i)

# For multiples of three print "Fizz" instead of the number

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print ("FizzBuzz")
    elif i % 5 == 0:
        print ("Buzz")
        #put most specific first
    elif i % 3 == 0:
        print ("Fizz")
    else:
        print(i)

# 4. Display a table of powers.

i = int(input('Enter a number: '))

for n in range(i):
    print (i ** 2) 
    print (i ** 3)
    if input("Do You Want To Continue? [y/n]") == "y":
    # now print square and cubed
        print (i ** 2) 
        print (i ** 3)
        for i in range (1, posited_num + 1):
            i_squared = i ** 2
            i_cubed = i ** 3
            print(f'{i: 6} | {i_squared: 7} | {i_cubed: 5}'')

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
{'title' : 'The Vanishing Half', 'author': 'Brit Bennett', 'genre' : 'Historical Fiction'},
{'title' : 'The Vanishing Half', 'author': 'Brit Bennett', 'genre' : 'Historical Fiction'},

]
for book in bookshelf:
    [print(key, ': ', book[key]) for key in book]

genre = input("Select a genre: ")
book_chosen = [book for book in bookshelf if book['genre'] == genre]

print(book_chosen)