from typing import List, Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

def insert_bst(root: Optional[TreeNode], val: int) -> TreeNode:
    """
    Inserts a value into a Binary Search Tree (BST) rooted at root.
    
    Trick to remember: Use recursive insertion maintaining the BST property.
    
    Time Complexity: O(log n) on average, O(n) in the worst case (for unbalanced tree)
    """
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root

def inorder_traversal(root: Optional[TreeNode], result: List[int]) -> None:
    """
    Performs an in-order traversal of a BST and appends the elements to the result list.
    
    Trick to remember: Perform in-order traversal (left-root-right) to get elements in sorted order.
    
    Time Complexity: O(n)
    """
    if root:
        inorder_traversal(root.left, result)
        result.append(root.val)
        inorder_traversal(root.right, result)

def bst_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers using a Binary Search Tree (BST).
    
    Trick to remember: Build a BST from the input array and perform an in-order traversal.
    
    Example usage:
        input_arr = [3, 2, 1, 5, 4]
        sorted_arr = bst_sort(input_arr)
        print("Sorted array:", sorted_arr)  # Expected output: [1, 2, 3, 4, 5]
    
    Time Complexity: O(n log n) average case, O(n^2) worst case (unbalanced BST)
    Space Complexity: O(n)
    """
    root = None
    for num in arr:
        root = insert_bst(root, num)
    
    sorted_arr = []
    inorder_traversal(root, sorted_arr)
    return sorted_arr

# Testing the function
input_arr = [3, 2, 1, 5, 4]
sorted_arr = bst_sort(input_arr)
print("Sorted array:", sorted_arr)  # Expected output: [1, 2, 3, 4, 5]
