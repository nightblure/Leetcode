# https://leetcode.com/problems/merge-two-sorted-lists/

from utils import list_to_linked_list, ListNode, is_same_linked_lists

class Solution:
    def mergeTwoLists(self, list1, list2):
        head = ListNode(0)
        node = head

        while list1 and list2:
            if list1.val < list2.val:
                node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                node.next = ListNode(list2.val)
                list2 = list2.next
            
            node = node.next
        
        node.next = list1 or list2
        return head.next
    
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