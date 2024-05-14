from typing import Optional, List, Deque
from collections import deque

class TreeNode:
    def __init__(self, key: int):
        self.key = key
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

class BinaryTree:
    def __init__(self):
        self.root: Optional[TreeNode] = None

    def insert(self, key: int) -> None:
        """
        Insert a node in the tree.
        Functioning: Iterates down the tree to find the correct spot for the new node.
        Trick: Like adding a number in a sorted array.
        Example: tree.insert(5)
        Time Complexity: O(h), where h is the height of the tree.
        Space Complexity: O(1), iterative solution.
        """
        if not self.root:
            self.root = TreeNode(key)
            return
        
        current = self.root
        while current:
            if key < current.key:
                if not current.left:
                    current.left = TreeNode(key)
                    return
                current = current.left
            else:
                if not current.right:
                    current.right = TreeNode(key)
                    return
                current = current.right
    
    def delete(self, key: int) -> None:
        """
        Delete a node from the tree.
        Functioning: Finds the node, then rearranges the tree so the binary search property remains true.
        Trick: If node has two children, swap with its in-order successor.
        Example: tree.delete(5)
        Time Complexity: O(h)
        Space Complexity: O(1)
        """
        # Helper function to find the in-order successor
        def min_value_node(node: TreeNode) -> TreeNode:
            current = node
            while current.left:
                current = current.left
            return current

        # Helper function to delete a node
        def delete_node(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
            if not root:
                return root
            
            if key < root.key:
                root.left = delete_node(root.left, key)
            elif key > root.key:
                root.right = delete_node(root.right, key)
            else:
                # Node with only one child or no child
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                
                # Node with two children, get the in-order successor
                temp = min_value_node(root.right)
                root.key = temp.key
                root.right = delete_node(root.right, temp.key)
            
            return root

        self.root = delete_node(self.root, key)

    def recursive_pre_order(self, node: Optional[TreeNode] = None, traversal: List[int] = []) -> List[int]:
        """
        Recursive pre-order traversal.
        Functioning: Visit root, left subtree, then right subtree.
        Trick: Root, Left, Right.
        Example: tree.recursive_pre_order(tree.root)
        Time Complexity: O(n)
        Space Complexity: O(h), where h is the height of the tree due to recursion stack.
        """
        if node is None:
            node = self.root
            traversal = []  # Reset traversal list for fresh traversal
        if node:
            traversal.append(node.key)
            self.recursive_pre_order(node.left, traversal)
            self.recursive_pre_order(node.right, traversal)
        return traversal

    def recursive_post_order(self, node: Optional[TreeNode] = None, traversal: List[int] = []) -> List[int]:
        """
        Recursive post-order traversal.
        Functioning: Visit left subtree, right subtree, then root.
        Trick: Left, Right, Root.
        Example: tree.recursive_post_order(tree.root)
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if node is None:
            node = self.root
            traversal = []  # Reset traversal list for fresh traversal
        if node:
            self.recursive_post_order(node.left, traversal)
            self.recursive_post_order(node.right, traversal)
            traversal.append(node.key)
        return traversal

    def recursive_in_order(self, node: Optional[TreeNode] = None, traversal: List[int] = []) -> List[int]:
        """
        Recursive in-order traversal.
        Functioning: Visit left subtree, root, then right subtree.
        Trick: Left, Root, Right.
        Example: tree.recursive_in_order(tree.root)
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if node is None:
            node = self.root
            traversal = []  # Reset traversal list for fresh traversal
        if node:
            self.recursive_in_order(node.left, traversal)
            traversal.append(node.key)
            self.recursive_in_order(node.right, traversal)
        return traversal

    def iterative_pre_order(self) -> List[int]:
        """
        Iterative pre-order traversal.
        Functioning: Uses a stack to emulate recursion.
        Trick: Use a stack, push right then left.
        Example: tree.iterative_pre_order()
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack, traversal = [self.root], []
        while stack:
            node = stack.pop()
            if node:
                traversal.append(node.key)
                stack.append(node.right)
                stack.append(node.left)
        return traversal

    def iterative_post_order(self) -> List[int]:
        """
        Iterative post-order traversal.
        Functioning: Uses two stacks, one to process nodes and another for the traversal order.
        Trick: Push to the second stack for the correct order.
        Example: tree.iterative_post_order()
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not self.root:
            return []
        
        stack1, stack2, traversal = [self.root], [], []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        
        while stack2:
            node = stack2.pop()
            traversal.append(node.key)
        return traversal

    def iterative_in_order(self) -> List[int]:
        """
        Iterative in-order traversal.
        Functioning: Uses a stack to hold nodes, traverses as far left as possible, then processes nodes.
        Trick: Go left as far as possible, then go right.
        Example: tree.iterative_in_order()
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack, traversal, current = [], [], self.root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            traversal.append(current.key)
            current = current.right
        return traversal

    def recursive_level_order(self, node: Optional[TreeNode] = None) -> List[int]:
        """
        Recursive level order traversal.
        Functioning: Uses recursion to visit each level of the tree.
        Trick: Use a helper function to process each level.
        Example: tree.recursive_level_order(tree.root)
        Time Complexity: O(n^2) in the worst case.
        Space Complexity: O(n) due to the system stack.
        """
        def get_height(node: TreeNode) -> int:
            if not node:
                return 0
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            return max(left_height, right_height) + 1

        def get_level_nodes(node: TreeNode, level: int, traversal: List[int]) -> None:
            if not node:
                return
            if level == 1:
                traversal.append(node.key)
            elif level > 1:
                get_level_nodes(node.left, level-1, traversal)
                get_level_nodes(node.right, level-1, traversal)

        height = get_height(self.root)
        traversal = []
        for i in range(1, height+1):
            get_level_nodes(self.root, i, traversal)
        return traversal

    def iterative_level_order(self) -> List[int]:
        """
        Iterative level order traversal.
        Functioning: Uses a queue to visit nodes level by level.
        Trick: Enqueue children of the current node.
        Example: tree.iterative_level_order()
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not self.root:
            return []
        
        queue: Deque[TreeNode] = deque([self.root])
        traversal = []
        while queue:
            node = queue.popleft()
            traversal.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return traversal

# Example usage with expected outputs as comments

tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

# Expected BST structure after insertions:
#         5
#        / \
#       3   7
#      / \ / \
#     2  4 6  8

print("Pre-order (Recursive):", tree.recursive_pre_order())
# Expected: [5, 3, 2, 4, 7, 6, 8]

print("Post-order (Recursive):", tree.recursive_post_order())
# Expected: [2, 4, 3, 6, 8, 7, 5]

print("In-order (Recursive):", tree.recursive_in_order())
# Expected: [2, 3, 4, 5, 6, 7, 8]

print("Pre-order (Iterative):", tree.iterative_pre_order())
# Expected: [5, 3, 2, 4, 7, 6, 8]

print("Post-order (Iterative):", tree.iterative_post_order())
# Expected: [2, 4, 3, 6, 8, 7, 5]

print("In-order (Iterative):", tree.iterative_in_order())
# Expected: [2, 3, 4, 5, 6, 7, 8]

print("Level-order (Recursive):", tree.recursive_level_order())
# Expected: [5, 3, 7, 2, 4, 6, 8]

print("Level-order (Iterative):", tree.iterative_level_order())
# Expected: [5, 3, 7, 2, 4, 6, 8]

tree.delete(7)
print("In-order (Iterative) after deleting 7:", tree.iterative_in_order())
# Expected after deleting 7: [2, 3, 4, 5, 6, 8]