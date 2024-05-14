class Node:
    def __init__(self, data: any) -> None:
        self.data: any = data
        self.next: Node = None


class Stack:
    def __init__(self) -> None:
        self.top: Node = None

    # Function to push an element onto the stack
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def push(self, item: any) -> None:
        """
        Pushes an element onto the stack.
        
        Trick: Create a new node and make it the new top of the stack.

        Example Usage: Used to implement algorithms like expression evaluation.
        """
        new_node: Node = Node(item)
        new_node.next = self.top
        self.top = new_node

    # Function to pop an element from the stack
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def pop(self) -> any:
        """
        Pops and returns the top element from the stack.
        
        Trick: Remove and return the top node from the stack.

        Example Usage: Used to implement algorithms like backtracking.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        item: any = self.top.data
        self.top = self.top.next
        return item

    # Function to check if the stack is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.
        
        Trick: Check if the top of the stack is None.

        Example Usage: Used to handle base cases in recursive algorithms.
        """
        return self.top is None

    # Function to peek the top element of the stack without removing it
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def peek(self) -> any:
        """
        Returns the top element of the stack without removing it.
        
        Trick: Return the data of the top node without removing it.

        Example Usage: Used in algorithms that require looking at the top element without removing it.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.data


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











