# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        # Step 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # cycle detected
                break
        else:
            return None  # no cycle

        # Step 2: Find cycle start
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow  # cycle start node
