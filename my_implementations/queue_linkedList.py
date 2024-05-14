class Node:
    def __init__(self, data: any) -> None:
        self.data: any = data
        self.next: Node = None


class Queue:
    def __init__(self) -> None:
        self.front: Node = None
        self.rear: Node = None
        self.size: int = 0

    # Function to enqueue an element into the queue
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def enqueue(self, item: any) -> None:
        """
        Enqueues an element into the queue.

        Trick: Add the element at the rear of the queue.

        Example Usage: Used in BFS (breadth-first search) algorithms for traversing graphs.
        """
        new_node: Node = Node(item)
        if self.is_empty():
            self.front: Node = new_node
        else:
            self.rear.next = new_node
        self.rear: Node = new_node
        self.size += 1

    # Function to dequeue an element from the queue
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def dequeue(self) -> any:
        """
        Dequeues and returns the front element from the queue.

        Trick: Remove the element from the front of the queue.

        Example Usage: Used in scheduling tasks in operating systems.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        front_data: any = self.front.data
        self.front: Node = self.front.next
        if self.front is None:
            self.rear: Node = None
        self.size -= 1
        return front_data

    # Function to check if the queue is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.

        Trick: Check if the front pointer is None.

        Example Usage: Used in algorithms to handle base cases when processing elements in a queue.
        """
        return self.front is None

    # Function to peek the front element of the queue without removing it
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def peek(self) -> any:
        """
        Returns the front element of the queue without removing it.

        Trick: Return the data of the front node without moving the front pointer.

        Example Usage: Used in algorithms to inspect the next element to be processed in the queue.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data

    # Function to get the size of the queue
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_size(self) -> int:
        """
        Returns the size of the queue.

        Trick: Return the stored size variable.

        Example Usage: Used in algorithms to monitor the size of the queue during processing.
        """
        return self.size


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

    # Enqueue another element
    queue.enqueue(4)

    # Get the size of the queue
    print("Size:", queue.get_size())  # Expected output: 2
