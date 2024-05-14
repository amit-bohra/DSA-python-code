import heapq
from typing import List


class MinHeap:
    def __init__(self) -> None:
        self.heap: List[int] = []

    # Function to insert a new element into the min-heap
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def insert(self, value: int) -> None:
        """
        Inserts a new element into the min-heap.

        Trick: Use the heapq.heappush function to insert the value into the heap.

        Example Usage: Used to add a new element to the min-heap.
        """
        heapq.heappush(self.heap, value)

    # Function to extract the minimum element from the min-heap
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def extract_min(self) -> int:
        """
        Extracts the minimum element from the min-heap.

        Trick: Use the heapq.heappop function to extract the minimum element from the heap.

        Example Usage: Used to remove and return the minimum element from the min-heap.
        """
        return heapq.heappop(self.heap)

    # Function to get the minimum element from the min-heap without removing it
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_min(self) -> int:
        """
        Returns the minimum element from the min-heap without removing it.

        Trick: Access the first element of the heap, which is always the minimum element.

        Example Usage: Used to retrieve the minimum element from the min-heap without removing it.
        """
        return self.heap[0]

    # Function to check if the min-heap is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def is_empty(self) -> bool:
        """
        Checks if the min-heap is empty.

        Trick: Check if the heap list is empty.

        Example Usage: Used to determine if the min-heap is empty before performing extract operations.
        """
        return len(self.heap) == 0

    # Function to heapify the min-heap
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def heapify(self) -> None:
        """
        Converts the existing list into a valid min-heap.

        Trick: Use the heapq.heapify function to convert the list into a min-heap in-place.

        Example Usage: Used to convert an unsorted list into a valid min-heap.
        """
        heapq.heapify(self.heap)


class MaxHeap:
    def __init__(self) -> None:
        self.heap: List[int] = []

    # Function to insert a new element into the max-heap
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def insert(self, value: int) -> None:
        """
        Inserts a new element into the max-heap.

        Trick: Negate the value before inserting it into the heap to create a max-heap effect.

        Example Usage: Used to add a new element to the max-heap.
        """
        heapq.heappush(self.heap, -value)

    # Function to extract the maximum element from the max-heap
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def extract_max(self) -> int:
        """
        Extracts the maximum element from the max-heap.

        Trick: Negate the extracted value to obtain the actual maximum element.

        Example Usage: Used to remove and return the maximum element from the max-heap.
        """
        return -heapq.heappop(self.heap)

    # Function to get the maximum element from the max-heap without removing it
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_max(self) -> int:
        """
        Returns the maximum element from the max-heap without removing it.

        Trick: Negate the first element of the heap to obtain the actual maximum element.

        Example Usage: Used to retrieve the maximum element from the max-heap without removing it.
        """
        return -self.heap[0]

    # Function to check if the max-heap is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def is_empty(self) -> bool:
        """
        Checks if the max-heap is empty.

        Trick: Check if the heap list is empty.

        Example Usage: Used to determine if the max-heap is empty before performing extract operations.
        """
        return len(self.heap) == 0

    # Function to heapify the max-heap
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def heapify(self) -> None:
        """
        Converts the existing list into a valid max-heap.

        Trick: Negate all elements in the list and then use the heapq.heapify function to convert it into a max-heap in-place.

        Example Usage: Used to convert an unsorted list into a valid max-heap.
        """
        self.heap = [-x for x in self.heap]
        heapq.heapify(self.heap)


# Example usage:
if __name__ == "__main__":
    # Create a new min-heap and max-heap
    min_heap: MinHeap = MinHeap()
    max_heap: MaxHeap = MaxHeap()

    # Insert elements into the min-heap
    min_heap.insert(4)
    min_heap.insert(8)
    min_heap.insert(2)
    min_heap.insert(5)

    # Insert elements into the max-heap
    max_heap.insert(4)
    max_heap.insert(8)
    max_heap.insert(2)
    max_heap.insert(5)

    # Get the minimum element from the min-heap
    print("Minimum Element from Min-Heap:", min_heap.get_min())  # Expected output: 2

    # Extract the minimum element from the min-heap
    min_value = min_heap.extract_min()
    print("Extracted Minimum Element from Min-Heap:", min_value)  # Expected output: 2

    # Check if the min-heap is empty
    print("Is the min-heap empty?", min_heap.is_empty())  # Expected output: False

    # Get the maximum element from the max-heap
    print("Maximum Element from Max-Heap:", max_heap.get_max())  # Expected output: 8

    # Extract the maximum element from the max-heap
    max_value = max_heap.extract_max()
    print("Extracted Maximum Element from Max-Heap:", max_value)  # Expected output: 8

    # Check if the max-heap is empty
    print("Is the max-heap empty?", max_heap.is_empty())  # Expected output: False

    # Heapify the min-heap
    min_heap.heapify()
    print("Min-Heap after Heapify:", min_heap.heap)  # Expected output: [4, 5, 8]

    # Heapify the max-heap
    max_heap.heapify()
    print("Max-Heap after Heapify:", max_heap.heap)  # Expected output: [5, 4, 2]
