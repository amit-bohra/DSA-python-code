from typing import List, Optional
from collections import deque

'''
class TreeNode:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.left: class TreeNode:
                        def __init__(self, val: int) -> None:
                            self.val: int = val
                            self.left: Optional[TreeNode] = None
                            self.right: Optional[TreeNode] = None
        self.right: = class TreeNode:
                        def __init__(self, val: int) -> None:
                            self.val: int = val
                            self.left: Optional[TreeNode] = None
                            self.right: Optional[TreeNode] = None

        node = TreeNode(1)
        print(node.val)
        node.left = TreeNode(2)
        node.right = TreeNode(3)
        node.left.left = TreeNode(4)
        node.left.right = TreeNode(5)
        node.right.left = TreeNode(6)
        node.right.right = TreeNode(7)

           1
          2 3
        4 5 6 7


        node # Created Above

        result = [4, 5, 2, 6, 7, 3, 1]

        def postOrder(node):
            if node:
                postOrder(node.left)
                postOrder(node.right)
                result.append(node.val)


        postOrder(node)


        result = [1,2, 4, 5, 3, 6, 7]


        def preOrder(node):
            if node:
                result.append(node.val)
                preOrder(node.left)
                preOrder(node.right)

        preOrder(node)


        result = [1,2, 4, 5, 3, 6, 7]
        


        def inorder(node):
            if node:
                inorder(node.left)
                result.append(node.val)
                inorder(node.right)

        inorder(node)


        result = [4, 2, 5, 1, 6, 3, 7]
        inorder(1) -> inorder(3) -> inorder(6)
            

        print(node.val)
        print(node.left.val)
        print(node.left.left)
        print(node.left.right)
        print(node.right.val)
'''


