import array
import numpy as np

# Differences:

# 1. Mutability:
# - Python list: Mutable (can be modified after creation).
# - Tuple: Immutable (cannot be modified after creation).
'''
Once a tuple is created you cannot set, append, insert, remove, pop, clear, sort, reverse it.
'''
# - Array (Python `array` module): Mutable, but elements must be of the same data type.
# - Numpy array: Mutable (can be modified after creation), optimized for numerical computations.

# 2. Memory Efficiency:
# - Python list: Less memory efficient due to dynamic resizing and heterogeneous elements.
# - Tuple: More memory efficient than lists due to immutability.
# - Array (Python `array` module): Memory efficient when elements are of the same data type.
# - Numpy array: Memory efficient, especially for large datasets, due to contiguous memory allocation.

# 3. Data Types:
# - Python list: Can store elements of different data types.
# - Tuple: Can store elements of different data types.
# - Array (Python `array` module): Elements must be of the same data type.
# - Numpy array: Elements must be of the same data type, typically used for numerical data.

# 4. Performance:
# - Python list: Slower performance compared to arrays and numpy arrays, especially for numerical computations.
# - Tuple: Similar performance to lists due to similar implementation.
# - Array (Python `array` module): Faster performance compared to lists, but slower than numpy arrays for numerical computations.
# - Numpy array: Faster performance, optimized for numerical computations using vectorized operations.

# 5. Functionality:
# - Python list: Versatile with built-in methods for various operations.
# - Tuple: Limited functionality compared to lists due to immutability.
# - Array (Python `array` module): Limited functionality compared to numpy arrays.
# - Numpy array: Rich functionality for numerical computations including element-wise operations, linear algebra, and statistical functions.

# 6. Creation Syntax:
# - Python list: Created using square brackets `[ ]`.
# - Tuple: Created using parentheses `( )`.
# - Array (Python `array` module): Created using `array()` function from the array module.
# - Numpy array: Created using `numpy.array()` function.

# 7. Size Flexibility:
# - Python list: Dynamically resizable, can grow or shrink as needed.
# - Tuple: Fixed size, cannot be resized after creation.
# - Array (Python `array` module): Can be resized, but requires creating a new array.
# - Numpy array: Dynamically resizable, can grow or shrink efficiently.

# 8. Indexing and Slicing:
# - Python list: Supports indexing and slicing with square brackets `[ ]`.
# - Tuple: Supports indexing and slicing similar to lists.
# - Array (Python `array` module): Supports indexing and slicing similar to lists.
# - Numpy array: Supports advanced indexing and slicing for multi-dimensional arrays.

# 9. Support for Mathematical Operations:
# - Python list: Limited support for mathematical operations, often requires looping.
# - Tuple: Limited support for mathematical operations, similar to lists.
# - Array (Python `array` module): Limited support for mathematical operations, similar to lists.
# - Numpy array: Extensive support for mathematical operations, optimized for numerical computations.

# 10. Dependencies:
# - Python list: No additional dependencies.
# - Tuple: No additional dependencies.
# - Array (Python `array` module): No additional dependencies.
# - Numpy array: Requires the NumPy library to be installed.

# Similarities:

# 1. Iterable:
# - All four data structures are iterable, meaning you can iterate over their elements using loops or comprehension.

# 2. Indexing:
# - They all support indexing to access individual elements by their position.

# 3. Slicing:
# - All four data structures support slicing to extract subsequences of elements.

# 4. Homogeneous and Heterogeneous Elements:
# - Python list, tuple, and array (Python `array` module) can store both homogeneous and heterogeneous elements.
# - Numpy array is typically used for homogeneous elements.

# 5. Data Storage:
# - They all store data elements, making them suitable for storing collections of items.

# 6. Data Organization:
# - They all organize data in a linear sequence, making them suitable for ordered collections.

# 7. Memory Allocation:
# - They all allocate memory dynamically to accommodate the storage of elements.

# 8. Iterable Methods:
# - Python list, tuple, and array (Python `array` module) provide built-in methods for various iterable operations like `len()`, `max()`, `min()`, `sum()`, etc.

# 9. Compatibility with Python Data Types:
# - They all seamlessly integrate with other Python data types and structures.

# 10. Support for Iteration Protocols:
# - They all support iteration protocols like iteration, membership testing, etc., making them compatible with various Python constructs.

# Benefits and Disadvantages:

# Python List:
# - Benefits: Versatility, dynamic resizing, compatibility.
# - Disadvantages: Lower performance for numerical computations, higher memory usage for heterogeneous elements.

# Tuple:
# - Benefits: Immutability ensures data integrity, memory efficiency.
# - Disadvantages: Limited functionality, fixed size.

# Array (Python array module):
# - Benefits: Memory efficiency for homogeneous elements, faster performance compared to lists.
# - Disadvantages: Limited functionality compared to numpy arrays, requires elements to be of the same data type.

# Numpy Array:
# - Benefits: High-performance numerical computations, extensive functionality, memory efficiency.
# - Disadvantages: Requires NumPy library, may have a learning curve for users unfamiliar with numerical computing.

# Use Cases:

# 1. Efficient Numerical Computations (Numpy Array)
# Numpy Arrays are best suited for efficient numerical computations.

# Example: Calculating element-wise multiplication of two arrays.
numpy_array1 = np.array([1, 2, 3])
numpy_array2 = np.array([4, 5, 6])
elementwise_product = numpy_array1 * numpy_array2
print("Element-wise product using Numpy Array:", elementwise_product)

# 2. Fixed Configuration (Tuple)
# Tuples are best suited when a fixed configuration is required, such as defining coordinates.

# Example: Defining coordinates of a point.
point_coordinates = (3, 4)
print("Coordinates of the point:", point_coordinates)

# 3. Byte-level Data Representation (Array)
# Arrays (from the Python array module) are best suited for byte-level data representation.

# Example: Storing binary data.
binary_data = array.array('B', [0, 1, 0, 1, 1, 0, 1, 0])
print("Binary data using Array:", binary_data)

# 4. Dynamic Storage and Heterogeneous Elements (Python List)
# Python Lists are best suited for dynamic storage and handling heterogeneous elements.

# Example: Storing a mix of different data types.
mixed_data = [1, "hello", 3.5, True]
print("Mixed data using Python List:", mixed_data)
