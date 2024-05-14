from typing import Any, List

class StackWithLimit:
    def __init__(self, limit: int) -> None:
        self.stack: List[Any] = []
        self.limit: int = limit

    # Function to push an element onto the stack
    def push(self, item: Any) -> None:
        """
        Pushes an element onto the stack.
        """
        if len(self.stack) < self.limit:
            self.stack.append(item)
        else:
            raise IndexError("Stack overflow")

    # Function to pop an element from the stack
    def pop(self) -> Any:
        """
        Pops and returns the top element from the stack.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack.pop()

    # Function to check if the stack is empty
    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.
        """
        return len(self.stack) == 0

    # Function to peek the top element of the stack without removing it
    def peek(self) -> Any:
        """
        Returns the top element of the stack without removing it.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[-1]

    # Function to get the size of the stack
    def size(self) -> int:
        """
        Returns the size of the stack.
        """
        return len(self.stack)


# Example usage:
if __name__ == "__main__":
    # Create a new stack with a maximum limit of 3
    stack: StackWithLimit = StackWithLimit(3)

    # Push elements onto the stack
    stack.push(1)
    stack.push(2)
    stack.push(3)

    # Attempt to push beyond the limit
    try:
        stack.push(4)
    except IndexError as e:
        print(e)  # Expected output: Stack overflow

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
