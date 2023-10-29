# 1. Update values in dictionaries and lists
x = [[5,2,3], [10,8,9]] #TASK 1 change the value 10 in x to 15. Once you're done, x should now be [[5,2,3], [15,8,9]].
x[1][0] = 15
print(x)

students = [ #TASK 2 change the last_name of the first student from 'Jordan' to 'Bryant'
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
] 
students[0]['last_name'] = 'Bryant'
print(students[0])

sports_directory = { #TASK 3 In the sports_directory, change 'Messi' to 'Andres'
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z = [{'x': 10, 'y': 20}] #TASK 4 change the value 20 in z to 30
z[0]['y'] = 30
print(z)

# 2. Iterate through a list of dictionaries
# Create a function iterate_dictionary(some_list) that,
#given  list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value.

cars = [
    {'make': 'Toyota', 'model': 'Supra MK5'},
    {'make': 'Toyota', 'model': 'AE86'},
    {'make': 'Nissa', 'model': 'Sylvia S15'},
    {'make': 'Nissa', 'model': 'GTR'}
]

def itirate_dict(lst):
    for i in lst:
        print('Make -', i['make'],'-', 'Model -', i['model'] )

itirate_dict(cars)

# 3. Get values from a list of dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionries
# and a key name, the function prints the value stored in that key for each dictionary.
# For example, iterateDictionary2('first_name', students) should output: the students first name

def itirate_dict2(lst):
    for i in lst:
        print(i['make'])

itirate_dict2(cars)


# 4. itirate through a dictionary with list values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(info):
    for key, val in info.items():
        print("------------")
        print(f"{len(val)} {key}")
        for i in range(0, len(val)):
            print(val[i])


print_info(dojo)