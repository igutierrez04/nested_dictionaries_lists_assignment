#Update values in dictionaries and lists
x = [[5,2,3], [10,8,9]] #TASK 1 change the value 10 in x to 15. Once you're done, x should now be [[5,2,3], [15,8,9]].
x[1][0] = 15

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
] #TASK 2 change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'

sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
} #TASK 3 In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'

z = [{'x': 10, 'y': 20}] #TASK 4 change the value 20 in z to 30
z[0]['y'] = 30

# Iterate through a list of dictionaries
# Create a function iterate_dictionary(some_list) that,
#given  list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value.

cars = [
    {'brand': 'Toyota', 'model': 'Supra MK5'},
    {'brand': 'Toyota', 'model': 'AE86'},
    {'brand': 'Nissa', 'model': 'Sylvia S15'},
    {'brand': 'Nissa', 'model': 'GTR'}
]

def itirate_dict(cars):
    for key, val in cars.items():
        print(key, " = ", val)

#test