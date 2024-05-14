from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class BinaryTree:
    def __init__(self) -> None:
        self.root: Optional[TreeNode] = None

    def insert_node(self, val: int) -> None:
        """
        Inserts a node into the binary tree following a level-order strategy to find the first available spot.

        Trick: Use a queue to perform level-order traversal until an empty spot is found for insertion.

        Example Usage: This function is used to insert a new node into a binary tree.

        Time Complexity: O(n), as it might need to traverse the entire tree to find an empty spot.
        Space Complexity: O(n), due to the use of a queue to facilitate level-order traversal.
        """
        new_node = TreeNode(val)
        if not self.root:
            self.root = new_node
            return

        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            if not current.left:
                current.left = new_node
                return
            else:
                queue.append(current.left)
            if not current.right:
                current.right = new_node
                return
            else:
                queue.append(current.right)

    def delete_node(self, val: int) -> bool:
        """
        Deletes a node with the specified value from the binary tree by swapping it with the deepest rightmost node and then removing the deepest rightmost node.

        Trick: Perform a level-order traversal to find both the target node and the deepest rightmost node.

        Example Usage: This method can be used to delete a node from a binary tree while attempting to maintain the completeness of the tree.

        Time Complexity: O(n), as it may need to traverse the entire tree to find the node and the deepest rightmost node.
        Space Complexity: O(n), due to the use of a queue for level-order traversal.

        :param val: The value of the node to be deleted.
        :return: True if the node was found and deleted, False otherwise.
        """
        if not self.root:
            return False

        queue = deque([self.root])
        node_to_delete, last_node = None, None

        while queue:
            last_node = queue.popleft()

            if last_node.val == val:
                node_to_delete = last_node

            if last_node.left:
                queue.append(last_node.left)
            if last_node.right:
                queue.append(last_node.right)

        if node_to_delete:
            if last_node:
                node_to_delete.val = last_node.val  # Swap values
                # Now, remove the last node using a similar level-order traversal to find its parent
                queue.append(self.root)
                while queue:
                    temp = queue.popleft()
                    if temp.left:
                        if temp.left == last_node:
                            temp.left = None
                            break
                        else:
                            queue.append(temp.left)
                    if temp.right:
                        if temp.right == last_node:
                            temp.right = None
                            break
                        else:
                            queue.append(temp.right)
            return True

        return False

    # Function for inorder traversal of the binary tree
    # Time Complexity: O(n)
    # Space Complexity: O(n) (in addition to recursive stack space)

    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs inorder traversal of the binary tree.

        Trick: Recursively traverse the left subtree, visit the current node, and then traverse the right subtree.

        Example Usage: Used to print the nodes of the binary tree in inorder sequence.
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

    # Iterative inorder traversal of the binary tree
    # Time Complexity: O(n)
    # Space Complexity: O(n) (in addition to recursive stack space)

    def iterative_inorder_traversal(self) -> List[int]:
        """
        Performs iterative inorder traversal of the binary tree.

        Trick: Use a stack to simulate the recursive function call.

        Example Usage: Used to print the nodes of the binary tree in inorder sequence.
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

    # Function for preorder traversal of the binary tree
    # Time Complexity: O(n)
    # Space Complexity: O(n) (in addition to recursive stack space)

    def preorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs preorder traversal of the binary tree.

        Trick: Visit the current node, then recursively traverse the left subtree followed by the right subtree.

        Example Usage: Used to print the nodes of the binary tree in preorder sequence.
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

    # Iterative preorder traversal of the binary tree
    # Time Complexity: O(n)
    # Space Complexity: O(n) (in addition to recursive stack space)

    def iterative_preorder_traversal(self) -> List[int]:
        """
        Performs iterative preorder traversal of the binary tree.

        Trick: Use a stack to simulate the recursive function call.

        Example Usage: Used to print the nodes of the binary tree in preorder sequence.
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

    # Function for postorder traversal of the binary tree
    # Time Complexity: O(n)
    # Space Complexity: O(n) (in addition to recursive stack space)

    def postorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs postorder traversal of the binary tree.

        Trick: Recursively traverse the left subtree, then the right subtree, and finally visit the current node.

        Example Usage: Used to print the nodes of the binary tree in postorder sequence.
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

    # Iterative postorder traversal of the binary tree
    # Time Complexity: O(n)
    # Space Complexity: O(n) (in addition to recursive stack space)

    def iterative_postorder_traversal(self) -> List[int]:
        """
        Performs iterative postorder traversal of the binary tree.

        Trick: Use a stack to simulate the recursive function call.

        Example Usage: Used to print the nodes of the binary tree in postorder sequence.
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

    # Function for level order traversal of the binary tree
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    def level_order_traversal(self) -> List[int]:
        """
        Performs level order traversal of the binary tree.

        Trick: Use a deque to traverse each level of the binary tree level by level.

        Example Usage: Used to print the nodes of the binary tree in level order.
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

    # Recursive level order traversal of the binary tree
    # Time Complexity: O(n)
    # Space Complexity: O(n) (system stack) + O(n) (result list)

    def recursive_level_order_traversal(self) -> List[int]:
        """
        Performs recursive level order traversal of the binary tree.

        Trick: Use a helper function to traverse the tree level by level recursively.

        Example Usage: Used to print the nodes of the binary tree in level order.
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
    # Create a new binary tree
    bt: BinaryTree = BinaryTree()

    # Insert nodes into the binary tree
    bt.insert_node(10)
    bt.insert_node(5)
    bt.insert_node(15)
    bt.insert_node(3)
    bt.insert_node(7)
    bt.insert_node(12)
    bt.insert_node(18)

    # Perform inorder traversal
    print("Inorder Traversal:")
    # Expected output: 3 5 7 10 12 15 18
    print(bt.inorder_traversal(bt.root))

    # Perform preorder traversal
    print("\nPreorder Traversal:")
    # Expected output: 10 5 3 7 15 12 18
    print(bt.preorder_traversal(bt.root))

    # Perform postorder traversal
    print("\nPostorder Traversal:")
    # Expected output: 3 7 5 12 18 15 10
    print(bt.postorder_traversal(bt.root))

    # Perform level order traversal
    print("\nLevel Order Traversal:")
    print(bt.level_order_traversal())  # Expected output: 10 5 15 3 7 12 18

    # Perform iterative inorder traversal
    print("\nIterative Inorder Traversal:")
    # Expected output: [3, 5, 7, 10, 12, 15, 18]
    print(bt.iterative_inorder_traversal())

    # Perform iterative preorder traversal
    print("\nIterative Preorder Traversal:")
    # Expected output: [10, 5, 3, 7, 15, 12, 18]
    print(bt.iterative_preorder_traversal())

    # Perform iterative postorder traversal
    print("\nIterative Postorder Traversal:")
    # Expected output: [3, 7, 5, 12, 18, 15, 10]
    print(bt.iterative_postorder_traversal())

    # Perform recursive level order traversal
    print("\nRecursive Level Order Traversal:")
    # Expected output: [10, 5, 15, 3, 7, 12, 18]
    print(bt.recursive_level_order_traversal())

    print(bt.delete_node(12))
    print(bt.recursive_level_order_traversal())
