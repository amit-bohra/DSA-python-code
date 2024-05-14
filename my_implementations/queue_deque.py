from collections import deque

class Queue:
    def __init__(self) -> None:
        self.queue: deque = deque()

    # Function to enqueue an element into the queue
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def enqueue(self, item: any) -> None:
        """
        Enqueues an element into the queue.
        
        Trick: Append the item to the right end of the deque.

        Example Usage: Used in breadth-first search (BFS) algorithms.
        """
        self.queue.append(item)

    # Function to dequeue an element from the queue
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def dequeue(self) -> any:
        """
        Dequeues and returns the front element from the queue.
        
        Trick: Pop the leftmost item from the deque.

        Example Usage: Used in scheduling tasks in real-time systems.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.popleft()

    # Function to check if the queue is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.
        
        Trick: Check if the length of the deque is zero.

        Example Usage: Used to handle base cases in algorithms involving queues.
        """
        return len(self.queue) == 0

    # Function to peek the front element of the queue without removing it
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def peek(self) -> any:
        """
        Returns the front element of the queue without removing it.
        
        Trick: Access the leftmost item of the deque.

        Example Usage: Used in algorithms that require looking at the front element without dequeuing it.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[0]

    # Function to get the size of the queue
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def size(self) -> int:
        """
        Returns the size of the queue.
        
        Trick: Get the length of the deque.

        Example Usage: Used to monitor the size of the queue during algorithm execution.
        """
        return len(self.queue)


# Example usage:
if __name__ == "__main__":
    # Create a new queue
    queue: Queue = Queue()

    # Enqueue elements into the queue
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    # Peek the front element
    print("Peek:", queue.peek())  # Expected output: 1

    # Dequeue elements from the queue
    print("Dequeue:", queue.dequeue())  # Expected output: 1
    print("Dequeue:", queue.dequeue())  # Expected output: 2

    # Check if the queue is empty
    print("Is empty:", queue.is_empty())  # Expected output: False

    # Dequeue the remaining element
    print("Dequeue:", queue.dequeue())  # Expected output: 3

    # Check if the queue is empty after dequeuing all elements
    print("Is empty:", queue.is_empty())  # Expected output: True
