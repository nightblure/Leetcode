# https://leetcode.com/problems/remove-linked-list-elements/

from utils import list_to_linked_list, ListNode, is_same_linked_lists

class Solution:
    def removeElements(self, head, val: int):
        dummy = ListNode(next=head)
        node = dummy

        while node and node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next

        return dummy.next

tests_data = [
    ([1,2,6,3,4,5,6], 6, [1,2,3,4,5]),
    ([], 1, []),
    ([7,7,7,7], 7, [])
]

obj = Solution()

for data in tests_data:
    l1 = list_to_linked_list(data[0])
    expected = list_to_linked_list(data[-1])
    assert is_same_linked_lists(expected, obj.removeElements(l1, data[1]))
