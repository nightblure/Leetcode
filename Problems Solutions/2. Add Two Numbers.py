# https://leetcode.com/problems/add-two-numbers/

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

def get_ll(values):
    head = ListNode(values[0])
    cur = head

    for value in values[1:]:
        cur.next = ListNode(value)
        cur = cur.next

    return head

arrs = [
    ([2,4,3], [5,6,4]),
    ([0], [0]),
    ([9,9,9,9,9,9,9], [9,9,9,9])
]

obj = Solution()

for data in arrs:
    a1, a2 = data[0], data[1]
    res = obj.addTwoNumbers(get_ll(a1), get_ll(a2))
    resl = []

    while res:
        resl.append(res.val)
        res = res.next
    
    print(
        f"{''.join([str(x) for x in a1])} + {''.join([str(x) for x in a2])} = {''.join([str(x) for x in resl])}"
    )
