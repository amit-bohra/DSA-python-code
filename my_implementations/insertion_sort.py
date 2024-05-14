from typing import List, Optional

# Assumptions:
# - For the linked list, we'll consider a simple singly linked list structure.

# Insertion Sort for a list
def insertion_sort_list(arr: List[int]) -> List[int]:
    """
    Performs insertion sort on a list of integers.
    
    Trick to remember: Think of sorting a hand of cards.
    
    Question: Sort a list of integers in non-decreasing order.
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Insertion Sort for a linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertion_sort_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Performs insertion sort on a singly linked list of integers.
    
    Trick to remember: Think of sorting a hand of cards.
    
    Question: Sort a singly linked list of integers in non-decreasing order.
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    if not head or not head.next:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    
    current = head.next
    last_sorted = head
    while current:
        if current.val >= last_sorted.val:
            last_sorted = last_sorted.next
        else:
            prev = dummy
            while prev.next.val < current.val:
                prev = prev.next
            last_sorted.next = current.next
            current.next = prev.next
            prev.next = current
        current = last_sorted.next
    return dummy.next

# Testing the functions
# For insertion_sort_list
input_list = [3, 2, 1, 5, 4]
print("Sorted list:", insertion_sort_list(input_list))  # Expected output: [1, 2, 3, 4, 5]

# For insertion_sort_linked_list
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
sorted_linked_list = insertion_sort_linked_list(input_linked_list)
print("Sorted linked list:", convert_to_list(sorted_linked_list))  # Expected output: [1, 2, 3, 4, 5]
