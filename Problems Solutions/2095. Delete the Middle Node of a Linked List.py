# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        # dummy нужен для обхода эдж-кейсов
        """ 
        fast изначально равен dummy.next, 
        потому что сдвинув его на 1 ноду вправо мы найдем middle - 1 ноду,
        потому что при fast = slow = head мы находим middle ноду
        """
        dummy = ListNode(next=head)
        fast, slow = dummy.next, dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next

        return dummy.next

def get_ll(values):
    head = ListNode(values[0])
    cur = head

    for value in values[1:]:
        cur.next = ListNode(value)
        cur = cur.next

    return head

arrs = [
    ([1,3,4,7,1,2,6], [1,3,4,1,2,6]),
    ([1,2,3,4], [1,2,4]),
    ([2,1], [2])
]

obj = Solution()

for data in arrs:
    l = data[0]
    res = obj.deleteMiddle(get_ll(l))
    ll = []

    while res:
        ll.append(res.val)
        res = res.next
    
    print(
        f"deleteMiddle({','.join([str(x) for x in l])}) = {''.join([str(x) for x in ll])}"
    )
