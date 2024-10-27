#!/usr/bin/python3
#TUPLES
#Methods
# number_tuple = (1, 5, 3, 8)
# print(len(number_tuple))

# index = number_tuple.index(5)
# print(index)

# count = number_tuple.count(5)
# print(count)

#SETS
# my_students = {'Grace', 'Noami', 'Emefa', 'Priscilla', 'Jennifer'}
# my_other_students = {'Grace', 'Beatrice', 'Noami', 'Rhoda', 'Manuella', 'Emefa'}
# print(my_other_students & my_students) #intersection
# print(my_other_students | my_students) #union
# print(my_other_students - my_students) #difference

# numbers = [1, 5, 3, 8, 8, 5]

# unique_numbers = set(numbers) 
# print(unique_numbers)

# new_list = list(unique_numbers)
# new_list.sort()

# print(new_list)
 
# How to create an empty list, tuples, and sets.
# var = list(vars)
# var = set(var)
# var = tuple(var)

# var = [] #empty list
# var = () # empty tuple

# Courses = ['Maths', 'Science', 'English','Social' ]
# MyCourses = set(Courses)
# print(MyCourses)

# Tuple_MyCourses = tuple(MyCourses)
# print(Tuple_MyCourses)

# To add
#my_set = ('James', 'Rhoda','Irene', 'Jedidah', 'Khadijah')
#my_set.add('Nana', 'Akua')

# To remove
# my_set = ('James', 'Rhoda','Irene', 'Jedidah', 'Khadijah')
# my_set.reomve('Jedidah')

# To clear
# my_set.clear

# to remove the last item
# my_set.pop()

#print(dir(set))

#print(help(str.lower))
#print(help(set.intersection)) press Q to exit 

#Dictionaries
#my_student = {'name' :'Rhoda', 'age' :21, 'program' : 'Tech4Girls'}
#print(my_student['name'])
#print(my_student['age'])
#print(my_student['program'])

#another way to use the key method is, returns an error as none
#print(my_student.get('name'))

#adding a new key to a dictionary
#my_student['coursemate'] = 'Noami'
#print(my_student['coursemate'])

#Over writing an existing key
# my_student['name'] = 'Sara'
# print(my_student.get('name'))

# print(my_student.keys())
# print(my_student.values())

# del my_student['program']
# print(my_student)

# my_student.pop('coursemate')
# print(my_student)

# #update
# my_student.update({'name':'Rhoda', 'age':21, 'program':'ALX', 'Coursemate': 'Noami'})
# print(my_student)


#control flow
#synthax
"""
if condition: 
    statement
else:
    statement
elif condition
    statement

my_string = 'Control flow lost '

if my_string == 'Hello Control flow':
    print ('control flow in python is easy')
elif my_string == 'Control flow lost':
    print('yes')
else: 
    print('All good')
"""
# my_set = {1, 3, 6, 8}
# if 4 | 6 in my_set:
#     print('Inclusive')
# else:
#     print('Exclusive')

# Assign a variable called number and number=7. if the number id divisble by 2 then is even and if is  not divisble by 2 else the number is odd

# if Number  % 2 == 1:
#      print('The Number is even')
# else:
#      print('The Number is odd')