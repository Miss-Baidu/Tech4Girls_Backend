#!/usr/bin/python3
sentence = "Python is powerful and easy to learn."
print("Length of the string:", len(sentence))
print("First character:", sentence[0])
print("Last character:", sentence[-1])
start_index = sentence.index("powerful")
end_index = start_index + len("powerful")
print("Word 'powerful':", sentence[start_index:end_index])