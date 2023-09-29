# https://leetcode.com/problems/merge-two-sorted-lists/

from utils import list_to_linked_list, ListNode, is_same_linked_lists

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        current = dummy
        n1, n2 = list1, list2

        while n1 and n2:
            num1, num2 = n1.val, n2.val

            if num1 < num2:
                current.next = ListNode(num1)
                n1 = n1.next
            else:
                current.next = ListNode(num2)
                n2 = n2.next

            current = current.next

        current.next = n1 or n2

        return dummy.next
    
tests_data = [
    ([1,2,4], [1,3,4], [1,1,2,3,4,4]),
    ([], [], []),
    ([], [0], [0]),
]
obj = Solution()

for data in tests_data:
    expected = list_to_linked_list(data[-1])
    l1 = list_to_linked_list(data[0])
    l2 = list_to_linked_list(data[1])
    assert is_same_linked_lists(expected, obj.mergeTwoLists(l1, l2))