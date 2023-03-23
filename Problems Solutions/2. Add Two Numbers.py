# https://leetcode.com/problems/add-two-numbers/

from utils import list_to_linked_list, is_same_linked_lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        add = 0

        while l1 or l2 or add:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            sum = n1 + n2 + add
            
            if sum >= 10:
                sum %= 10
                add = 1
            else:
                add = 0

            cur.next = ListNode(sum)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


arrs = [
    ([2,4,3], [5,6,4], [7,0,8]),
    ([0], [0], [0]),
    ([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1])
]

obj = Solution()

for data in arrs:
    l1, l2 = list_to_linked_list(data[0]), list_to_linked_list(data[1])
    res = obj.addTwoNumbers(l1, l2)
    assert is_same_linked_lists(res, list_to_linked_list(data[-1]))
