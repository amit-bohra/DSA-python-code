from typing import List

def binary_search(arr: List[int], target: int) -> int:
    """
    Performs binary search on a sorted list of integers.
    
    Assumptions:
    - The input list 'arr' is sorted in non-decreasing order.
    - Returns the index of the target element if found, otherwise returns -1.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            left = mid + 1
            
        else:
            right = mid - 1
    
    return -1

# Testing the function
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 13
index = binary_search(arr, target)
if index != -1:
    print(f"Target {target} found at index {index}.")
else:
    print(f"Target {target} not found in the array.")








    from typing import List

def binary_search_2d(matrix: List[List[int]], target: int) -> bool:
    """
    Performs binary search on a sorted 2D matrix of integers.
    
    Assumptions:
    - The input 2D matrix 'matrix' is sorted in non-decreasing order row-wise and column-wise.
    - Returns True if the target element is found, otherwise returns False.
    
    Time Complexity: O(log n + log m), where n is the number of rows and m is the number of columns
    Space Complexity: O(1)
    """
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1  # Start from the top-right corner
    
    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1  # Move down if the current element is smaller than the target
        else:
            col -= 1  # Move left if the current element is larger than the target
    
    return False

# Testing the function
matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17],
]

target = 9
if binary_search_2d(matrix, target):
    print(f"Target {target} found in the matrix.")
else:
    print(f"Target {target} not found in the matrix.")
