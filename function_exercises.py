# 1. Define a function named is_two. It should accept one input and 
# return True if the passed input is either the number or the string 2, False otherwise.

# is_two defines a single parameter and will return True or False
def is_two(x):
    # checks if input is a number or string 2 and returns true if the condition is met
    return x == '2' or x == 2

assert is_two(3) == False
assert is_two(2) == True
print("Exercise 1 is correct")


# 2. Define a function named is_vowel. It should return True if the passed string is a 
# vowel, False otherwise.

# is_vowel takes in a single letter as a parameter and will return True or False
def is_vowel(letter):
    letter = str(letter) # convert input to a string
    if letter.isalpha(): # check if the input is an alphabet
        return letter in 'aeiouAEIOU' # if the letter is an uppercase or lowercase vowel, return True
    return False

assert is_vowel('y') == False
assert is_vowel(52) == False
assert is_vowel('u') == True
assert is_vowel('52') == False
print("Exercise 2 is correct")


# 3. Define a function named is_consonant. It should return True if the passed
# string is a consonant, False otherwise. Use your is_vowel function to accomplish this

def is_consonant(letter): #function takes in a letter as input
    return not is_vowel(letter) # if the letter is not in the is_vowel function, the function will return True

assert is_consonant('2 chains') == False   
assert is_consonant('y') == True
assert is_consonant('i') == False
print("Exercise 3 is correct")


# 4. Define a function that accepts a string that is a word. The function 
# should capitalize the first letter of the word if the word starts with a consonant.

def capital_firstletter(word): # function takes in a word as a parameter
    first_letter = word[0] # initializes a variable for the first letter in the word, the letter on index = 0 in the word
    if is_consonant(first_letter): # this calls the is_consonant function to check if the first letter is a consonant
        return word.capitalize() # uppercases
    else:
        return word

capital_firstletter('amazing')
capital_firstletter('jump')
print("Exercise 4 is correct")


# 5. Define a function named calculate_tip. It should accept a tip percentage (a number 
# between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tip_percentage,bill): # function takes in 2 parameters: the tip % and the bill total
    amount_to_tip = tip_percentage * bill  # the formula to calculate amount to tip
    if tip_percentage > 0 and tip_percentage < 1 : # if the tip % entered is between 0 and 1
        return amount_to_tip
    else: # if the if condition is not met, the function will return the below statement
        return "Enter a tip percentage between 0 and 1" 

print (calculate_tip(15,50))
print (calculate_tip(0.15,50))
print (calculate_tip(0,50))
print("Exercise 5 is correct")

# 6. Define a function named apply_discount. It should accept a original price, 
# and a discount percentage, and return the price after the discount is applied.

def apply_discount(price, disc_percentage):# takes in 2 parameters
    if price and disc_percentage > 0 : # if both parameters are positive
        disc_to_apply = price * (disc_percentage/100) # formula to calculate the discount to apply
        price_after_disc = price - disc_to_apply # calculates price after discount
        return price_after_disc
    else:
        return 'Enter a price and discount percentage greater than 0' # if the input is not greater than 0, returns this 

apply_discount(1000,-30)
print("Exercise 6 is correct")

# 7. Define a function named handle_commas. It should accept a string that is a number 
# that contains commas in it as input, and return a number as output.

def handle_commas(num_with_commas): # function takes in a string that is a number with commas
    remove_commas = num_with_commas.replace(',','') # removes commas
    return int(remove_commas)

print(handle_commas('5,000'))
print("Exercise 7 is correct")

# 8. Define a function named get_letter_grade. 
# It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(num_grade):
    if num_grade < 0 or num_grade > 100: # if the input is not between 0 and 100, the elif statements wont run
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
    else: #if none of the above conditions are met, the grade returned will be F
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
    without_vowels_string = '' #initialize empty string to add characters to
    for char in string: 
        if char not in 'AEIOUaeiou': # if char is not a vowel concatenate it to without vowels string
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

def get_valid_string(string): # returns a string that has only alphabets, numbers, empty space or underscore
    return ''.join([c for c in string if c.isalnum() or c == ' ' or c == '_'])

def normalize_name(string): # uses the output string from function above and lowercases it, removes leading and trailing whitespace 
    #and replaces space with _
    valid_string = get_valid_string(string)
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
    output = [] #initialize empty list for output to append to
    for index in range (0, (len(list_of_numbers))): #provides range of index 0 to the length of the string
        new_value = 0
        if index == 0:
            new_value = list_of_numbers[index]  # if the list only contains one value, the sum is the value itself
        else: 
            new_value = list_of_numbers[index] + output[index-1] #index -1 adds the last number returned in the output
        output.append(new_value)
    return output
assert cumulative_sum([1,2,3]) == [1,3,6]