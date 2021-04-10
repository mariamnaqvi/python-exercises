students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]
# 1. How many students are there?

print(f'There are {len(students)} students')

# -------------------------------------------------------------

# 2. How many students prefer light coffee? For each type of coffee roast?

# find the different types of coffee preferences in the list

coffee_roasts = []
for student in students:
    coffee_pref = student['coffee_preference']
    if coffee_pref not in coffee_roasts:
        coffee_roasts.append(coffee_pref)
print(coffee_roasts)

# to find how many students like each type of coffee roast

count_dark = 0
count_medium = 0
count_light = 0
for student in students:
    coffee_pref = student['coffee_preference']
    if coffee_pref == "light":
        count_light += 1
    elif coffee_pref == "medium":
        count_medium += 1
    elif coffee_pref == "dark":
        count_dark += 1
print(f'{count_light} students prefer light coffee')
print(f'{count_medium} students prefer medium coffee')
print(f'{count_dark} students prefer dark coffee')

# --------------------------------------------------------------

# 3. How many types of each pet are there?

# find how many different types of pets

pet_types = []
for student in students:
    pets = student['pets']
    for pet in pets:
        pet_type = pet['species']
        if pet_type not in pet_types:
            pet_types.append(pet_type)
print(pet_types)

#   to find count of each type of pet

count_horse = 0
count_cat = 0
count_dog = 0
for student in students:
    pets = student['pets']
    for pet in pets:
        pet_type = pet['species']
        if pet_type == 'horse':
            count_horse += 1 
        elif pet_type == 'cat':
            count_cat += 1
        elif pet_type == 'dog':
            count_dog += 1
print(f'There are {count_horse} horses')
print(f'There are {count_cat} cats')
print(f'There are {count_dog} dogs')

# --------------------------------------------------------------

# 4. How many grades does each student have? Do they all have the same number of grades?

count_grade = []

for student in students:
    grade = student['grades']
    num_grades = len(grade)
    count_grade.append(num_grades)  
print(count_grade)

# checking if all students have the same grades

for num_grade in count_grade:
    if num_grade != count_grade[0]:
        print ('grade is different')
print ('All students have the same number of grades')

# --------------------------------------------------------------

# 5. What is each student's grade average?

average_grades_of_all_students = []
for student in students:
    grades = student['grades']
    total = 0 
    for grade in grades:
        total += grade
    average_grade = total / len(grades)
    average_grades_of_all_students.append(average_grade)
print (average_grades_of_all_students)

# 6. How many pets does each student have?

count_of_pets = []
for student in students:
    pets = student['pets']
    num_pets = len(pets)
    count_of_pets.append(num_pets)
print(count_of_pets)

# --------------------------------------------------------------

# 7. How many students are in web development? data science?

count_WD_students = 0
count_DS_students = 0
for student in students:
    course = student['course']
    if course == 'web development':
        count_WD_students += 1
    else:
        count_DS_students += 1
print (count_WD_students)
print (count_DS_students)

# --------------------------------------------------------------

# 8. What is the average number of pets for students in web development?

count_WD_students = 0
count_of_pets = 0
for student in students:
    course = student['course']
    pets = len(student['pets'])
    if course == 'web development':
        count_WD_students += 1
        count_of_pets += pets
        
avg_pets_WD = round(count_of_pets/count_WD_students,3)

print (f'There are {count_WD_students} students in WD') 
print (f'There are {count_of_pets} pets for students in WD')
print (f'{avg_pets_WD} is the average number of pets for students in WD')

# --------------------------------------------------------------

# 9. What is the average pet age for students in data science?

total_age = 0
total_num_pets = 0

for student in students:
    pets = student['pets']
    course = student['course']
    if course == 'data science':
        for pet in pets:
            age = pet['age']
            total_age += age
            total_num_pets += 1
avg_pet_age = total_age/total_num_pets
print(avg_pet_age)

# --------------------------------------------------------------

# 10. What is most frequent coffee preference for data science students?

count_light = 0
count_medium = 0
count_dark = 0

for student in students:
    coffee_pref = student['coffee_preference']
    if coffee_pref == 'light':
        count_light += 1
    elif coffee_pref == 'medium':
        count_medium += 1
    elif coffee_pref == 'dark':
        count_dark += 1

coffee_counts = {"light":count_light, "medium":count_medium, "dark":count_dark}
sorted_coffee_counts = sorted(coffee_counts.items(),key = lambda kv: kv[1])
last_el = sorted_coffee_counts[-1]
print(f'{last_el[0].title()} is the most frequent coffee preference')

# --------------------------------------------------------------

# 11. What is the least frequent coffee preference for web development students?

count_light = 0
count_dark = 0
count_medium = 0

for student in students:
    coffee_pref = student['coffee_preference']
    course = student['course']
    if course == 'web development':
        if coffee_pref == 'light':
            count_light += 1
        elif coffee_pref == 'medium':
            count_medium += 1
        elif coffee_pref == 'dark':
            count_dark += 1
print(count_medium)
print(count_light)
print(count_dark)
coffee_counts = {"light":count_light, "medium":count_medium, "dark":count_dark}
sorted_coffee_counts = sorted(coffee_counts.items(),key = lambda kv: kv[1])
print(sorted_coffee_counts)
# print the first lowest preference since there are 2 of the same counts
first_el = sorted_coffee_counts[0]
print(f'{first_el[0].title()} is the least frequent coffee preference among WD students')

# --------------------------------------------------------------

# 12. What is the average grade for students with at least 2 pets?

count_grades = 0
total_grade = 0
for student in students:
    grades = student['grades']
    num_pets = len(student['pets'])
    if num_pets >= 2:
        for grade in grades:
            total_grade += grade
            count_grades += 1
avg_grade = total_grade / count_grades
print(avg_grade)

# --------------------------------------------------------------

# 13. How many students have 3 pets?

num_students = 0
for student in students:
    pet = student['pets']
    num_pets = len(pet)
    if len(pet) == 3:
        num_students += 1
print(num_students)

# --------------------------------------------------------------

# 14. What is the average grade for students with 0 pets?

total_grade = 0
count_grades = 0
for student in students:
    grades = student['grades']
    num_pets = len(student['pets'])
    for grade in grades:
        if num_pets == 0:
            total_grade += grade
            count_grades += 1
avg_grade = round(total_grade/count_grades, 2)
print(avg_grade)

# --------------------------------------------------------------

# 15. What is the average grade for web development students? data science students?

# 16. What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
# 17. What is the average number of pets for medium coffee drinkers?
# 18. What is the most common type of pet for web development students?
# 19. What is the average name length?
# 20. What is the highest pet age for light coffee drinkers?