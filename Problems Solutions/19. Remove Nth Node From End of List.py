# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

from utils import list_to_linked_list, ListNode, is_same_linked_lists

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(next=head)
        fast = slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dummy.next

tests_data = [
    ([1,2,3,4,5], 2, [1,2,3,5]),
    ([1], 1, []),
    ([1,2], 1, [1])
]

obj = Solution()

for data in tests_data:
    l1 = list_to_linked_list(data[0])
    expected = list_to_linked_list(data[-1])
    assert is_same_linked_lists(obj.removeNthFromEnd(l1, data[1]), expected)