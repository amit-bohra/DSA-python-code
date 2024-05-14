# Python Tuple: Top 10 Functions (with Error Handling)


'''
Once a tuple is created you cannot set, append, insert, remove, pop, clear, sort, reverse it.
'''

# Function 1: index()
# Description: Returns the index of the first occurrence of a value in the tuple.
# Time Complexity: O(n)
# Space Complexity: O(1)
# Input Types: Any data type
# Return Type: Integer
# Explanation: Internally, index() iterates through the elements of the tuple to find the first occurrence of the specified value.

# Example:
example_tuple = (1, 2, 3, 4, 2)
index_of_3 = example_tuple.index(3)
print(index_of_3)  # Output: 2

# Handling Error: If value is not found
# example_tuple.index(10)  # Raises ValueError: tuple.index(x): x not in tuple

# Function 2: count()
# Description: Returns the number of occurrences of a value in the tuple.
# Time Complexity: O(n)
# Space Complexity: O(1)
# Input Types: Any data type
# Return Type: Integer
# Explanation: Internally, count() iterates through the elements of the tuple and counts the occurrences of the specified value.

# Example:
count_of_2 = example_tuple.count(2)
print(count_of_2)  # Output: 2

# Handling Error: If value is not found
# count_of_10 = example_tuple.count(10)  # Returns 0

# Function 3: slicing
# Description: Extracts a subset of elements from the tuple using slicing notation.
# Time Complexity: O(k)
# Space Complexity: O(k)
# Input Types: Integer (optional)
# Return Type: Tuple
# Explanation: Slicing creates a new tuple containing elements from the original tuple within the specified range.

# Example:
subset_tuple = example_tuple[1:4]
print(subset_tuple)  # Output: (2, 3, 4)

# Handling Error: If index is out of range
# out_of_range_slice = example_tuple[10:20]  # Returns an empty tuple ()

# Function 4: concatenation
# Description: Concatenates two tuples to create a new tuple.
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
# Input Types: Tuple
# Return Type: Tuple
# Explanation: Concatenation creates a new tuple by combining elements from both tuples.

# Example:
another_tuple = (5, 6)
concatenated_tuple = example_tuple + another_tuple
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 2, 5, 6)

# Handling Error: No error raised

# Function 5: unpacking
# Description: Unpacks a tuple into individual elements.
# Time Complexity: O(1)
# Space Complexity: O(n)
# Input Types: None
# Return Type: Individual elements
# Explanation: Unpacking assigns each element of the tuple to separate variables.

# Example:
a, b, c, *rest = example_tuple
print(a, b, c)  # Output: 1 2 3

# Handling Error: If number of variables does not match the length of the tuple
# a, b = example_tuple  # Raises ValueError: too many values to unpack

# Function 6: min()
# Description: Returns the minimum value from the tuple.
# Time Complexity: O(n)
# Space Complexity: O(1)
# Input Types: None
# Return Type: Any data type
# Explanation: Internally, min() iterates through the elements of the tuple to find the minimum value.

# Example:
min_value = min(example_tuple)
print(min_value)  # Output: 1

# Handling Error: If tuple is empty
# min_value_empty = min(())  # Raises ValueError: min() arg is an empty sequence

# Function 7: max()
# Description: Returns the maximum value from the tuple.
# Time Complexity: O(n)
# Space Complexity: O(1)
# Input Types: None
# Return Type: Any data type
# Explanation: Internally, max() iterates through the elements of the tuple to find the maximum value.

# Example:
max_value = max(example_tuple)
print(max_value)  # Output: 4

# Handling Error: If tuple is empty
# max_value_empty = max(())  # Raises ValueError: max() arg is an empty sequence

# Function 8: sorted()
# Description: Returns a new sorted list from the elements of the tuple.
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Input Types: None
# Return Type: List
# Explanation: sorted() creates a new sorted list from the elements of the tuple using an optimized sorting algorithm.

# Example:
sorted_list = sorted(example_tuple)
print(sorted_list)  # Output: [1, 2, 2, 3, 4]

# Handling Error: No error raised

# Function 9: len()
# Description: Returns the number of elements in the tuple.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Input Types: None
# Return Type: Integer
# Explanation: Internally, len() returns the length of the tuple.

# Example:
length_of_tuple = len(example_tuple)
print(length_of_tuple)  # Output: 5

# Handling Error: No error raised

# Function 10: membership test
# Description: Checks if a value exists in the tuple.
# Time Complexity: O(n)
# Space Complexity: O(1)
# Input Types: Any data type
# Return Type: Boolean
# Explanation: Internally, membership test iterates through the elements of the tuple to check for the presence of the specified value.

# Example:
is_present = 2 in example_tuple
print(is_present)  # Output: True

# Handling Error: No error raised

