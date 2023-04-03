# https://leetcode.com/problems/linked-list-cycle/

from utils import list_to_linked_list, ListNode, is_same_linked_lists

class Solution:
    def hasCycle(self, head) -> bool:
        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, dummy.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False