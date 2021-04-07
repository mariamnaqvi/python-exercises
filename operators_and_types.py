# Identify the data type of the following values:

# 99.9 - float
print(type(99.9))

# "False" - string
print(type("False"))

# False - boolean
print(type(False))

# '0' -string
print(type('0'))

# 0 -integer
print(type(0))

# True - boolean
print(type(True))

# 'True' - string
print(type('True'))

# [{}] - list
print(type([{}]))

# {'a': []} - dictionary
print(type({'a': []}))

# What data type would best represent:

# A term or phrase typed into a search box? (str)
# If a user is logged in? (bool)
# A discount amount to apply to a user's shopping cart? (float)
# Whether or not a coupon code is valid? (bool)
# An email address typed into a registration form? (list or dict)
# The price of a product? (float)
# A Matrix? (list of lists)
# The email addresses collected from a registration form? (str)
# Information about applicants to Codeup's data science program? (str)

# For each of the following code blocks, read the expression 
# and predict what the result of evaluating it would be, then execute the expression in your Python REPL. 

'1' + 2
# 3
# returns TypeError: can only concatenate str (not "int") to str

6 % 4
# remainder of 6 divided by 4
# returns 2

type(6 % 4)
# int
# returns int

type(type(6 % 4))
# type
# returns <class 'type'>

'3 + 4 is ' + 3 + 4
# error
# returns TypeError: can only concatenate str (not "int") to str

0 < 0
# false
# returns False

'False' == False
# False >> single quotes reads as a string literal while without strings it is a boolean
# returns False

True == 'True'
# false
# returns False

5 >= -5
# true
# returns True

True or "42"
# true
# returns True >>> if you compare true or anything else, you end up with true if at least one of them is true

'42' or True
# returns '42' because 42 exists

6 % 5
# 1 >> remainder of 6 divided by 5
# returns 1

5 < 4 and 1 == 1
#False
# returns false

'codeup' == 'codeup' and 'codeup' == 'Codeup'
# returns False

4 >= 0 and 1 !== '1'
# error
# returns SyntaxError: invalid syntax

6 % 3 == 0
# true
# returns true

5 % 2 != 0
# true
# returns true

[1] + 2
# error
# returns TypeError: can only concatenate list (not "int") to list

[1] + [2]
# 3
# returns [1, 2]

[1] * 2
# returns [1, 1]

[1] * [2]
# returns TypeError: can't multiply sequence by non-int of type 'list'

[] + [] == []
# returns true

{} + {}
# error
# TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
