# Write the code that operates on a single string containing the make and model of a vehicle. 
# The first part of the string before the space is the make. The last part of the string after the space is the model.
# We can assume that the strings will only have one space. 
# Assume the input string is completely lower-cased.

# Exercise #1
# Write the code to take a string and produce a dictionary out of that 
# string such that the output looks like the following:

# Input truck = "toyota tacoma"
# Output

# truck = {
#     "make": "toyota",
#     "model": "tacoma"
# }

truck = 'toyota tacoma'
print(truck)

# create a list with make and model of the truck
make_and_model = truck.split()
print(make_and_model)

# to get the first index of the list
make = make_and_model[0]
print(make)

# to get the second index of the list 
model = make_and_model[1]
print(model)

# to create the dictionary 
truck = dict(make = make_and_model[0],model = make_and_model[1])
print(truck)

# or do this 
print('Here is the dictionary')
truck = {
    "make": make_and_model[0],
    "model": make_and_model[1]
}
truck

# Exercise #2
# Write the code that takes a dictionary containing make/model for a vehicle 
# and capitalizes the first character of the make and the model

print('Here is the dictionary with the first letters capitalized')
truck['make'] = truck['make'].title()
truck['model'] = truck['model'].title()
truck

# Create a list of 3 dictionaries where each dictionary represents
# a vehicle, as above. Write the code that operates on that list of 
# dictionaries in order to uppercase the entire make and model values.

print('Here is the list of 3 dictionaries')

vehicles = [
    {
        "make": "Toyota",
        "model": "Tacoma"
    },
    {
        "make": "Honda",
        "model": "Accord"
    },
    {
        "make": "Nissan",
        "model": "Altima"
    }
]
vehicles


for vehicle in vehicles:
    vehicle['make'] = vehicle['make'].upper()
    vehicle['model'] = vehicle["model"].upper()
print(vehicles)











