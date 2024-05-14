from typing import List, Optional

# Quick Sort for a list
def quick_sort_list(arr: List[int]) -> List[int]:
    """
    Performs quick sort on a list of integers using the two-pointer approach.
    
    Trick to remember: Choose the first element as pivot and use two pointers technique.
    
    Question: Sort a list of integers in non-decreasing order.
    
    Time Complexity: O(n log n) on average, O(n^2) worst case
    Space Complexity: O(log n) on average, O(n) worst case due to recursion stack
    """
    def partition(arr: List[int], low: int, high: int) -> int:
        pivot = arr[low]
        left = low + 1
        right = high
        
        while True:
            while left <= right and arr[left] <= pivot:
                left += 1
            while left <= right and arr[right] > pivot:
                right -= 1
            
            if left > right:
                break
                
            arr[left], arr[right] = arr[right], arr[left]
        
        arr[low], arr[right] = arr[right], arr[low]
        return right
    
    def quick_sort_helper(arr: List[int], low: int, high: int) -> None:
        if low < high:
            pivot_index = partition(arr, low, high)
            quick_sort_helper(arr, low, pivot_index - 1)
            quick_sort_helper(arr, pivot_index + 1, high)
    
    quick_sort_helper(arr, 0, len(arr) - 1)
    return arr

# Quick Sort for a linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def quick_sort_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Performs quick sort on a singly linked list of integers using the two-pointer approach.
    
    Trick to remember: Choose the first element as pivot and use two pointers technique.
    
    Question: Sort a singly linked list of integers in non-decreasing order.
    
    Time Complexity: O(n^2) worst case, O(n log n) average case
    Space Complexity: O(log n) on average, O(n) worst case due to recursion stack
    """
    def partition(head: ListNode, end: ListNode) -> ListNode:
        pivot = head.val
        left_dummy = ListNode()
        right_dummy = ListNode()
        equal_dummy = ListNode()
        left_tail = left_dummy
        right_tail = right_dummy
        equal_tail = equal_dummy
        
        current = head
        while current != end:
            if current.val < pivot:
                left_tail.next = current
                left_tail = left_tail.next
            elif current.val > pivot:
                right_tail.next = current
                right_tail = right_tail.next
            else:
                equal_tail.next = current
                equal_tail = equal_tail.next
            current = current.next
        
        left_tail.next = None
        right_tail.next = None
        equal_tail.next = None
        
        left_sorted = quick_sort_linked_list(left_dummy.next)
        right_sorted = quick_sort_linked_list(right_dummy.next)
        
        left_tail.next = equal_dummy.next
        equal_tail.next = right_sorted
        
        return left_sorted if left_sorted else left_dummy.next
    
    def quick_sort_helper(head: ListNode, end: ListNode) -> ListNode:
        if head != end:
            pivot_node = partition(head, end)
            quick_sort_helper(head, pivot_node)
            while pivot_node.next:
                pivot_node = pivot_node.next
            quick_sort_helper(pivot_node.next, end)
        return head
    
    return quick_sort_helper(head, None)

# Testing the functions
# For quick_sort_list
input_list = [3, 2, 1, 5, 4]
print("Sorted list:", quick_sort_list(input_list))  # Expected output: [1, 2, 3, 4, 5]

# For quick_sort_linked_list
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
sorted_linked_list = quick_sort_linked_list(input_linked_list)
print("Sorted linked list:", convert_to_list(sorted_linked_list))  # Expected output: [1, 2, 3, 4, 5]
