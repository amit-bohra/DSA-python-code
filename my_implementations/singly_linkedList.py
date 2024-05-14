class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Function to get the value at a specific index
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_value_at_index(self, index: int) -> int:
        """
        Returns the value at the specified index in the linked list.
        
        Trick: Traverse the list while keeping track of the current index.

        Example Question: Find the value at the middle of a singly linked list.
        """
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            current = current.next
            count += 1
        raise IndexError("Index out of range")

    # Function to add a new node at the head of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_at_head(self, data: int) -> None:
        """
        Adds a new node at the beginning of the linked list.
        
        Trick: Similar to insert_at_beginning function.

        Example Question: Insert a node in a sorted linked list while maintaining its sorted order.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Function to add a new node at the tail of the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_at_tail(self, data: int) -> None:
        """
        Adds a new node at the end of the linked list.
        
        Trick: Similar to insert_at_end function.

        Example Question: Implement a queue using a linked list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Function to add a new node at a specific index in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_at_index(self, index: int, data: int) -> None:
        """
        Adds a new node at the specified index in the linked list.
        
        Trick: Traverse the list to the previous node of the index and adjust pointers.

        Example Question: Implement an algorithm to reverse a linked list in groups of a given size.
        """
        if index < 0:
            raise IndexError("Index out of range")
        if index == 0:
            self.add_at_head(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            if not current:
                raise IndexError("Index out of range")
            current = current.next
        if not current:
            raise IndexError("Index out of range")
        new_node.next = current.next
        current.next = new_node

    # Function to delete a node at a specific index
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete_at_index(self, index: int) -> None:
        """
        Deletes the node at the specified index in the linked list.
        
        Trick: Similar to delete_node function, but keep track of the previous node.

        Example Question: Remove the nth node from the end of a linked list.
        """
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(index - 1):
            if not current.next:
                raise IndexError("Index out of range")
            current = current.next
        if not current or not current.next:
            raise IndexError("Index out of range")
        current.next = current.next.next

    # Function to traverse and print the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def print_list(self) -> None:
        """Traverses and prints the elements of the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage:
if __name__ == "__main__":
    # Create a new singly linked list
    sll = SinglyLinkedList()

    # Add nodes at the head
    sll.add_at_head(2)
    sll.add_at_head(1)
    # Expected output: 1 -> 2 -> None
    sll.print_list()

    # Add nodes at the tail
    sll.add_at_tail(3)
    sll.add_at_tail(4)
    # Expected output: 1 -> 2 -> 3 -> 4 -> None
    sll.print_list()

    # Add node at a specific index
    sll.add_at_index(2, 2.5)
    # Expected output: 1 -> 2 -> 2.5 -> 3 -> 4 -> None
    sll.print_list()

    # Delete node at a specific index
    sll.delete_at_index(2)
    # Expected output: 1 -> 2 -> 3 -> 4 -> None
    sll.print_list()

    # Get value at a specific index
    print("Value at index 2:", sll.get_value_at_index(2))  # Expected output: 3
