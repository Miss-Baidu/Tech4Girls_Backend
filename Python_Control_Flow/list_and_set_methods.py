#!/usr/bin/python3
list_Names = ['Akua', 'Yaa', 'Adjoa', 'Ama', 'Afia']
print(list_Names)
list_Names.append('Esi')
print(list_Names)
list_Names.remove('Yaa')
print(list_Names)
popped_value = list_Names.pop()
print("Popped value:", popped_value)
print(list_Names)
list_Names.sort()
print(list_Names)
list_Names.reverse()
print(list_Names)
list_Names.extend(['Aba','Naa'])
print(list_Names)

#SET METHOD
set_Fruits = {'Apple','Grape', 'Carrot', 'Pear', 'Cherry'}
set_Veggies = {'Carrot', 'Cabbage', 'Lettuce', 'Pepper', 'Onion' }
print(set_Fruits)
print(set_Veggies)
set_Fruits.add('Mango')
print(set_Fruits)
set_Veggies.remove('Pepper')
print(set_Veggies)
union_set = set_Fruits.union(set_Veggies)
print(union_set)
intersection_set = set_Fruits.intersection(set_Veggies)
print(intersection_set)
difference_set_Fruits_Veggies = set_Fruits.difference(set_Veggies)
difference_set_Veggies_Fruits = set_Veggies.difference(set_Fruits)
print(difference_set_Fruits_Veggies)
print(difference_set_Veggies_Fruits)