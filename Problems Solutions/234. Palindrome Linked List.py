# https://leetcode.com/problems/palindrome-linked-list/

from utils import list_to_linked_list, ListNode, is_same_linked_lists

class Solution:
    def isPalindrome(self, head) -> bool:
        # обход эдж кейсов
        dummy = ListNode(next=head)
        slow = fast = dummy

        # поиск середины
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        def reverse(head):
            prev, cur = None, head

            while cur:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            
            return prev
        
        head2 = reverse(slow)

        while head2 and head:
            if head.val != head2.val:
                return False
            
            head = head.next
            head2 = head2.next

        return True

tests_data = [
    ([1,2,2,1], True),
    ([1,2], False),
]

obj = Solution()

for data in tests_data:
    l1 = list_to_linked_list(data[0])
    assert data[1] == obj.isPalindrome(l1)
