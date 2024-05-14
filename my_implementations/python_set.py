# Python Set: Top 10 Functions (with Error Handling)

# Function 1: add()
# Description: Adds an element to the set.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Input Types: Any data type
# Return Type: None
# Explanation: Internally, add() inserts the element into the set if it does not already exist.

# Example:
example_set = {1, 2, 3}
example_set.add(4)
print(example_set)  # Output: {1, 2, 3, 4}

# Handling Error: No error raised

# Function 2: update()
# Description: Updates the set with elements from another set or iterable.
# Time Complexity: O(n)
# Space Complexity: O(n)
# Input Types: Set or Iterable
# Return Type: None
# Explanation: Internally, update() adds elements from the specified set or iterable to the existing set.

# Example:
example_set.update({5, 6})
print(example_set)  # Output: {1, 2, 3, 4, 5, 6}

# Handling Error: No error raised

# Function 3: remove()
# Description: Removes a specified element from the set.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Input Types: Any data type
# Return Type: None
# Explanation: Internally, remove() removes the specified element from the set if it exists; otherwise, it raises a KeyError.

# Example:
example_set.remove(3)
print(example_set)  # Output: {1, 2, 4, 5, 6}

# Handling Error: If element is not found
# example_set.remove(7)  # Raises KeyError: 7

# Function 4: discard()
# Description: Removes a specified element from the set if it exists.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Input Types: Any data type
# Return Type: None
# Explanation: Internally, discard() removes the specified element from the set if it exists; otherwise, it does nothing.

# Example:
example_set.discard(2)
print(example_set)  # Output: {1, 4, 5, 6}

# Handling Error: No error raised if element is not found

# Function 5: pop()
# Description: Removes and returns an arbitrary element from the set.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Input Types: None
# Return Type: Any data type
# Explanation: Internally, pop() removes and returns an arbitrary element from the set.

# Example:
popped_element = example_set.pop()
print(popped_element)  # Output: 1
print(example_set)  # Output: {4, 5, 6}

# Handling Error: If set is empty
# {}.pop()  # Raises KeyError: 'pop from an empty set'

# Function 6: clear()
# Description: Removes all elements from the set.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Input Types: None
# Return Type: None
# Explanation: Internally, clear() removes all elements from the set.

# Example:
example_set.clear()
print(example_set)  # Output: set()

# Handling Error: No error raised

# Function 7: union()
# Description: Returns a new set containing the union of two sets.
# Time Complexity: O(n)
# Space Complexity: O(n)
# Input Types: Set
# Return Type: Set
# Explanation: Internally, union() creates a new set containing all elements from both sets.

# Example:
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Handling Error: No error raised

# Function 8: intersection()
# Description: Returns a new set containing the intersection of two sets.
# Time Complexity: O(min(n, m))
# Space Complexity: O(min(n, m))
# Input Types: Set
# Return Type: Set
# Explanation: Internally, intersection() creates a new set containing elements that are common to both sets.

# Example:
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}

# Handling Error: No error raised

# Function 9: difference()
# Description: Returns a new set containing the difference between two sets.
# Time Complexity: O(n)
# Space Complexity: O(n)
# Input Types: Set
# Return Type: Set
# Explanation: Internally, difference() creates a new set containing elements that are present in the first set but not in the second set.

# Example:
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}

# Handling Error: No error raised

# Function 10: symmetric_difference()
# Description: Returns a new set containing the symmetric difference between two sets.
# Time Complexity: O(n)
# Space Complexity: O(n)
# Input Types: Set
# Return Type: Set
# Explanation: Internally, symmetric_difference() creates a new set containing elements that are present in either set but not in both sets.

# Example:
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}

# Handling Error: No error raised

