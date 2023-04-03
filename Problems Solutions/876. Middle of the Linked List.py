# https://leetcode.com/problems/middle-of-the-linked-list/

from utils import list_to_linked_list, ListNode, is_same_linked_lists

class Solution:
    def middleNode(self, head):
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

tests_data = (
    ([1,2,3,4,5], [3,4,5]),
    ([1,2,3,4,5,6], [4,5,6])
)

obj = Solution()

for data in tests_data:
    expected = list_to_linked_list(data[-1])
    l = list_to_linked_list(data[0])
    assert is_same_linked_lists(expected, obj.middleNode(l))
