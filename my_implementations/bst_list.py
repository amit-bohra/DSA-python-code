from collections import deque
from typing import List


class BinarySearchTree:
    def __init__(self) -> None:
        self.tree: List[int] = []

    # Function to insert a node into the binary search tree
    # Time Complexity: O(log n) on average (when the tree is balanced)
    #                   O(n) in the worst case (when the tree is highly unbalanced)
    # Space Complexity: O(1)
    def insert_node(self, val: int) -> None:
        """
        Inserts a node into the binary search tree.

        Trick: Perform a binary search to find the correct position for insertion.

        Example Usage: Used to build a binary search tree by inserting nodes.
        """
        # If the tree is empty, insert the val as the root node
        if not self.tree:
            self.tree.append(val)
            return

        # Define a recursive helper function to insert the val into the tree
        def _insert(node: List[int], index: int) -> None:
            # If the current index is at the end of the node list, append the val
            if index == len(node):
                node.append(val)
            # If the val is less than the current node's val, go left
            elif val < node[index]:
                _insert(node, 2 * index + 1)
            # If the val is greater than or equal to the current node's val, go right
            else:
                _insert(node, 2 * index + 2)

        # Call the helper function to insert the val into the tree
        _insert(self.tree, 0)

    # Function to delete a node from the binary search tree
    # Time Complexity: O(log n) on average (when the tree is balanced)
    #                   O(n) in the worst case (when the tree is highly unbalanced)
    # Space Complexity: O(1)
    def delete_node(self, val: int) -> None:
        """
        Deletes a node with the given val from the binary search tree.

        Trick: Find the node to delete, then handle the cases based on the number of children.

        Example Usage: Used to remove a specific node from the binary search tree.
        """
        def find_min(node: List[int]) -> List[int]:
            # Function to find the minimum val node in the subtree rooted at 'node'
            current = node
            while current[1] is not None:
                current = current[1]
            return current

        def delete(node: List[int], index: int) -> List[int]:
            # Recursive function to delete the node with the given val
            if node[index] is None:
                return node  # Base case: Val not found, return the current node

            if val < node[index]:
                node[2 * index + 1] = delete(node[2 * index + 1], 0)
            elif val > node[index]:
                node[2 * index + 2] = delete(node[2 * index + 2], 0)
            else:
                # Case 1: Node to be deleted has no children or only one child
                if node[1] is None:
                    return node[2]  # Return the right child (if exists) or None
                elif node[2] is None:
                    return node[1]  # Return the left child (no right child)

                # Case 2: Node to be deleted has two children
                temp = find_min(node[2])  # Find the minimum val node in the right subtree
                node[0] = temp[0]  # Copy the val of the minimum node to the current node
                node[2] = delete(node[2], 0)  # Delete the minimum val node from the right subtree

            return node

        # Check if the tree is empty
        if not self.tree:
            return  # Tree is empty, no node to delete

        # Call the recursive helper function to delete the node with the given val
        self.tree = delete(self.tree, 0)

    # Function for inorder traversal of the binary search tree
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder_traversal(self, index: int = 0) -> List[int]:
        """
        Performs inorder traversal of the binary search tree.

        Trick: Recursively traverse the left subtree, visit the current node, and then traverse the right subtree.

        Example Usage: Used to print the nodes of the binary search tree in inorder sequence.
        """
        # Initialize an empty list to store the inorder traversal result
        result = []

        # Check if the current index is within the bounds of the tree and if the current node exists
        if index < len(self.tree) and self.tree[index] is not None:
            # Recursively traverse the left subtree
            result += self.inorder_traversal(2 * index + 1)
            
            # Visit the current node
            result.append(self.tree[index])
            
            # Recursively traverse the right subtree
            result += self.inorder_traversal(2 * index + 2)
        
        # Return the inorder traversal result
        return result

    # Function for preorder traversal of the binary search tree
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def preorder_traversal(self, index: int = 0) -> List[int]:
        """
        Performs preorder traversal of the binary search tree.

        Trick: Visit the current node, then recursively traverse the left subtree followed by the right subtree.

        Example Usage: Used to print the nodes of the binary search tree in preorder sequence.
        """
        # Initialize an empty list to store the preorder traversal result
        result = []

        # Check if the current index is within the bounds of the tree and if the current node exists
        if index < len(self.tree) and self.tree[index] is not None:
            # Visit the current node
            result.append(self.tree[index])
            
            # Recursively traverse the left subtree
            result += self.preorder_traversal(2 * index + 1)
            
            # Recursively traverse the right subtree
            result += self.preorder_traversal(2 * index + 2)
        
        # Return the preorder traversal result
        return result

    # Function for postorder traversal of the binary search tree
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def postorder_traversal(self, index: int = 0) -> List[int]:
        """
        Performs postorder traversal of the binary search tree.

        Trick: Recursively traverse the left subtree, then the right subtree, and finally visit the current node.

        Example Usage: Used to print the nodes of the binary search tree in postorder sequence.
        """
        # Initialize an empty list to store the postorder traversal result
        result = []

        # Check if the current index is within the bounds of the tree and if the current node exists
        if index < len(self.tree) and self.tree[index] is not None:
            # Recursively traverse the left subtree
            result += self.postorder_traversal(2 * index + 1)
            
            # Recursively traverse the right subtree
            result += self.postorder_traversal(2 * index + 2)
            
            # Visit the current node
            result.append(self.tree[index])
        
        # Return the postorder traversal result
        return result

    # Function for level order traversal of the binary search tree
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def level_order_traversal(self) -> List[int]:
        """
        Performs level order traversal of the binary search tree.

        Trick: Use a queue to traverse each level of the binary search tree level by level.

        Example Usage: Used to print the nodes of the binary search tree in level order.
        """
        # If the tree is empty, return an empty list
        if not self.tree:
            return []

        # Initialize an empty list to store the level order traversal result
        result = []

        # Initialize a deque with the root index
        queue = deque([0])

        # Traverse the tree level by level
        while queue:
            # Pop the front index from the deque (current level node)
            index = queue.popleft()
            
            # Process the current node (add its val to the result)
            result.append(self.tree[index])
            
            # Add the left child index to the queue if it exists and is not None
            if 2 * index + 1 < len(self.tree) and self.tree[2 * index + 1] is not None:
                queue.append(2 * index + 1)
            
            # Add the right child index to the queue if it exists and is not None
            if 2 * index + 2 < len(self.tree) and self.tree[2 * index + 2] is not None:
                queue.append(2 * index + 2)

        # Return the level order traversal result
        return result
    # Iterative inorder traversal of the binary search tree
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def iterative_inorder_traversal(self) -> List[int]:
        """
        Performs iterative inorder traversal of the binary search tree.

        Trick: Use a stack to simulate the recursive function call.

        Example Usage: Used to print the nodes of the binary search tree in inorder sequence.
        """
        # Initialize an empty list to store the inorder traversal result
        result = []
        
        # Initialize an empty stack
        stack = []
        
        # Start traversal from the root index
        current = 0

        # Traverse the tree until the stack is empty and all nodes are visited
        while stack or current < len(self.tree):
            # Traverse the left subtree and push nodes onto the stack
            while current < len(self.tree) and self.tree[current] is not None:
                stack.append(current)
                current = 2 * current + 1
            
            # If there are nodes in the stack, pop the top node, add its val to the result, and move to its right child
            if stack:
                current = stack.pop()
                result.append(self.tree[current])
                current = 2 * current + 2

        # Return the inorder traversal result
        return result

    # Iterative preorder traversal of the binary search tree
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def iterative_preorder_traversal(self) -> List[int]:
        """
        Performs iterative preorder traversal of the binary search tree.

        Trick: Use a stack to simulate the recursive function call.

        Example Usage: Used to print the nodes of the binary search tree in preorder sequence.
        """
        # Initialize an empty list to store the preorder traversal result
        result = []
        
        # Initialize a stack with the root index
        stack = [0]

        # Traverse the tree until the stack is empty
        while stack:
            # Pop the top index from the stack
            current = stack.pop()
            
            # If the current node is not None, add its val to the result
            if self.tree[current] is not None:
                result.append(self.tree[current])
                
                # Push the right child index onto the stack first to ensure left child is processed first (LIFO)
                if 2 * current + 2 < len(self.tree) and self.tree[2 * current + 2] is not None:
                    stack.append(2 * current + 2)
                # Push the left child index onto the stack
                if 2 * current + 1 < len(self.tree) and self.tree[2 * current + 1] is not None:
                    stack.append(2 * current + 1)

        # Return the preorder traversal result
        return result

    # Iterative postorder traversal of the binary search tree
    # Time Complexity: O(n)
    # Space Complexity: O(n) (in addition to recursive stack space)
    def iterative_postorder_traversal(self) -> List[int]:
        """
        Performs iterative postorder traversal of the binary search tree.

        Trick: Use a single stack to simulate the recursive function call.

        Example Usage: Used to print the nodes of the binary search tree in postorder sequence.
        """
        # Initialize an empty list to store the postorder traversal result
        result = []
        
        # Initialize a stack with tuples containing index and a boolean flag indicating if the node is visited
        stack = [(0, False)]  # (index, is_visited)

        # Traverse the tree until the stack is empty
        while stack:
            # Pop the top index and its visited flag from the stack
            index, is_visited = stack.pop()

            # If the current index is within the bounds of the tree and the node is not None
            if index < len(self.tree) and self.tree[index] is not None:
                # If the node is visited, add its val to the result
                if is_visited:
                    result.append(self.tree[index])
                else:
                    # If the node is not visited, mark it as visited and push back to the stack
                    stack.append((index, True))
                    # Push the right child index onto the stack first to visit it first in postorder
                    stack.append((2 * index + 2, False))
                    # Push the left child index onto the stack
                    stack.append((2 * index + 1, False))

        # Return the postorder traversal result
        return result

    # Recursive level order traversal of the binary search tree
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def recursive_level_order_traversal(self, index: int = 0, result: List[int] = None) -> List[int]:
        """
        Performs recursive level order traversal of the binary search tree.

        Trick: Recursively traverse each level of the binary search tree.

        Example Usage: Used to print the nodes of the binary search tree in level order.
        """
        # Initialize the result list if it's None
        if result is None:
            result = []

        # Check if the current index is within the bounds of the tree and if the node is not None
        if index < len(self.tree) and self.tree[index] is not None:
            # Add the val of the current node to the result
            result.append(self.tree[index])
            
            # Recursively traverse the left subtree
            self.recursive_level_order_traversal(2 * index + 1, result)
            
            # Recursively traverse the right subtree
            self.recursive_level_order_traversal(2 * index + 2, result)

        # Return the level order traversal result
        return result

