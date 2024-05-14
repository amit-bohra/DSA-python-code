from typing import List, Optional

# Assumptions:
# - For the linked list, we'll consider a simple singly linked list structure.

# Bubble Sort for a list
def bubble_sort_list(arr: List[int]) -> List[int]:
    """
    Performs bubble sort on a list of integers.
    
    Trick to remember: Imagine bubbles rising to the surface.
    
    Question: Sort a list of integers in non-decreasing order.
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Bubble Sort for a linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def bubble_sort_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Performs bubble sort on a singly linked list of integers.
    
    Trick to remember: Imagine bubbles rising to the surface.
    
    Question: Sort a singly linked list of integers in non-decreasing order.
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    if not head or not head.next:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    
    swapped = True
    while swapped:
        swapped = False
        prev = dummy
        current = dummy.next
        while current and current.next:
            if current.val > current.next.val:
                prev.next = current.next
                current.next = current.next.next
                prev.next.next = current
                swapped = True
            prev = prev.next
            current = current.next
    return dummy.next

# Testing the functions
# For bubble_sort_list
input_list = [3, 2, 1, 5, 4]
print("Sorted list:", bubble_sort_list(input_list))  # Expected output: [1, 2, 3, 4, 5]

# For bubble_sort_linked_list
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
sorted_linked_list = bubble_sort_linked_list(input_linked_list)
print("Sorted linked list:", convert_to_list(sorted_linked_list))  # Expected output: [1, 2, 3, 4, 5]
