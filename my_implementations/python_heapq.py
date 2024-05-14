import heapq

# Python heapq: Top 10 Functions (with Error Handling)

# Function 1: heappush()
# Description: Pushes an element onto the heap.
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Input Types: List, Any data type
# Return Type: None
# Explanation: Internally, heappush() pushes the element onto the heap maintaining the heap invariant.

# Example:
heap = []
heapq.heappush(heap, 4)
print(heap)  # Output: [4]

# Handling Error: No error raised

# Function 2: heappop()
# Description: Pops and returns the smallest element from the heap.
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Input Types: List
# Return Type: Any data type
# Explanation: Internally, heappop() removes and returns the smallest element from the heap maintaining the heap invariant.

# Example:
min_value = heapq.heappop(heap)
print(min_value)  # Output: 4

# Handling Error: If heap is empty
# empty_heap = []
# heapq.heappop(empty_heap)  # Raises IndexError: pop from an empty heap

# Function 3: heapify()
# Description: Converts a list into a heap in place.
# Time Complexity: O(n)
# Space Complexity: O(1)
# Input Types: List
# Return Type: None
# Explanation: Internally, heapify() converts the list into a heap by rearranging its elements.

# Example:
unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6]
heapq.heapify(unsorted_list)
print(unsorted_list)  # Output: [1, 1, 2, 6, 5, 9, 4, 3]

# Handling Error: No error raised

# Function 4: heappushpop()
# Description: Pushes an element onto the heap and pops the smallest element.
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Input Types: List, Any data type
# Return Type: Any data type
# Explanation: Internally, heappushpop() pushes the element onto the heap and returns the smallest element after popping.

# Example:
heap = [1, 3, 5, 7, 9]
result = heapq.heappushpop(heap, 2)
print(result)  # Output: 1
print(heap)  # Output: [2, 3, 5, 7, 9]

# Handling Error: No error raised

# Function 5: heapreplace()
# Description: Pops and returns the smallest element and pushes a new element.
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Input Types: List, Any data type
# Return Type: Any data type
# Explanation: Internally, heapreplace() pops the smallest element and pushes a new element onto the heap.

# Example:
heap = [1, 3, 5, 7, 9]
result = heapq.heapreplace(heap, 4)
print(result)  # Output: 1
print(heap)  # Output: [3, 4, 5, 7, 9]

# Handling Error: If heap is empty
# empty_heap = []
# heapq.heapreplace(empty_heap, 4)  # Raises IndexError: pop from an empty heap

# Function 6: nlargest()
# Description: Returns the n largest elements from the heap.
# Time Complexity: O(n log k)
# Space Complexity: O(k)
# Input Types: Integer, List
# Return Type: List
# Explanation: Internally, nlargest() returns the n largest elements from the heap using heap sort algorithm.

# Example:
heap = [1, 3, 5, 7, 9]
largest_elements = heapq.nlargest(3, heap)
print(largest_elements)  # Output: [9, 7, 5]

# Handling Error: No error raised

# Function 7: nsmallest()
# Description: Returns the n smallest elements from the heap.
# Time Complexity: O(n log k)
# Space Complexity: O(k)
# Input Types: Integer, List
# Return Type: List
# Explanation: Internally, nsmallest() returns the n smallest elements from the heap using heap sort algorithm.

# Example:
heap = [1, 3, 5, 7, 9]
smallest_elements = heapq.nsmallest(2, heap)
print(smallest_elements)  # Output: [1, 3]

# Handling Error: No error raised

# Function 8: merge()
# Description: Merges multiple sorted iterables into a single sorted iterable.
# Time Complexity: O(n log k)
# Space Complexity: O(k)
# Input Types: Iterable
# Return Type: Iterable
# Explanation: Internally, merge() merges multiple sorted iterables into a single sorted iterable using heap queue.

# Example:
iterable1 = [1, 3, 5]
iterable2 = [2, 4, 6]
merged_iterable = heapq.merge(iterable1, iterable2)
print(list(merged_iterable))  # Output: [1, 2, 3, 4, 5, 6]

# Handling Error: No error raised

# Function 9: _siftup()
# Description: Rebalances the heap by moving the element at the given index up the heap.
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Input Types: List, Integer
# Return Type: None
# Explanation: Internally, _siftup() rebalances the heap after insertion by moving the element up the heap.

# Example:
heap = [2, 4, 3, 7, 9, 6]
heapq._siftup(heap, 2)
print(heap)  # Output: [2, 4, 6, 7, 9, 3]

# Handling Error: No direct error handling as it's an internal function

# Function 10: _siftdown()
# Description: Rebalances the heap by moving the element at the given index down the heap.
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Input Types: List, Integer
# Return Type: None
# Explanation: Internally, _siftdown() rebalances the heap after extraction by moving the element down the heap.

# Example:
heap = [9, 7, 6, 2, 4, 3]
heapq._siftdown(heap, 0, len(heap) - 1)
print(heap)  # Output: [2, 4, 3, 9, 7, 6]

# Handling Error: No direct error handling as it's an internal function

