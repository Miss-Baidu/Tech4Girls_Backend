# For loops in Python
#items = [2, 4, 6, 8, 10, ]

#Names = ['Afia', 'Ama', 'Yaa', 'Nana']
#my_tuple = tuple(Names)
#print(my_tuple)
#for Name in Names:
 #   print(Name)




#Synthax
#for item in items:
#  if item == 8:
#       print('Skipped 8')
#        continue
#     print(item)

#for item in range(1,11):
#    print(item)


#Break statement stops a loop when a condition is met 
#Continue skips to the next value in the list   
#Enested loop(loop within a loop)

#for item in items:  #outer loop
 #   for letter in 'abc':   #inner loop
  #      print(item, letter)

#looking into dictionary
#my_dict = {'name': 'Sara', 'age':20, 'work':'student', 'energy_level': 70 }
#for key, value in my_dict.items():
 #  print(key, value)
#for value in my_dict.values():
 #   print(value)
#for key in my_dict.keys():
    #print(key)

#Fizz buzz challange
#Sudo code : first look through a range of numbers from 1 to 50
#for i in range (1, 51):
#if number is divisible by both 3 and 5, print fizzbuzz
    #if (i % 3 == 0 and i % 5 == 0):
     #   print('FizzBuzz')
# if number is /3 and returns 0, print fizz
    #elif(i % 3 == 0):
     #   print('Fizz')
#if number is /5 and returns 0, print buzz
    #elif (i % 5 == 0):
     #   print ('Buzz')
#else print the number
    #else:
        #print(i)

#TRY QUESTIONS

#Create a dictionary called students with keys name, age and city and corresponding values. use a for loop to print each key value pair in a format key:value.
#Students = {'Name': 'Sara', 'Age': 20, 'City': 'Accra' }
#for key, value in Students.items():
    #print(f"{key}: {value}")

#Create a list called Grades cony 85,72,90,68,80. use the for loop to print the grades above 80. 
#Grades = [85, 72, 90, 68, 80]

# print out only grades above 80
#print("Grades above 80:")
#for Grade in Grades:
    #if Grade > 80:
        #print(Grade) 


#calcuate and print out the average of all the grades
#Average = sum(Grades)/ len(Grades)
#print("Average of all grades:", Average)

#Exercise : Create a list of tuples called products comtaining product names and prices:
#Products = [("Apple", 1.29), ("Banana", 0.59), ("Orange", 0.79)]
#Use a for loop to unlock each tuple and print "Product: [name] - Price: [price]".
#for product, price in Products:
 #   print(f"Product: {product} - Price: {price}")

