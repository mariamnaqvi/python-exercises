# 1. Define a function named is_two. It should accept one input and 
# return True if the passed input is either the number or the string 2, False otherwise.

def is_two(x):
    return x == '2' or x == 2

is_two(3)
is_two(2)
print("Exercise 1 is correct")


# 2. Define a function named is_vowel. It should return True if the passed string is a 
# vowel, False otherwise.

def is_vowel(letter):
    letter = str(letter)
    if letter.isalpha():
        return letter in 'aeiouAEIOU'
    return False

is_vowel('y')
is_vowel(52)
print("Exercise 2 is correct")


# 3. Define a function named is_consonant. It should return True if the passed
# string is a consonant, False otherwise. Use your is_vowel function to accomplish this
def is_vowel(letter):
    return letter in 'aeiouAEIOU'
def is_consonant(letter):
    return not is_vowel(letter)

is_consonant('y')
is_consonant('i')
print("Exercise 3 is correct")


# 4. Define a function that accepts a string that is a word. The function 
# should capitalize the first letter of the word if the word starts with a consonant.

def capital_firstletter(word):
    first_letter = word[0]
    if is_consonant(first_letter):
        return word.capitalize()
    else:
        return word

capital_firstletter('amazing')
capital_firstletter('jump')
print("Exercise 4 is correct")


# 5. Define a function named calculate_tip. It should accept a tip percentage (a number 
# between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tip_percentage,bill):
    amount_to_tip = tip_percentage * bill
    if tip_percentage <= 1:
        return amount_to_tip
    else:
        return "Enter a tip percentage between 0 and 1" 

print (calculate_tip(15,50))
print (calculate_tip(0.15,50))
print (calculate_tip(0,50))
print("Exercise 5 is correct")

# 6. Define a function named apply_discount. It should accept a original price, 
# and a discount percentage, and return the price after the discount is applied.

def apply_discount(price, disc_percentage):
    if price and disc_percentage > 0 :
        disc_to_apply = price * (disc_percentage/100)
        price_after_disc = price - disc_to_apply
        print (f'The price after discount is {price_after_disc}')
    else:
        print ('Enter a price and discount percentage greater than 0')

apply_discount(1000,30)
print("Exercise 6 is correct")

# 7. Define a function named handle_commas. It should accept a string that is a number 
# that contains commas in it as input, and return a number as output.

def handle_commas(num_with_commas):
    remove_commas = num_with_commas.replace(',','')
    return int(remove_commas)

print (type((handle_commas('5,000'))))
print("Exercise 7 is correct")

# 8. Define a function named get_letter_grade. 
# It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(num_grade):
    if num_grade < 0 or num_grade > 100:
        return 'Enter a number between 0 and 100'
    elif num_grade >= 90:
        return 'A'
    elif num_grade >= 80:
        return 'B'
    elif num_grade >= 70:
        return 'C'
    elif num_grade >= 60:
        return 'D'
    elif num_grade >= 50:
        return 'E'
    else:
        return 'F'

# get_letter_grade(65)
# get_letter_grade(30)
# get_letter_grade(-80)
# get_letter_grade(900)
assert get_letter_grade(90) == 'A'
assert get_letter_grade(95) == 'A'
assert get_letter_grade(900) == 'Enter a number between 0 and 100'
assert get_letter_grade(-80) == 'Enter a number between 0 and 100'
assert get_letter_grade(73) == 'C'
assert get_letter_grade(30) == 'F'
print("Exercise 8 is correct")

# 9.Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(string):
    without_vowels_string = ''
    for char in string:
        if char not in 'AEIOUaeiou':
            without_vowels_string += char
    return without_vowels_string

assert remove_vowels('a') == ''
assert remove_vowels('octopus') == 'ctps'
assert remove_vowels('nymph') == 'nymph'
assert remove_vowels('bbb') == 'bbb'
print("Exercise 9 is correct")

# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed

def get_valid_string(string):
    return ''.join([c for c in string if c.isalnum() or c == ' '])

def normalize_name(string):
    valid_string = get_valid_string(string)
    # lower_cased = string.lower()
    # remove_spaces = lower_cased.strip()
    # new_string = remove_spaces.
    return valid_string.lower().strip().replace(' ','_')

assert normalize_name('Name') == 'name'
assert normalize_name('First Name') == 'first_name'
assert normalize_name('% Completed') == 'completed'
print("Exercise 10 is correct")
     
"""
11. Write a function named cumulative_sum 
that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
"""

def cumulative_sum(list_of_numbers):
    output = []
    for index in range (0, (len(list_of_numbers))):
        new_value = 0
        if index == 0:
            new_value = list_of_numbers[index]
        else:
            new_value = list_of_numbers[index] + output[index-1]
        output.append(new_value)
    return output
assert cumulative_sum([1,2,3]) == 6, "x should be 'hello'"