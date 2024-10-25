#!/usr/bin/python3

def demonstrate_string_methods(): 
    example = "Hello, I am a Scholar of T4G!"
    upper_example = example.upper()
    print("Uppercase:", upper_example)
    lower_example = example.lower()
    print("Lowercase:", lower_example)
    replaced_example = example.replace("Scholar", "student")
    print("Replaced String:", replaced_example)
    words = ["Hello", "am a", "T4G Scholar"]
    joined_example = " ".join(words)
    print("Joined String:", joined_example)
if __name__ == "__main__":
    demonstrate_string_methods()
