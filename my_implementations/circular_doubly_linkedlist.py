class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    # Function to get the value at a specific index
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_value_at_index(self, index: int) -> int:
        """
        Returns the value at the specified index in the circular doubly linked list.
        
        Trick: Traverse the list in either direction from the head or the tail, depending on which direction is closer.

        Example Question: Find the value at the middle of a circular doubly linked list.
        """
        if index < 0:
            raise IndexError("Index out of range")
        if not self.head:
            raise IndexError("Empty list")
        current = self.head
        count = 0
        while count < index:
            current = current.next
            if current == self.head:
                raise IndexError("Index out of range")
            count += 1
        return current.data

    # Function to add a new node at the head of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_at_head(self, data: int) -> None:
        """
        Adds a new node at the beginning of the circular doubly linked list.
        
        Trick: Similar to add_at_head function in DoublyLinkedList.

        Example Question: Insert a node in a sorted circular doubly linked list while maintaining its sorted order.
        """
        new_node = Node(data)
        if not self.head:
            new_node.prev = new_node
            new_node.next = new_node
            self.head = new_node
        else:
            new_node.prev = self.head.prev
            new_node.next = self.head
            self.head.prev.next = new_node
            self.head.prev = new_node
            self.head = new_node

    # Function to add a new node at the tail of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_at_tail(self, data: int) -> None:
        """
        Adds a new node at the end of the circular doubly linked list.
        
        Trick: Similar to add_at_tail function in DoublyLinkedList.

        Example Question: Implement a queue using a circular doubly linked list.
        """
        new_node = Node(data)
        if not self.head:
            new_node.prev = new_node
            new_node.next = new_node
            self.head = new_node
        else:
            new_node.prev = self.head.prev
            new_node.next = self.head
            self.head.prev.next = new_node
            self.head.prev = new_node

    # Function to add a new node at a specific index in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_at_index(self, index: int, data: int) -> None:
        """
        Adds a new node at the specified index in the circular doubly linked list.
        
        Trick: Traverse the list to the previous node of the index and adjust pointers.

        Example Question: Implement an algorithm to rotate a circular doubly linked list by k positions.
        """
        if index < 0:
            raise IndexError("Index out of range")
        if index == 0:
            self.add_at_head(data)
            return
        new_node = Node(data)
        current = self.head
        count = 0
        while count < index - 1:
            current = current.next
            if current == self.head:
                raise IndexError("Index out of range")
            count += 1
        new_node.prev = current
        new_node.next = current.next
        current.next.prev = new_node
        current.next = new_node

    # Function to delete a node at a specific index
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete_at_index(self, index: int) -> None:
        """
        Deletes the node at the specified index in the circular doubly linked list.
        
        Trick: Similar to delete_at_index function in DoublyLinkedList.

        Example Question: Josephus problem - Eliminate every mth node from a circular doubly linked list until only one node is left.
        """
        if not self.head:
            return
        if index == 0:
            if self.head.next == self.head:
                self.head = None
            else:
                self.head.prev.next = self.head.next
                self.head.next.prev = self.head.prev
                self.head = self.head.next
            return
        current = self.head
        count = 0
        while count < index:
            current = current.next
            if current == self.head:
                raise IndexError("Index out of range")
            count += 1
        current.prev.next = current.next
        current.next.prev = current.prev

    # Function to traverse and print the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def print_list(self) -> None:
        """Traverses and prints the elements of the circular doubly linked list."""
        if not self.head:
            print("Empty list")
            return
        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print()


# Example usage:
if __name__ == "__main__":
    # Create a new circular doubly linked list
    cdll = CircularDoublyLinkedList()

    # Add nodes at the head
    cdll.add_at_head(2)
    cdll.add_at_head(1)
    # Expected output: 1 <-> 2 <-> 
    cdll.print_list()

    # Add nodes at the tail
    cdll.add_at_tail(3)
    cdll.add_at_tail(4)
    # Expected output: 1 <-> 2 <-> 3 <-> 4 <-> 
    cdll.print_list()

    # Add node at a specific index
    cdll.add_at_index(2, 2.5)
    # Expected output: 1 <-> 2 <-> 2.5 <-> 3 <-> 4 <-> 
    cdll.print_list()

    # Delete node at a specific index
    cdll.delete_at_index(2)
    # Expected output: 1 <-> 2 <-> 3 <-> 4 <-> 
    cdll.print_list()

    # Get value at a specific index
    print("Value at index 2:", cdll.get_value_at_index(2))  # Expected output: 3
