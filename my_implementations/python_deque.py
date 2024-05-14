from collections import deque

# Python deque: Top 15 Functions (with Error Handling)

# Function 1: append()
# Description: Adds an element to the right end of the deque.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Input Types: Any data type
# Return Type: None
# Explanation: Internally, append() inserts the element at the end of the deque.

# Example:
example_deque = deque([1, 2, 3])
example_deque.append(4)
print(example_deque)  # Output: deque([1, 2, 3, 4])

# Handling Error: No error raised

# Function 2: appendleft()
# Description: Adds an element to the left end of the deque.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Input Types: Any data type
# Return Type: None
# Explanation: Internally, appendleft() inserts the element at the beginning of the deque.

# Example:
example_deque.appendleft(0)
print(example_deque)  # Output: deque([0, 1, 2, 3, 4])

# Handling Error: No error raised

# Function 3: pop()
# Description: Removes and returns the rightmost element from the deque.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Input Types: None
# Return Type: Any data type
# Explanation: Internally, pop() removes and returns the element at the end of the deque.

# Example:
popped_element = example_deque.pop()
print(popped_element)  # Output: 4
print(example_deque)  # Output: deque([0, 1, 2, 3])

# Handling Error: If deque is empty
# empty_deque = deque([])
# empty_deque.pop()  # Raises IndexError: pop from an empty deque

# Function 4: popleft()
# Description: Removes and returns the leftmost element from the deque.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Input Types: None
# Return Type: Any data type
# Explanation: Internally, popleft() removes and returns the element at the beginning of the deque.

# Example:
popped_left = example_deque.popleft()
print(popped_left)  # Output: 0
print(example_deque)  # Output: deque([1, 2, 3])

# Handling Error: If deque is empty
# empty_deque = deque([])
# empty_deque.popleft()  # Raises IndexError: pop from an empty deque

# Function 5: extend()
# Description: Extends the deque by appending elements from an iterable to the right end.
# Time Complexity: O(k)
# Space Complexity: O(k)
# Input Types: Iterable
# Return Type: None
# Explanation: Internally, extend() adds elements from the iterable to the end of the deque.

# Example:
example_deque.extend([4, 5, 6])
print(example_deque)  # Output: deque([1, 2, 3, 4, 5, 6])

# Handling Error: No error raised

# Function 6: extendleft()
# Description: Extends the deque by appending elements from an iterable to the left end.
# Time Complexity: O(k)
# Space Complexity: O(k)
# Input Types: Iterable
# Return Type: None
# Explanation: Internally, extendleft() adds elements from the iterable to the beginning of the deque in reverse order.

# Example:
example_deque.extendleft([-1, 0])
print(example_deque)  # Output: deque([0, -1, 1, 2, 3, 4, 5, 6])

# Handling Error: No error raised

# Function 7: rotate()
# Description: Rotates the deque n steps to the right (positive n) or left (negative n).
# Time Complexity: O(k)
# Space Complexity: O(1)
# Input Types: Integer
# Return Type: None
# Explanation: Internally, rotate() shifts the elements of the deque by n steps to the right or left.

# Example:
example_deque.rotate(2)
print(example_deque)  # Output: deque([5, 6, 0, -1, 1, 2, 3, 4])

# Handling Error: No error raised

# Function 8: reverse()
# Description: Reverses the elements of the deque in place.
# Time Complexity: O(n)
# Space Complexity: O(1)
# Input Types: None
# Return Type: None
# Explanation: Internally, reverse() reverses the order of elements in the deque.

# Example:
example_deque.reverse()
print(example_deque)  # Output: deque([4, 3, 2, 1, -1, 0, 6, 5])

# Handling Error: No error raised

# Function 9: count()
# Description: Returns the number of occurrences of a value in the deque.
# Time Complexity: O(n)
# Space Complexity: O(1)
# Input Types: Any data type
# Return Type: Integer
# Explanation: Internally, count() counts the occurrences of the specified value in the deque.

# Example:
count_of_2 = example_deque.count(2)
print(count_of_2)  # Output: 1

# Handling Error: No error raised

# Function 10: clear()
# Description: Removes all elements from the deque.
# Time Complexity: O(n)
# Space Complexity: O(1)
# Input Types: None
# Return Type: None
# Explanation: Internally, clear() removes all elements from the deque.

# Example:
example_deque.clear()
print(example_deque)  # Output: deque([])

# Handling Error: No error raised

# Function 11: copy()
# Description: Returns a shallow copy of the deque.
# Time Complexity: O(n)
# Space Complexity: O(n)
# Input Types: None
# Return Type: deque
# Explanation: Internally, copy() creates a new deque with the same elements as the original deque.

# Example:
example_deque = deque([1, 2, 3])
copy_deque = example_deque.copy()
print(copy_deque)  # Output: deque([1, 2, 3])

# Handling Error: No error raised

# Function 12: maxlen attribute
# Description: Returns the maximum size of the deque.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Input Types: None
# Return Type: Integer or None
# Explanation: Internally, maxlen attribute specifies the maximum number of elements that the deque can hold. If not specified, it returns None.

# Example:
print(example_deque.maxlen)  # Output: None

# Handling Error: No error raised

# Function 13: insert()
# Description: Inserts an element at a specified position.
# Time Complexity: O(n)
# Space Complexity: O(1)
# Input Types: Integer, Any data type
# Return Type: None
# Explanation: Internally, insert() inserts the element at the specified index position in the deque.

# Example:
example_deque.insert(1, 0)
print(example_deque)  # Output: deque([1, 0, 2, 3])

# Handling Error: If index is out of range
# example_deque.insert(10, 5)  # Raises IndexError: deque index out of range

# Function 14: index()
# Description: Returns the index of the first occurrence of a value.
# Time Complexity: O(n)
# Space Complexity: O(1)
# Input Types: Any data type
# Return Type: Integer
# Explanation: Internally, index() returns the index of the first occurrence of the specified value in the deque.

# Example:
index_of_2 = example_deque.index(2)
print(index_of_2)  # Output: 2

# Handling Error: If value is not found
# example_deque.index(5)  # Raises ValueError: deque.index(x): x not in deque

# Function 15: remove()
# Description: Removes the first occurrence of a value from the deque.
# Time Complexity: O(n)
# Space Complexity: O(1)
# Input Types: Any data type
# Return Type: None
# Explanation: Internally, remove() removes the first occurrence of the specified value from the deque.

# Example:
example_deque.remove(2)
print(example_deque)  # Output: deque([1, 0, 3])

# Handling Error: If value is not found
# example_deque.remove(5)  # Raises ValueError: deque.remove(x): x not in deque

