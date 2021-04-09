

make_and_model = ['toyota','tacoma']

truck = 'toyota tacoma'
print(truck)


make_and_model = truck.split()
print(make_and_model)


make = make_and_model[0]
print(make)


model = make_and_model[1]
print(model)



truck = dict(make = make_and_model[0],model = make_and_model[1])
print(truck)



truck['make'] = truck['make'].title()
print(truck)

truck['model'] = truck['model'].title()
truck



truck['make'] = truck['make'].upper()
truck





truck['model'] = truck['model'].upper()
truck




truck






