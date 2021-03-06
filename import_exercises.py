# 1. Import and test 3 of the functions from your functions exercise file. Import each function in a different way:
# run an interactive ipython session
# type 'ipython' in terminal to start session

import function_exercises # make sure you are in the same directory so it can execute the script
function_exercises.is_vowel('a')
function_exercises.is_vowel('b')

#use from to import the function directly
from function_exercises import calculate_tip
print(calculate_tip(10,50))
print(calculate_tip(0.2,100))

#use from and give the function a different name
from function_exercises import capital_firstletter as capit
print(capit('hello'))

#---------------------------------------------------------------------------

# 2. For this exercise, read about and use the itertools module from the standard library to help you solve the problem.

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

#from the itertools module importing the product function
from itertools import product
list(itertools.product('ABC', '123'))
print(len(list(itertools.product('ABC', '123'))))
# 9 different combinations
# [('A', 1), ('A', 2), ('A', 3), ('B', 1), ('B', 2), ('B', 3), ('C', 1), ('C', 2), ('C', 3)]

    
# How many different ways can you combine two of the letters from "abcd?"
import itertools 

len(list(itertools.combinations('abcd',2))) # 6 different ways

len(list(itertools.permutations('abcd',2))) # ba is different from ab unlike combinations, 12 different combinations

# ---------------------------------------------------------------------------

# 3. Save this file as profiles.json inside of your exercises directory. Use the load function from the json module to open this file, it will produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:

import json

with open('/Users/mariamnaqvi/codeup-data-science/python-exercises/profiles.json') as f:
    data = json.load(f)

    print(data[0])
# Total number of users  >>  19
total_users = len(data)
print(f'Number of total users is: {total_users}')

# Number of active users >> 9
active_count = 0
inactive_count = 0 
for user in data:
    if user["isActive"] == True:
        active_count += 1
    else:
        inactive_count += 1
print(f'number of active users: {active_count}')
#using lc
active_accounts = [accnt for accnt in profiles if accnt['isActive']]

# ---------------------------------------------------------------------------

# Number of inactive users >> 10
print(f'number of inactive users: {inactive_count}')
#using lc
for accnt in data:
    if not accnt['isActive']:
        inactive_count.append(accnt)

# ---------------------------------------------------------------------------

# Grand total of balances for all users
grand_total = 0
for user in data:
    user_balance = user["balance"]
    #remove the unnecessary characters - $ , and .
    sanitized_balance =  user_balance.replace("$","").replace(",","")
    grand_total += round(float(sanitized_balance),2)

print(f'grand total of all balances: {grand_total}')

# ---------------------------------------------------------------------------

# Average balance per user
#divide the total balance from the previous section, by the length of the dict
avg_balance = round(grand_total / len(data), 3)
print(avg_balance)

# ---------------------------------------------------------------------------

# User with the lowest balance

balances_list = []
lowest_bal_user = []
highest_bal_user = []
for user in data:
    
    name = user['name']
    user_balance = user["balance"]
    sanitized_balance =  user_balance.replace("$","").replace(",","")
    balances_list.append(sanitized_balance)
    lowest_bal = min(balances_list)
    highest_bal = max(balances_list)
    user_index = user['index']
    if user_index == 6:
        lowest_bal_user.append(name)
    elif user_index == 3:
        highest_bal_user.append(name)
        
print(highest_bal_user)       
print(lowest_bal_user)
# to find indexes for lowest and highest balances
print(list(enumerate(balances_list)))

    # User with the highest balance
print(highest_bal_user)

# ---------------------------------------------------------------------------

# Most common favorite fruit
favorite_fruits = []
most_common_fave_fruit = ""
for user in data:
    favorite_fruit = user["favoriteFruit"]
    favorite_fruits.append(favorite_fruit)
print(favorite_fruits)
most_common_fave_fruit = max(favorite_fruits)
print(f'most common favorite fruit: {most_common_fave_fruit}')
#using lc
fruit_list = [accnt['favoriteFruit'] for accnt in profiles]

# ---------------------------------------------------------------------------

# Least most common favorite fruit
least_common_fave_fruit = min(favorite_fruits)
print(f'most common favorite fruit: {least_common_fave_fruit}')

# ---------------------------------------------------------------------------

# Total number of unread messages for all users >> 210
#look in the greetings key
total_unread = 0
for user in data:
    greeting_value = user["greeting"].split()
    #break the value into mini strings

    #loop through the array and get the numeric value
    for el in greeting_value:
        if el.isdigit():
            total_unread += int(el)
    #add it to the running total
print(total_unread)

#  ---------------------------------------------------------------------------
   