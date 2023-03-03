# https://leetcode.com/problems/add-two-numbers/

from utils import list_to_linked_list, list_to_str

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        mem = 0

        while l1 or l2 or mem == 1:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            sum = n1 + n2 + mem
            
            if sum >= 10:
                sum = sum % 10
                mem = 1
            else:
                mem = 0

            cur.next = ListNode(sum)
            cur = cur.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next


arrs = [
    ([2,4,3], [5,6,4]),
    ([0], [0]),
    ([9,9,9,9,9,9,9], [9,9,9,9])
]

obj = Solution()

for data in arrs:
    a1, a2 = data[0], data[1]
    res = obj.addTwoNumbers(list_to_linked_list(a1), list_to_linked_list(a2))
    resl = []

    while res:
        resl.append(res.val)
        res = res.next
    
    print(
        f"{list_to_str(a1)} + {list_to_str(a2)} = {list_to_str(resl)}"
    )
