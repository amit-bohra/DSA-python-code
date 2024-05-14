import heapq
from typing import List

# Heap Sort for a list
def heap_sort(arr: List[int]) -> List[int]:
    """
    Performs heap sort on a list of integers using heapq.
    
    Trick to remember: Use heapq to heapify the array.
    
    Question: Sort a list of integers in non-decreasing order.
    
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    heapq.heapify(arr)
    sorted_arr = []
    while arr:
        sorted_arr.append(heapq.heappop(arr))
    return sorted_arr

# Testing the function
input_arr = [3, 2, 1, 5, 4]
print("Sorted list:", heap_sort(input_arr))  # Expected output: [1, 2, 3, 4, 5]
