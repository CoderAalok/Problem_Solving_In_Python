from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head:Optional[ListNode]) -> ListNode:
        # L0 -> L1 -> L2 -> ... -> Ln-1 -> Ln
        # reorder: L0 -> Ln -> L1 -> Ln-1 -> L2 -> ...
        # find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # breaking middle
        second = slow.next
        slow.next = None
        
        # reversed order
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            
        # merge the nodes
        left, right = head, prev
        while right:
            temp_left = left.next
            temp_right = right.next
            left.next = right   # L0 -> Ln ....
            right.next = temp_left # L0 -> Ln -> L1 ....
            left = temp_left
            right = temp_right
            
        # output part
        result = head
        while result:
            print(result.val)
            result = result.next
        return
        
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

# connecting each node together
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

s = Solution()
s.reorderList(n1)

            
            