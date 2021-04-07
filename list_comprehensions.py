# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    
# Exercise 1 - rewrite the above example code using list comprehension syntax. 
# Make a variable named uppercased_fruits to hold the output of the list comprehension. 
# Output should be ['MANGO', 'KIWI', etc...]

# as list comprehension
uppercased_fruits = [fruit.upper() for fruit in fruits]

# as for loop
uppercased_fruits
for fruit in fruits:
    uppercased_fruits.append(fruit.upper())
print ('uppercased_fruits:')
print (uppercased_fruits)

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output 
# like ['Mango', 'Kiwi', 'Strawberry', etc...

# as list comprehension
capitalized_fruits = [fruit.capitalize() for fruit in fruits]

# as for loop
capitalized_fruits = []
for fruit in fruits:
    capitalized_fruits.append(fruit.capitalize()) 
print ('capitalized_fruits:')
print (capitalized_fruits)

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. 
# Hint: You'll need a way to check if something is a vowel.

# as list comprehension
def count_vowels(string):
    count = 0 
    for letter in string:
        if letter in 'aeiouAEIOU':
            count += 1
    return count
fruits_with_more_than_two_vowels = [f for f in fruits if count_vowels(f) > 2]

#  as for loop
fruits_with_more_than_two_vowels = []

def count_vowels(string):
    count = 0 
    for letter in string:
        if letter in 'aeiouAEIOU':
            count += 1
    return count

for fruit in fruits:
    if count_vowels(fruit) > 2:
        fruits_with_more_than_two_vowels.append(fruit)

print ('fruits_with_more_than_two_vowels:')
print (fruits_with_more_than_two_vowels)

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

# as list comprehension
fruits_with_only_two_vowels = [f for f in fruits if count_vowels(f) == 2]

#  as for loop
fruits_with_only_two_vowels = []
for fruit in fruits:
    if count_vowels(fruit) == 2:
        fruits_with_only_two_vowels.append(fruit) 

print ('fruits_with_only_two_vowels:')    
print (fruits_with_only_two_vowels)

# Exercise 5 - make a list that contains each fruit with more than 5 characters

# as list comprehension
def count_char(fruit):
    return len(fruit)

fruits_morethan5 = [f for f in fruits if count_char(f) > 5]

#  as for loop
fruits_morethan5 = []
for fruit in fruits:
    if len(fruit) > 5:
        fruits_morethan5.append(fruit)
print ('fruits with more than 5 chars:')
print(fruits_morethan5)

# Exercise 6 - make a list that contains each fruit with exactly 5 characters

# as list comprehension
fruits_exactly5 = [f for f in fruits if count_char(f) == 5]

#  as for loop
fruits_exactly5 = []

for fruit in fruits:
    if len(fruit) == 5:
        fruits_exactly5.append(fruit)
print ('fruits_exactly5:')
print(fruits_exactly5)

# Exercise 7 - Make a list that contains fruits that have less than 5 characters

# as list comprehension
fruits_lessthan5 = [f for f in fruits if count_char(f) < 5]

#  as for loop
fruits_lessthan5 = []

for fruit in fruits:
    if len(fruit) == 5:
        fruits_lessthan5.append(fruit)
print ('fruits_lessthan5:')
print(fruits_lessthan5)

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

# as list comprehension
fruit_characters = [len(fruit) for fruit in fruits]

#  as for loop
fruit_characters = []

for fruit in fruits:
    fruit_characters.append(len(fruit))

print ('fruit_characters: ')
print (fruit_characters)

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

# as list comprehension
fruits_with_letter_a = [f for f in fruits if 'a' in f]

#  as for loop
fruits_with_letter_a = []

for fruit in fruits:
    if fruit.find('a') != -1:
        fruits_with_letter_a.append(fruit)
print ('fruits_with_letter_a:')
print(fruits_with_letter_a)

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 

# as list comprehension
even_numbers = [n for n in numbers if n % 2 == 0]

#  as for loop
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print ('even_numbers: ')
print(even_numbers)

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers

# as list comprehension
odd_numbers = [n for n in numbers if n % 2 == 1]

#  as for loop
odd_numbers = []

for number in numbers:
    if number % 2 == 1:
        odd_numbers.append(number)

print ('odd_numbers: ')
print(odd_numbers)

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

# as list comprehension
positive_numbers = [n for n in numbers if n > 0]

#  as for loop
positive_numbers = []

for number in numbers:
    if number > 0:
        positive_numbers.append(number)

print ('positive_numbers: ')
print(positive_numbers)

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers

# as list comprehension
negative_numbers = [n for n in numbers if n < 0]

#  as for loop
negative_numbers = []

for number in numbers:
    if number < 0:
        negative_numbers.append(number)

print ('negative_numbers: ')
print(negative_numbers)

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
two_ormore_numerals = [n for n in numbers if len(str(abs((n)))) >= 2]

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
num_squared = [n * n for n in numbers]

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers = [n for n in numbers if n < 0 and n % 2 == 1]

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
numbers_plus_5 =[number + 5 for number in numbers]

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. 
# *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
