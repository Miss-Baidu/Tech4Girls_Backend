#!/usr/bin/python3
 # Name = " Sarah's Laptop "
 # print(Name)
 # print(Name.replace("Laptop","phone"))
 # Name.find("Laptop")
 # Name[0:1]

 #1 create a list called number containing the numbers (1,5,3,8).Append the number 10 to the end of the list.Insert the number 2 at index 1. Remove the number 3 from the list.Print the final list.
 #Numbers = [1, 5, 3, 8]
# Numbers.append(10)
# Numbers.insert(1, 2)
# Numbers.remove(3)
# print(Numbers)
# #2 Create a list called colors containg (red, green, blue, purple) sort the list alphabetically.Reverse the sorted list.Print the final list
# Colours = ['Yellow''Red', 'Green', 'Blue', 'Purple']
# Colours.sort()
# Colours.reverse()
# print(Colours)

#3 Create a list called temperat containing (25, 18, 32, 20, 28). find the minimun temp ,maximum print both values
# Temparature = [25, 18, 32, 20, 28]
# min_temp = min(Temparature)
# max_temp = max(Temparature)
# print(min_temp)
# print(max_temp)
# #4 Create a list called scores containing (85, 72, 90, 68, 80) calculate the total sum of the scores. Print the total sum
# Scores = [85, 72, 90, 68, 80]
# totalsum = sum(Scores)
# print(totalsum)
# #5 CREATE A LIST CALLED ANIMALS CONTAINING (Cat, Dog Bird Fish)Remove the element at index 2. Replace the element at index 1 with lizard.
# Animals = ['Cat', 'Dog', 'Bird', 'Fish']
# Animals.remove('Bird')
# Animals.insert(1,'Lizard')
# popped = Animals.pop()
# print(popped)
# print(Animals)
# #6 Create two list, list1(1 2 3) and list2(4 5 6) and comibine list two into list 1
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.extend(list2)
# print(list1)


# #create a name called names containing (alice bob charlie and david) find the index of bob and then print it out
# Name = [ 'Alice', 'Bob', 'Charlie', 'David' ]
# Name.index('Bob')
# print(Name.index('Bob'))

#TUPLES
#Methods
number_tuple = (1, 5, 3, 8)
print(len(number_tuple))

index = number_tuple.index(5)
print(index)

count = number_tuple.count(5)
print(count)

