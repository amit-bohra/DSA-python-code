from typing import List, Optional

# Assumptions:
# - For the linked list, we'll consider a simple singly linked list structure.

# Merge Sort for a list
def merge_sort_list(arr: List[int]) -> List[int]:
    """
    Performs merge sort on a list of integers.
    
    Trick to remember: Think of dividing the list into halves and merging sorted halves.
    
    Question: Sort a list of integers in non-decreasing order.
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort_list(left_half)
    right_half = merge_sort_list(right_half)
    
    return merge_lists(left_half, right_half)

# Merge Sort for a linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sort_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Performs merge sort on a singly linked list of integers.
    
    Trick to remember: Think of dividing the list into halves and merging sorted halves.
    
    Question: Sort a singly linked list of integers in non-decreasing order.
    
    Time Complexity: O(n log n)
    Space Complexity: O(log n) due to recursion stack
    """
    if not head or not head.next:
        return head
    
    slow = head
    fast = head.next
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    mid = slow.next
    slow.next = None
    
    left_half = merge_sort_linked_list(head)
    right_half = merge_sort_linked_list(mid)
    
    return merge_lists_linked_list(left_half, right_half)

# Merge function for lists
def merge_lists(left: List[int], right: List[int]) -> List[int]:
    """
    Merges two sorted lists into one sorted list.
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Merge function for linked lists
def merge_lists_linked_list(left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merges two sorted linked lists into one sorted linked list.
    """
    dummy = ListNode()
    current = dummy
    while left and right:
        if left.val < right.val:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next
    current.next = left if left else right
    return dummy.next

# Testing the functions
# For merge_sort_list
input_list = [3, 2, 1, 5, 4]
print("Sorted list:", merge_sort_list(input_list))  # Expected output: [1, 2, 3, 4, 5]

# For merge_sort_linked_list
# Helper function to convert list to linked list
def convert_to_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert linked list to list
def convert_to_list(head):
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr

input_linked_list = convert_to_linked_list([3, 2, 1, 5, 4])
sorted_linked_list = merge_sort_linked_list(input_linked_list)
print("Sorted linked list:", convert_to_list(sorted_linked_list))  # Expected output: [1, 2, 3, 4, 5]
