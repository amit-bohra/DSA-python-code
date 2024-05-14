from typing import Any, List

class QueueUsingStacks:
    def __init__(self) -> None:
        self.stack1: List[Any] = []  # For enqueue operation
        self.stack2: List[Any] = []  # For dequeue operation

    # Function to enqueue an element into the queue
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def enqueue(self, item: Any) -> None:
        """
        Enqueues an element into the queue.

        Trick: Push the element onto stack1.

        Example Usage: Used in BFS (breadth-first search) algorithms for traversing graphs.
        """
        self.stack1.append(item)

    # Function to dequeue an element from the queue
    # Time Complexity: O(n) amortized
    # Space Complexity: O(1)
    def dequeue(self) -> Any:
        """
        Dequeues and returns the front element from the queue.

        Trick: If stack2 is empty, transfer all elements from stack1 to stack2.
               Then pop from stack2.

        Example Usage: Used in scheduling tasks in operating systems.
        """
        if not self.stack2:
            if not self.stack1:
                raise IndexError("Queue is empty")
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    # Function to check if the queue is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.

        Trick: Check if both stack1 and stack2 are empty.

        Example Usage: Used in algorithms to handle base cases when processing elements in a queue.
        """
        return not self.stack1 and not self.stack2

    # Function to peek the front element of the queue without removing it
    # Time Complexity: O(n) amortized
    # Space Complexity: O(1)
    def peek(self) -> Any:
        """
        Returns the front element of the queue without removing it.

        Trick: If stack2 is empty, transfer all elements from stack1 to stack2.
               Then peek the top element of stack2.

        Example Usage: Used in algorithms to inspect the next element to be processed in the queue.
        """
        if not self.stack2:
            if not self.stack1:
                raise IndexError("Queue is empty")
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]


# Example usage:
if __name__ == "__main__":
    # Create a new queue using stacks
    queue: QueueUsingStacks = QueueUsingStacks()

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

    # Enqueue another element
    queue.enqueue(4)

    # Peek the front element
    print("Peek:", queue.peek())  # Expected output: 3
