# 1. Import and test 3 of the functions from your functions exercise file. Import each function in a different way:

 
#import the module and use the . notation
import function_exercises
print(function_exercises.is_two(2))
print(function_exercises.is_two(4))

#use from to import the function directly
from function_exercises import is_vowel
print(is_vowel('x'))
print(is_vowel('e'))

#use from and give the function a different name
from function_exercises import capital_firstletter as capit
print(capit('hello'))


# 2. For this exercise, read about and use the itertools module from the standard library to help you solve the problem.

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

from itertools import product
print(list(product('ABC', [1,2,3])))
# 9 different combinations 
# [('A', 1), ('A', 2), ('A', 3), ('B', 1), ('B', 2), ('B', 3), ('C', 1), ('C', 2), ('C', 3)]

    
# How many different ways can you combine two of the letters from "abcd"?
from itertools import permutations
print(list(permutations(['ab', 'cd'])))
# 2 different ways
# [('ab', 'cd'), ('cd', 'ab')]

# 3. Save this file as profiles.json inside of your exercises directory. Use the load function from the json module to open this file, it will produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:

import json

with open('/Users/mariamnaqvi/codeup-data-science/python-exercises/profiles.json') as f:
    data = json.load(f)

    print(data[0])
# Total number of users  >>  19
total_users = len(data)
total_users

# Number of active users
active_count = 0
inactive_count = 0 
for user in data:
    if user["isActive"] == True:
        active_count += 1
    else:
        inactive_count += 1
print(f'number of active users: {active_count}')

# Number of inactive users
print(f'number of inactive users: {inactive_count}')

# Grand total of balances for all users
grand_total = 0
for user in data:
    user_balance = user["balance"]
    #remove the unnecessary characters - $ , and .
    sanitized_balance =  user_balance.replace("$","").replace(",","")
    grand_total += round(float(sanitized_balance),2)

print(f'grand total of all balances: {grand_total}')


# Average balance per user
#divide the total balance from the previous section,  by the length of the dict


# User with the lowest balance

# User with the highest balance

# Most common favorite fruit
favorite_fruits = []
most_common_fave_fruit = ""
for user in data:
    favorite_fruit = user["favoriteFruit"]
    favorite_fruits.append(favorite_fruit)
print(favorite_fruits)
most_common_fave_fruit = max(favorite_fruits)
print(f'most common favorite fruit: {most_common_fave_fruit}')


# Least most common favorite fruit
least_common_fave_fruit = min(favorite_fruits)
print(f'most common favorite fruit: {least_common_fave_fruit}')

# Total number of unread messages for all users
#look in the greetings key
total_unread = 0
for user in data:
    greeting_value = user["greeting"].split()

    #break the value into mini strings, 

    #loop through the array and get the numeric value
    for el in greeting_value:
        if el.isdigit():
            total_unread += int(el)
    #add it to the running total
print(total_unread)
    