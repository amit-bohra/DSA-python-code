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
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    # Function to extract the minimum element from the min-heap
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def extract_min(self) -> int:
        """
        Extracts the minimum element from the min-heap.

        Trick: Use the heapq.heappop function to extract the minimum element from the heap.

        Example Usage: Used to remove and return the minimum element from the min-heap.
        """
        if len(self.heap) == 0:
            raise IndexError("Cannot extract from an empty heap")
        min_value = self.heap[0]
        last_value = self.heap.pop()
        if self.heap:
            self.heap[0] = last_value
            self._bubble_down(0)
        return min_value

    # Function to get the minimum element from the min-heap without removing it
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_min(self) -> int:
        """
        Returns the minimum element from the min-heap without removing it.

        Trick: Access the first element of the heap, which is always the minimum element.

        Example Usage: Used to retrieve the minimum element from the min-heap without removing it.
        """
        if len(self.heap) == 0:
            raise IndexError("Cannot get minimum from an empty heap")
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

    # Function to perform the bubble-up operation
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def _bubble_up(self, index: int) -> None:
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    # Function to perform the bubble-down operation
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def _bubble_down(self, index: int) -> None:
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest_index = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest_index]:
                smallest_index = left_child_index
            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest_index]:
                smallest_index = right_child_index

            if smallest_index != index:
                self.heap[index], self.heap[smallest_index] = self.heap[smallest_index], self.heap[index]
                index = smallest_index
            else:
                break


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
        self.heap.append(-value)
        self._bubble_up(len(self.heap) - 1)

    # Function to extract the maximum element from the max-heap
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def extract_max(self) -> int:
        """
        Extracts the maximum element from the max-heap.

        Trick: Negate the extracted value to obtain the actual maximum element.

        Example Usage: Used to remove and return the maximum element from the max-heap.
        """
        if len(self.heap) == 0:
            raise IndexError("Cannot extract from an empty heap")
        max_value = -self.heap[0]
        last_value = self.heap.pop()
        if self.heap:
            self.heap[0] = last_value
            self._bubble_down(0)
        return max_value

    # Function to get the maximum element from the max-heap without removing it
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_max(self) -> int:
        """
        Returns the maximum element from the max-heap without removing it.

        Trick: Negate the first element of the heap to obtain the actual maximum element.

        Example Usage: Used to retrieve the maximum element from the max-heap without removing it.
        """
        if len(self.heap) == 0:
            raise IndexError("Cannot get maximum from an empty heap")
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

    # Function to perform the bubble-up operation
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def _bubble_up(self, index: int) -> None:
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    # Function to perform the bubble-down operation
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def _bubble_down(self, index: int) -> None:
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest_index = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest_index]:
                largest_index = left_child_index
            if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest_index]:
                largest_index = right_child_index

            if largest_index != index:
                self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
                index = largest_index
            else:
                break


# Example usage for MinHeap:
if __name__ == "__main__":
    # Create a new MinHeap instance
    min_heap: MinHeap = MinHeap()

    # Insert elements into the min-heap
    min_heap.insert(4)
    min_heap.insert(2)
    min_heap.insert(5)

    # Extract the minimum element from the min-heap
    print("Extracted Min Element:", min_heap.extract_min())  # Expected output: 2

    # Get the minimum element without removing it
    print("Min Element:", min_heap.get_min())  # Expected output: 4

    # Check if the min-heap is empty
    print("Is MinHeap Empty:", min_heap.is_empty())  # Expected output: False


# Example usage for MaxHeap:
if __name__ == "__main__":
    # Create a new MaxHeap instance
    max_heap: MaxHeap = MaxHeap()

    # Insert elements into the max-heap
    max_heap.insert(4)
    max_heap.insert(2)
    max_heap.insert(5)

    # Extract the maximum element from the max-heap
    print("Extracted Max Element:", max_heap.extract_max())  # Expected output: 5

    # Get the maximum element without removing it
    print("Max Element:", max_heap.get_max())  # Expected output: 4

    # Check if the max-heap is empty
    print("Is MaxHeap Empty:", max_heap.is_empty())  # Expected output: False
