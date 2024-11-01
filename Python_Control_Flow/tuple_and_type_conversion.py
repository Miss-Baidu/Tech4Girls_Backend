#!/usr/bin/python3
my_tuple = ("Ama", 30, 2.89, "Apple", ['a', 'b', 'c'])
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
count_of_30 = my_tuple.count(30)
index_of_2_89 = my_tuple.index(2.89)

int_to_float = float(10)          
float_to_int = int(2.89)          
string_to_int = int("30")         

string_list = ["Hello,", "i'm", "Sarah"]
joined_string = " ".join(string_list)


print( count_of_30)
print("Index of 2.89 in tuple:", index_of_2_89)
print( int_to_float)
print( float_to_int)
print( string_to_int)
print( joined_string)


