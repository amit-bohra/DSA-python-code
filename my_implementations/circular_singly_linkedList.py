class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    # Function to get the value at a specific index
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_value_at_index(self, index: int) -> int:
        """
        Returns the value at the specified index in the circular linked list.
        
        Trick: Traverse the list while keeping track of the current index.

        Example Question: Find the value at the middle of a circular singly linked list.
        """
        if not self.head:
            raise IndexError("Empty list")
        current = self.head
        count = 0
        while count < index:
            current = current.next
            count += 1
            if current == self.head:
                raise IndexError("Index out of range")
        return current.data

    # Function to add a new node at the head of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_at_head(self, data: int) -> None:
        """
        Adds a new node at the beginning of the circular linked list.
        
        Trick: Similar to insert_at_beginning function.

        Example Question: Insert a node in a sorted circular linked list while maintaining its sorted order.
        """
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.next = self.head
            temp.next = new_node
            self.head = new_node

    # Function to add a new node at the tail of the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_at_tail(self, data: int) -> None:
        """
        Adds a new node at the end of the circular linked list.
        
        Trick: Traverse the list to the last node and add the new node.

        Example Question: Implement a queue using a circular linked list.
        """
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.next = self.head
            temp.next = new_node

    # Function to add a new node at a specific index in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_at_index(self, index: int, data: int) -> None:
        """
        Adds a new node at the specified index in the circular linked list.
        
        Trick: Traverse the list to the previous node of the index and adjust pointers.

        Example Question: Implement an algorithm to rotate a circular linked list by k positions.
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
            count += 1
            if current == self.head:
                raise IndexError("Index out of range")
        new_node.next = current.next
        current.next = new_node

    # Function to delete a node at a specific index
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete_at_index(self, index: int) -> None:
        """
        Deletes the node at the specified index in the circular linked list.
        
        Trick: Similar to delete_node function, but keep track of the previous node.

        Example Question: Josephus problem - Eliminate every mth node from a circular linked list until only one node is left.
        """
        if not self.head:
            return
        if index == 0:
            current = self.head
            while current.next != self.head:
                current = current.next
            if self.head == self.head.next:
                self.head = None
            else:
                current.next = self.head.next
                self.head = self.head.next
        else:
            current = self.head
            count = 0
            while count < index - 1:
                current = current.next
                count += 1
                if current.next == self.head:
                    raise IndexError("Index out of range")
            current.next = current.next.next

    # Function to traverse and print the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def print_list(self) -> None:
        """Traverses and prints the elements of the circular linked list."""
        if not self.head:
            print("Empty list")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print()


# Example usage:
if __name__ == "__main__":
    # Create a new circular singly linked list
    csll = CircularSinglyLinkedList()

    # Add nodes at the head
    csll.add_at_head(2)
    csll.add_at_head(1)
    # Expected output: 1 -> 2 ->
    csll.print_list()

    # Add nodes at the tail
    csll.add_at_tail(3)
    csll.add_at_tail(4)
    # Expected output: 1 -> 2 -> 3 -> 4 ->
    csll.print_list()

    # Add node at a specific index
    csll.add_at_index(2, 2.5)
    # Expected output: 1 -> 2 -> 2.5 -> 3 -> 4 ->
    csll.print_list()

    # Delete node at a specific index
    csll.delete_at_index(2)
    # Expected output: 1 -> 2 -> 3 -> 4 ->
    csll.print_list()

    # Get value at a specific index
    print("Value at index 2:", csll.get_value_at_index(2))  # Expected output: 3