class TreeNode:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Optional[TreeNode] = None

    # Function to insert a node into the binary search tree
    # Time Complexity: O(log n) on average (when the tree is balanced)
    #                   O(n) in the worst case (when the tree is highly unbalanced)
    # Space Complexity: O(1) (in addition to recursive stack space)

    def insert_node(self, val: int) -> None:
        """
        Inserts a node into the binary search tree.

        Trick: Recursively traverse the tree to find the correct position for insertion.

        Example Usage: Used to build a binary search tree by inserting nodes.
        """

        # Define a helper function for insertion
        def _insert(root: Optional[TreeNode], val: int) -> TreeNode:
            # Base case: if the root is None, create a new node with the given val
            if not root:
                return TreeNode(val)

            # If the val is less than the current node's val, insert it into the left subtree
            if val < root.val:
                root.left = _insert(root.left, val)
            # If the val is greater than the current node's val, insert it into the right subtree
            elif val > root.val:
                root.right = _insert(root.right, val)

            # Return the modified root
            return root

        # If the tree is empty, set the root to the newly inserted node
        if not self.root:
            self.root = TreeNode(val)
        else:
            # Call the helper function to recursively insert the node
            self.root = _insert(self.root, val)

    # Function to delete a node from the binary search tree
    # Time Complexity: O(log n) on average (when the tree is balanced)
    #                   O(n) in the worst case (when the tree is highly unbalanced)
    # Space Complexity: O(1) (in addition to recursive stack space)

    def delete_node(self, val: int) -> None:
        """
        Deletes a node with the given value from the binary search tree.

        Trick: Recursively search for the node to delete, then handle the cases based on the number of children.

        Example Usage: Used to remove a specific node from the binary search tree.
        """

        # Define a helper function to find the node with the minimum value in a subtree
        def _min_value_node(node: TreeNode) -> TreeNode:
            # If the input node is None, there's no minimum value node, return None
            if not node:
                return None

            # Start with the input node
            current = node

            # Traverse left until reaching the leftmost node (smallest value)
            while current.left:
                current = current.left

            # Return the leftmost node, which contains the minimum value
            return current

        # Define a recursive helper function to delete the node with the given val
        def _delete(root: Optional[TreeNode], val: int) -> TreeNode:
            # Base case: if the root is None, return None
            if not root:
                return root

            # If the val is smaller than the root's val, go left
            if val < root.val:
                root.left = _delete(root.left, val)
            # If the val is greater than the root's val, go right
            elif val > root.val:
                root.right = _delete(root.right, val)
            else:  # Found the node to delete
                # Case 1: Node to be deleted has no children or only one child
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:  # Case 2: Node to be deleted has two children
                    # Find the inorder successor (smallest node in the right subtree)
                    temp = _min_value_node(root.right)
                    # Copy the inorder successor's val to this node
                    root.val = temp.val
                    # Delete the inorder successor
                    root.right = _delete(root.right, temp.val)

            # Return the modified root
            return root

        # Call the helper function to delete the node with the given val
        self.root = _delete(self.root, val)

    # Function for inorder traversal of the binary search tree
    # Time Complexity: O(n)
    # Space Complexity: O(n) (in addition to recursive stack space)

    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs inorder traversal of the binary search tree.

        Trick: Recursively traverse the left subtree, visit the current node, and then traverse the right subtree.

        Example Usage: Used to print the nodes of the binary search tree in inorder sequence.
        """
        # Initialize an empty list to store the inorder traversal result
        result = []

        # Define a recursive helper function to perform inorder traversal
        def _inorder_traversal(root: Optional[TreeNode]) -> None:
            if root:
                # Traverse the left subtree
                _inorder_traversal(root.left)
                # Visit the current node
                result.append(root.val)
                # Traverse the right subtree
                _inorder_traversal(root.right)

        # Call the recursive helper function with the root node
        _inorder_traversal(root)

        # Return the inorder traversal result
        return result

    # Iterative inorder traversal of the binary search tree
    # Time Complexity: O(n)
    # Space Complexity: O(n) (in addition to recursive stack space)

    def iterative_inorder_traversal(self) -> List[int]:
        """
        Performs iterative inorder traversal of the binary search tree.

        Trick: Use a stack to simulate the recursive function call.

        Example Usage: Used to print the nodes of the binary search tree in inorder sequence.
        """
        # Initialize an empty list to store the inorder traversal result
        result = []

        # Initialize an empty stack for iterative traversal
        stack = []

        # Start traversal from the root node
        current = self.root

        # Traverse the tree until the current node is None and the stack is empty
        while current or stack:
            # Traverse left subtree until reaching the leftmost node
            while current:
                stack.append(current)
                current = current.left

            # Process the current node (leftmost node)
            current = stack.pop()
            result.append(current.val)

            # Move to the right subtree
            current = current.right

        # Return the inorder traversal result
        return result

    # Function for preorder traversal of the binary search tree
    # Time Complexity: O(n)
    # Space Complexity: O(n) (in addition to recursive stack space)

    def preorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs preorder traversal of the binary search tree.

        Trick: Visit the current node, then recursively traverse the left subtree followed by the right subtree.

        Example Usage: Used to print the nodes of the binary search tree in preorder sequence.
        """
        # Initialize an empty list to store the preorder traversal result
        result = []

        # Define a recursive helper function to perform preorder traversal
        def _preorder_traversal(root: Optional[TreeNode]) -> None:
            if root:
                # Visit the current node
                result.append(root.val)
                # Recursively traverse the left subtree
                _preorder_traversal(root.left)
                # Recursively traverse the right subtree
                _preorder_traversal(root.right)

        # Call the recursive helper function with the root node
        _preorder_traversal(root)

        # Return the preorder traversal result
        return result

    # Iterative preorder traversal of the binary search tree
    # Time Complexity: O(n)
    # Space Complexity: O(n) (in addition to recursive stack space)

    def iterative_preorder_traversal(self) -> List[int]:
        """
        Performs iterative preorder traversal of the binary search tree.

        Trick: Use a stack to simulate the recursive function call.

        Example Usage: Used to print the nodes of the binary search tree in preorder sequence.
        """
        # Initialize an empty list to store the preorder traversal result
        result = []

        # Initialize a stack with the root node if it exists, otherwise an empty stack
        stack = [self.root] if self.root else []

        # Traverse the tree while the stack is not empty
        while stack:
            # Pop the top node from the stack
            current = stack.pop()

            # Process the current node (add its val to the result)
            result.append(current.val)

            # Push the right child onto the stack first to ensure left child is processed first (LIFO)
            if current.right:
                stack.append(current.right)
            # Push the left child onto the stack
            if current.left:
                stack.append(current.left)

        # Return the preorder traversal result
        return result

    # Function for postorder traversal of the binary search tree
    # Time Complexity: O(n)
    # Space Complexity: O(n) (in addition to recursive stack space)

    def postorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs postorder traversal of the binary search tree.

        Trick: Recursively traverse the left subtree, then the right subtree, and finally visit the current node.

        Example Usage: Used to print the nodes of the binary search tree in postorder sequence.
        """
        # Initialize an empty list to store the postorder traversal result
        result = []

        # Define a recursive helper function to perform postorder traversal
        def _postorder_traversal(root: Optional[TreeNode]) -> None:
            if root:
                # Traverse the left subtree
                _postorder_traversal(root.left)
                # Traverse the right subtree
                _postorder_traversal(root.right)
                # Visit the current node
                result.append(root.val)

        # Call the recursive helper function with the root node
        _postorder_traversal(root)

        # Return the postorder traversal result
        return result

    # Iterative postorder traversal of the binary search tree
    # Time Complexity: O(n)
    # Space Complexity: O(n) (in addition to recursive stack space)

    def iterative_postorder_traversal(self) -> List[int]:
        """
        Performs iterative postorder traversal of the binary search tree.

        Trick: Use a stack to simulate the recursive function call.

        Example Usage: Used to print the nodes of the binary search tree in postorder sequence.
        """
        # Initialize an empty list to store the postorder traversal result
        result = []

        # Initialize a stack with the root node if it exists, otherwise an empty stack
        stack = [self.root] if self.root else []

        # Traverse the tree while the stack is not empty
        while stack:
            # Pop the top node from the stack
            current = stack.pop()

            # Process the current node (add its val to the result)
            result.append(current.val)

            # Push the left child onto the stack first
            if current.left:
                stack.append(current.left)
            # Push the right child onto the stack next
            if current.right:
                stack.append(current.right)

        # Return the reversed result to obtain the postorder traversal
        return result[::-1]

    # Function for level order traversal of the binary search tree
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    def level_order_traversal(self) -> List[int]:
        """
        Performs level order traversal of the binary search tree.

        Trick: Use a deque to traverse each level of the binary search tree level by level.

        Example Usage: Used to print the nodes of the binary search tree in level order.
        """
        # Initialize an empty list to store the level order traversal result
        result = []

        # If the tree is empty, return an empty result
        if not self.root:
            return result

        # Initialize a deque with the root node
        queue = deque([self.root])

        # Traverse the tree level by level
        while queue:
            # Pop the front node from the deque (current level node)
            current = queue.popleft()

            # Process the current node (add its val to the result)
            result.append(current.val)

            # Add the left and right children of the current node to the queue
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        # Return the level order traversal result
        return result

    # Recursive level order traversal of the binary search tree
    # Time Complexity: O(n)
    # Space Complexity: O(n) (system stack) + O(n) (result list)

    def recursive_level_order_traversal(self) -> List[int]:
        """
        Performs recursive level order traversal of the binary search tree.

        Trick: Use a helper function to traverse the tree level by level recursively.

        Example Usage: Used to print the nodes of the binary search tree in level order.
        """
        # Define a helper function to traverse the tree level by level recursively
        def _recursive_level_order(node: Optional[TreeNode], level: int) -> None:
            # If the node is None, return
            if not node:
                return
            # If the length of the result list is equal to the current level, append a new empty list
            if len(result) == level:
                result.append([])
            # Append the val of the current node to the list at the current level
            result[level].append(node.val)
            # Recursively traverse the left and right subtrees with increased level
            _recursive_level_order(node.left, level + 1)
            _recursive_level_order(node.right, level + 1)

        # Initialize an empty list to store the level order traversal result
        result = []

        # Call the recursive helper function with the root node and level 0
        _recursive_level_order(self.root, 0)

        # Flatten the nested lists and return the result
        return [item for sublist in result for item in sublist]


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
    # Expected output: 3 5 7 10 12 15 18
    print(bst.inorder_traversal(bst.root))

    # Perform preorder traversal
    print("\nPreorder Traversal:")
    # Expected output: 10 5 3 7 15 12 18
    print(bst.preorder_traversal(bst.root))

    # Perform postorder traversal
    print("\nPostorder Traversal:")
    # Expected output: 3 7 5 12 18 15 10
    print(bst.postorder_traversal(bst.root))

    # Perform level order traversal
    print("\nLevel Order Traversal:")
    print(bst.level_order_traversal())  # Expected output: 10 5 15 3 7 12 18

    # Perform iterative inorder traversal
    print("\nIterative Inorder Traversal:")
    # Expected output: [3, 5, 7, 10, 12, 15, 18]
    print(bst.iterative_inorder_traversal())

    # Perform iterative preorder traversal
    print("\nIterative Preorder Traversal:")
    # Expected output: [10, 5, 3, 7, 15, 12, 18]
    print(bst.iterative_preorder_traversal())

    # Perform iterative postorder traversal
    print("\nIterative Postorder Traversal:")
    # Expected output: [3, 7, 5, 12, 18, 15, 10]
    print(bst.iterative_postorder_traversal())

    # Perform recursive level order traversal
    print("\nRecursive Level Order Traversal:")
    # Expected output: [10, 5, 15, 3, 7, 12, 18]
    print(bst.recursive_level_order_traversal())
