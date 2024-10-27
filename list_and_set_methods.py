#!/usr/bin/python3
# Demonstrating the said methods 

Name_list = ['Ama', 'Akua', 'Adjoa', 'Afia', 'Yaa']
print(Name_list)
Name_list.append("Adjoa")
print("Adjoa:", Name_list)
Name_list.remove("Yaa")
print ("Yaa", Name_list )
popped_name = Name_list.pop()
print(popped_name)
print(Name_list)
Name_list.sort()  
print("Sorted Name_list:", Name_list)
Name_list.reverse()
print(Name_list)
Name_list.extend(['Esi', 'Abena'])
print(Name_list)

my_Fruits = {'Apple', 'Orange', 'Carrot', 'Grapes','Pear'}
my_Vegetables = {'Onion', 'Pepper', 'Carrot', 'Lettuce', 'Cabbage'}
print(my_Fruits)
print(my_Vegetables)
my_Fruits.add('Mango')
print(my_Fruits)
my_Vegetables.remove('Cabbage')
print(my_Vegetables)
union = my_Vegetables.union(my_Fruits)
print(union)
intersection = my_Fruits.intersection(my_Vegetables)
print(intersection)
difference = my_Fruits.difference(my_Vegetables)
print(difference)




