# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

from utils import list_to_linked_list, ListNode, is_same_linked_lists

class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        # dummy нужен для обхода эдж-кейсов
        """ 
        fast изначально равен dummy.next, 
        потому что сдвинув его на 1 ноду вправо мы найдем middle - 1 ноду,
        потому что при fast = slow = head мы находим middle ноду
        """
        dummy = ListNode(next=head)
        slow, fast = dummy, dummy.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next
        return dummy.next

tests_data = [
    ([1,3,4,7,1,2,6], [1,3,4,1,2,6]),
    ([1,2,3,4], [1,2,4]),
    ([2,1], [2])
]

obj = Solution()

for data in tests_data:
    l1 = list_to_linked_list(data[0])
    l2 = list_to_linked_list(data[1])
    assert is_same_linked_lists(obj.deleteMiddle(l1), l2)
