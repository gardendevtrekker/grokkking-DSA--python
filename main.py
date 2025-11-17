"""
Data Structures and Algorithms Practice Repository
This is a practice repository for learning DSA with Python
"""
from ch1.binary_search import binary_search

def main():
    print("Hello and welcome to the learning Data Structures and Algorithms with Pythons!")

    my_list = [1, 3, 5, 7, 9]

    print(binary_search(my_list, 3)) # => 1
    print(binary_search(my_list, -1)) # => None

if __name__ == "__main__":
    main()