# Example usage:
if __name__ == "__main__":
    # Create a new binary search tree
    bst: BinarySearchTree = BinarySearchTree()

    # Insert nodes into the binary search tree
    bst.insert_node(10)
    bst.insert_node(5)
    bst.insert_node(15)
    bst.insert_node(3)
    bst.insert_node(7)
    bst.insert_node(12)
    bst.insert_node(18)

    # Perform inorder traversal
    print("Inorder Traversal:")
    # Expected output: [3, 5, 7, 10, 12, 15, 18]
    print(bst.inorder_traversal())
    print()

    # Perform iterative inorder traversal
    print("Iterative Inorder Traversal:")
    # Expected output: [3, 5, 7, 10, 12, 15, 18]
    print(bst.iterative_inorder_traversal())
    print()

    # Perform preorder traversal
    print("Preorder Traversal:")
    # Expected output: [10, 5, 3, 7, 15, 12, 18]
    print(bst.preorder_traversal())
    print()

    # Perform iterative preorder traversal
    print("Iterative Preorder Traversal:")
    # Expected output: [10, 5, 3, 7, 15, 12, 18]
    print(bst.iterative_preorder_traversal())
    print()

    # Perform postorder traversal
    print("Postorder Traversal:")
    # Expected output: [3, 7, 5, 12, 18, 15, 10]
    print(bst.postorder_traversal())
    print()

    # Perform iterative postorder traversal
    print("Iterative Postorder Traversal:")
    # Expected output: [3, 7, 5, 12, 18, 15, 10]
    print(bst.iterative_postorder_traversal())
    print()

    # Perform level order traversal
    print("Level Order Traversal:")
    # Expected output: [10, 5, 15, 3, 7, 12, 18]
    print(bst.level_order_traversal())
    print()

    # Perform recursive level order traversal
    print("Recursive Level Order Traversal:")
    # Expected output: [10, 5, 15, 3, 7, 12, 18]
    print(bst.recursive_level_order_traversal())
    print()
