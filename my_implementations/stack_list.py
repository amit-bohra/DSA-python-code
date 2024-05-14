from typing import Any, List

class Stack:
    def __init__(self) -> None:
        self.stack: List = []

    # Function to push an element onto the stack
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def push(self, item: Any) -> None:
        """
        Pushes an element onto the stack.

        Trick: Append the item to the end of the list.

        Example Usage: Used to implement algorithms like depth-first search (DFS).
        """
        self.stack.append(item)

    # Function to pop an element from the stack
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def pop(self) -> Any:
        """
        Pops and returns the top element from the stack.

        Trick: Pop the last item from the list.

        Example Usage: Used to implement backtracking algorithms.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack.pop()

    # Function to check if the stack is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.

        Trick: Check if the length of the list is zero.

        Example Usage: Used to handle base cases in recursive algorithms.
        """
        return len(self.stack) == 0

    # Function to peek the top element of the stack without removing it
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def peek(self) -> Any:
        """
        Returns the top element of the stack without removing it.

        Trick: Access the last item of the list.

        Example Usage: Used in algorithms that require looking at the top element without removing it.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[-1]


# Example usage:
if __name__ == "__main__":
    # Create a new stack
    stack: Stack = Stack()

    # Push elements onto the stack
    stack.push(1)
    stack.push(2)
    stack.push(3)

    # Peek the top element
    print("Peek:", stack.peek())  # Expected output: 3

    # Pop elements from the stack
    print("Pop:", stack.pop())  # Expected output: 3
    print("Pop:", stack.pop())  # Expected output: 2

    # Check if the stack is empty
    print("Is empty:", stack.is_empty())  # Expected output: False

    # Pop the remaining element
    print("Pop:", stack.pop())  # Expected output: 1

    # Check if the stack is empty after popping all elements
    print("Is empty:", stack.is_empty())  # Expected output: True
