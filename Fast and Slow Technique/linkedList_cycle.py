from typing import Optional,List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def hasCycle(self, head: Optional[ListNode])->bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False

# these all are contains a container itself
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(-1)
node4 = ListNode(0)

#connecting each node together
# [node1] -> [node2] -> [node3] -> [node4] -> [node3]l
node1.next = node2
node2.next = node2
node3.next = node4
node4.next = node3

s = Solution()
print(s.hasCycle(node1))
# print(s.hasCycle(node2))
# print(s.hasCycle(node3))
# print(s.hasCycle(node4)) 

