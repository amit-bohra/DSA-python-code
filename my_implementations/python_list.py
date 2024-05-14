# Python Dictionary: Top 10 Functions (with Error Handling)

# Function 1: get()
# Description: Returns the value associated with the specified key.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Input Types: Any data type (key), Any data type (default value, optional)
# Return Type: Any data type
# Explanation: Internally, get() computes the hash value of the specified key to efficiently retrieve the corresponding value from the dictionary. If the key is not found, it returns the default value (if provided) or None.

# Example:
example_dict = {'a': 1, 'b': 2, 'c': 3}
value_of_a = example_dict.get('a')
print(value_of_a)  # Output: 1

# Handling Error: If key is not found
value_of_x = example_dict.get('x')
print(value_of_x)  # Output: None

# Function 2: setdefault()
# Description: Returns the value associated with the specified key. If the key is not found, inserts the key with the specified value.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Input Types: Any data type (key), Any data type (default value, optional)
# Return Type: Any data type
# Explanation: Internally, setdefault() checks if the specified key exists in the dictionary. If it does, it returns the corresponding value. If not, it inserts the key with the specified default value and returns the default value.

# Example:
example_dict = {'a': 1, 'b': 2, 'c': 3}
value_of_d = example_dict.setdefault('d', 4)
print(example_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Handling Error: If key is not found
value_of_x = example_dict.setdefault('x', 5)
print(example_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'x': 5}

# Function 3: keys()
# Description: Returns a view of all keys in the dictionary.
# Time Complexity: O(1)
# Space Complexity: O(n)
# Input Types: None
# Return Type: dict_keys
# Explanation: Internally, keys() returns a view object that provides a dynamic view of the keys in the dictionary. This view object does not create a new list of keys, but rather provides a dynamic view of the existing keys.

# Example:
example_dict = {'a': 1, 'b': 2, 'c': 3}
keys_view = example_dict.keys()
print(keys_view)  # Output: dict_keys(['a', 'b', 'c'])

# Function 4: values()
# Description: Returns a view of all values in the dictionary.
# Time Complexity: O(1)
# Space Complexity: O(n)
# Input Types: None
# Return Type: dict_values
# Explanation: Internally, values() returns a view object that provides a dynamic view of the values in the dictionary. Similar to keys(), this view object does not create a new list of values but provides a dynamic view of the existing values.

# Example:
example_dict = {'a': 1, 'b': 2, 'c': 3}
values_view = example_dict.values()
print(values_view)  # Output: dict_values([1, 2, 3])

# Function 5: items()
# Description: Returns a view of all key-value pairs in the dictionary.
# Time Complexity: O(1)
# Space Complexity: O(n)
# Input Types: None
# Return Type: dict_items
# Explanation: Internally, items() returns a view object that provides a dynamic view of the key-value pairs in the dictionary. Similar to keys() and values(), this view object does not create new lists but provides a dynamic view of the existing key-value pairs.

# Example:
example_dict = {'a': 1, 'b': 2, 'c': 3}
items_view = example_dict.items()
print(items_view)  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# Function 6: pop()
# Description: Removes and returns the value associated with the specified key.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Input Types: Any data type (key)
# Return Type: Any data type
# Explanation: Internally, pop() computes the hash value of the specified key to efficiently locate and remove the corresponding key-value pair from the dictionary. If the key is not found, it raises a KeyError.

# Example:
example_dict = {'a': 1, 'b': 2, 'c': 3}
value_of_b = example_dict.pop('b')
print(value_of_b)  # Output: 2
print(example_dict)  # Output: {'a': 1, 'c': 3}

# Handling Error: If key is not found
# example_dict.pop('x')  # Raises KeyError: 'x'

# Function 7: popitem()
# Description: Removes and returns a key-value pair from the dictionary.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Input Types: None
# Return Type: Tuple (key, value)
# Explanation: Internally, popitem() removes and returns an arbitrary key-value pair from the dictionary. As dictionaries are unordered, there is no guarantee which key-value pair will be removed.

# Example:
example_dict = {'a': 1, 'b': 2, 'c': 3}
key_value_pair = example_dict.popitem()
print(key_value_pair)  # Output: ('c', 3)
print(example_dict)  # Output: {'a': 1, 'b': 2}

# Handling Error: If dictionary is empty
# {}.popitem()  # Raises KeyError: 'popitem(): dictionary is empty'

# Function 8: update()
# Description: Updates the dictionary with the key-value pairs from another dictionary or an iterable of key-value pairs.
# Time Complexity: O(n)
# Space Complexity: O(n)
# Input Types: Dictionary or Iterable (of key-value pairs)
# Return Type: None
# Explanation: Internally, update() iterates through the key-value pairs of the provided dictionary or iterable and adds or updates the corresponding key-value pairs in the dictionary.

# Example:
example_dict = {'a': 1, 'b': 2}
example_dict.update({'b': 3, 'c': 4})
print(example_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Function 9: clear()
# Description: Removes all key-value pairs from the dictionary.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Input Types: None
# Return Type: None
# Explanation: Internally, clear() deallocates the memory occupied by the key-value pairs in the dictionary, effectively removing all key-value pairs.

# Example:
example_dict = {'a': 1, 'b': 2, 'c': 3}
example_dict.clear()
print(example_dict)  # Output: {}

# Function 10: fromkeys()
# Description: Creates a new dictionary with the specified keys and optional default value.
# Time Complexity: O(n)
# Space Complexity: O(n)
# Input Types: Iterable (of keys), Any data type (default value, optional)
# Return Type: Dictionary
# Explanation: Internally, fromkeys() iterates through the specified keys and adds them to the new dictionary with the optional default value (if provided).

# Example:
keys = ['a', 'b', 'c']
default_value = 0
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}
