from collections import OrderedDict, defaultdict

# Internal Implementation:

# OrderedDict:
# - Internally, OrderedDict maintains a doubly linked list to preserve the order of insertion.
# - Each entry in the dictionary has a reference to the previous and next entries, enabling efficient reordering.
# - This additional structure incurs higher memory overhead compared to a standard dictionary.

# defaultdict:
# - Internally, defaultdict is a subclass of dict that overrides the `__missing__()` method.
# - The `__missing__()` method is called when a key is not found in the dictionary.
# - It allows defaultdict to provide default values for missing keys based on a factory function specified during initialization.

# Differences:

# 1. Ordering:
# - Dictionary (dict): Does not maintain order of elements.
# - OrderedDict: Maintains order of elements based on insertion sequence.
# - defaultdict: Same as dict, does not maintain order of elements.

# 2. Default Values:
# - Dictionary (dict): Does not provide default values for missing keys.
# - OrderedDict: Does not provide default values for missing keys.
# - defaultdict: Provides default values for missing keys based on a factory function.

# 3. Memory Usage:
# - Dictionary (dict): Lower memory overhead compared to OrderedDict.
# - OrderedDict: Higher memory overhead due to additional storage for maintaining order.
# - defaultdict: Similar memory usage to dict.

# 4. Insertion Time Complexity:
# - Dictionary (dict), OrderedDict, defaultdict: O(1) for average case insertion.

# 5. Dependencies:
# - OrderedDict and defaultdict are subclasses of dict and are part of the collections module in Python.

# Similarities:

# 1. Key-Value Pair Storage:
# - All three data structures store key-value pairs.

# 2. Mutable:
# - They are all mutable and can be modified after creation.

# 3. Access Time Complexity:
# - They all have O(1) average time complexity for accessing elements by key.

# 4. Support for Key Operations:
# - They all support common dictionary operations like adding, updating, and deleting elements.

# 5. Compatibility:
# - They are all compatible with other Python data types and structures.

# Benefits and Disadvantages:

# Dictionary (dict):
# - Benefits: Low memory overhead, efficient for general-purpose key-value storage.
# - Disadvantages: Lack of order preservation, no default values for missing keys.

# OrderedDict:
# - Benefits: Preserves insertion order, suitable for scenarios requiring ordered storage.
# - Disadvantages: Higher memory usage compared to dict, no default values for missing keys.

# defaultdict:
# - Benefits: Provides default values for missing keys, useful for handling missing keys gracefully.
# - Disadvantages: Similar memory usage to dict, no order preservation.

# Use Cases:

# 1. Preserving Insertion Order (OrderedDict):
# - Use OrderedDict when preserving the order of insertion is important, such as maintaining a history of operations.

# Example:
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
print("OrderedDict:", ordered_dict)

# 2. Handling Default Values (defaultdict):
# - Use defaultdict when dealing with missing keys and providing default values is necessary, such as counting occurrences of elements.

# Example:
def_count = defaultdict(int)
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
for word in words:
    def_count[word] += 1
print("DefaultDict:", def_count)

# 3. General-Purpose Key-Value Storage (Dictionary):
# - Use dictionary for general key-value storage when order preservation and default values are not required.

# Example:
regular_dict = {'a': 1, 'b': 2, 'c': 3}
print("Dictionary:", regular_dict)
