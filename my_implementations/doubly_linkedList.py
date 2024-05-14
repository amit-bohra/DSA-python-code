class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Function to get the value at a specific index
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_value_at_index(self, index: int) -> int:
        """
        Returns the value at the specified index in the doubly linked list.
        
        Trick: Traverse the list either from the head or the tail, depending on which direction is closer.

        Example Question: Find the value at the middle of a doubly linked list.
        """
        if index < 0:
            raise IndexError("Index out of range")
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
        Adds a new node at the beginning of the doubly linked list.
        
        Trick: Similar to insert_at_beginning function.

        Example Question: Insert a node in a sorted doubly linked list while maintaining its sorted order.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Function to add a new node at the tail of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_at_tail(self, data: int) -> None:
        """
        Adds a new node at the end of the doubly linked list.
        
        Trick: Similar to insert_at_end function.

        Example Question: Implement a queue using a doubly linked list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # Function to add a new node at a specific index in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_at_index(self, index: int, data: int) -> None:
        """
        Adds a new node at the specified index in the doubly linked list.
        
        Trick: Traverse the list to the previous node of the index and adjust pointers.

        Example Question: Implement an algorithm to reverse a doubly linked list in groups of a given size.
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
            if not current:
                raise IndexError("Index out of range")
            current = current.next
            count += 1
        if not current:
            raise IndexError("Index out of range")
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        if new_node.next is None:
            self.tail = new_node

    # Function to delete a node at a specific index
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete_at_index(self, index: int) -> None:
        """
        Deletes the node at the specified index in the doubly linked list.
        
        Trick: Similar to delete_node function, but keep track of the previous and next nodes.

        Example Question: Remove the nth node from the end of a doubly linked list.
        """
        if not self.head:
            return
        if index == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return
        current = self.head
        count = 0
        while current and count < index:
            current = current.next
            count += 1
        if not current:
            raise IndexError("Index out of range")
        if current == self.tail:
            current.prev.next = None
            self.tail = current.prev
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

    # Function to traverse and print the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def print_list(self) -> None:
        """Traverses and prints the elements of the doubly linked list."""
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


# Example usage:
if __name__ == "__main__":
    # Create a new doubly linked list
    dll = DoublyLinkedList()

    # Add nodes at the head
    dll.add_at_head(2)
    dll.add_at_head(1)
    # Expected output: 1 <-> 2 <-> None
    dll.print_list()

    # Add nodes at the tail
    dll.add_at_tail(3)
    dll.add_at_tail(4)
    # Expected output: 1 <-> 2 <-> 3 <-> 4 <-> None
    dll.print_list()

    # Add node at a specific index
    dll.add_at_index(2, 2.5)
    # Expected output: 1 <-> 2 <-> 2.5 <-> 3 <-> 4 <-> None
    dll.print_list()

    # Delete node at a specific index
    dll.delete_at_index(2)
    # Expected output: 1 <-> 2 <-> 3 <-> 4 <-> None
    dll.print_list()

    # Get value at a specific index
    print("Value at index 2:", dll.get_value_at_index(2))  # Expected output: 3
