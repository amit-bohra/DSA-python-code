from typing import List, Optional

# Assumptions:
# - For the linked list, we'll consider a simple singly linked list structure.

# Selection Sort for a list
def selection_sort_list(arr: List[int]) -> List[int]:
    """
    Performs selection sort on a list of integers.
    
    Trick to remember: Think of finding the minimum element and swapping it.
    
    Question: Sort a list of integers in non-decreasing order.
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Selection Sort for a linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def selection_sort_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Performs selection sort on a singly linked list of integers.
    
    Trick to remember: Think of finding the minimum element and swapping it.
    
    Question: Sort a singly linked list of integers in non-decreasing order.
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    if not head or not head.next:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    
    current = dummy
    while current.next:
        min_node = current
        inner_current = current.next
        while inner_current:
            if inner_current.val < min_node.next.val:
                min_node = current
            inner_current = inner_current.next
        if min_node != current:
            temp = current.next
            current.next = min_node.next
            min_node.next = min_node.next.next
            current.next.next = temp
        current = current.next
    return dummy.next

# Testing the functions
# For selection_sort_list
input_list = [3, 2, 1, 5, 4]
print("Sorted list:", selection_sort_list(input_list))  # Expected output: [1, 2, 3, 4, 5]

# For selection_sort_linked_list
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
sorted_linked_list = selection_sort_linked_list(input_linked_list)
print("Sorted linked list:", convert_to_list(sorted_linked_list))  # Expected output: [1, 2, 3, 4, 5]
