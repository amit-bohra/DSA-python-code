from typing import List

def min_heapify(arr: List[int], n: int, i: int) -> None:
    """
    Converts the subtree rooted at index i into a min heap.
    """
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)

def build_min_heap(arr: List[int]) -> None:
    """
    Builds a min heap from the given list in O(n) time complexity.
    
    Trick to remember: Build the heap in linear time by starting from the last non-leaf node.
    """
    n = len(arr)
    start = n // 2 - 1
    for i in range(start, -1, -1):
        min_heapify(arr, n, i)

def heap_sort_ascending(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers in ascending order using a min heap in O(n) time complexity.
    
    Trick to remember: Use a min heap and repeatedly extract the minimum element.
    
    Example usage:
        input_arr = [3, 2, 1, 5, 4]
        sorted_arr = heap_sort_ascending(input_arr)
        print("Sorted array:", sorted_arr)  # Expected output: [1, 2, 3, 4, 5]
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Build a min heap from the input array
    build_min_heap(arr)

    # Extract minimum element from the heap repeatedly
    sorted_arr = []
    while arr:
        sorted_arr.append(arr[0])  # Append minimum element to the sorted array
        arr[0] = arr[-1]  # Move the last element to the root
        arr.pop()  # Remove the last element from the heap
        min_heapify(arr, len(arr), 0)  # Restore heap property
    return sorted_arr

# Testing the function
input_arr = [3, 2, 1, 5, 4]
sorted_arr = heap_sort_ascending(input_arr)
print("Sorted array:", sorted_arr)  # Expected output: [1, 2, 3, 4, 5]




def max_heapify(arr: List[int], n: int, i: int) -> None:
    """
    Converts the subtree rooted at index i into a max heap.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def build_max_heap(arr: List[int]) -> None:
    """
    Builds a max heap from the given list in O(n) time complexity.
    
    Trick to remember: Build the heap in linear time by starting from the last non-leaf node.
    """
    n = len(arr)
    start = n // 2 - 1
    for i in range(start, -1, -1):
        max_heapify(arr, n, i)

def heap_sort_descending(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers in descending order using a max heap in O(nlogn) time complexity.
    
    Trick to remember: Use a max heap and repeatedly extract the maximum element.
    
    Example usage:
        input_arr = [3, 2, 1, 5, 4]
        sorted_arr = heap_sort_descending(input_arr)
        print("Sorted array:", sorted_arr)  # Expected output: [5, 4, 3, 2, 1]
    
    Time Complexity: O(nlogn)
    Space Complexity: O(1)
    """
    # Build a max heap from the input array
    build_max_heap(arr)

    # Extract maximum element from the heap repeatedly
    sorted_arr = []
    while arr:
        sorted_arr.append(arr[0])  # Append maximum element to the sorted array
        arr[0] = arr[-1]  # Move the last element to the root
        arr.pop()  # Remove the last element from the heap
        max_heapify(arr, len(arr), 0)  # Restore heap property
    return sorted_arr

# Testing the function
input_arr = [3, 2, 1, 5, 4]
sorted_arr = heap_sort_descending(input_arr)
print("Sorted array:", sorted_arr)  # Expected output: [5, 4, 3, 2, 1]