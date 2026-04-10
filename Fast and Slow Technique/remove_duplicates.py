from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeDuplicates(self, head:Optional[ListNode]) -> ListNode:
        # head: [1,1,2,2,3]
        current = head
        while current and current.next:
            if current.val == current.next.val: 
                node = current.next  
                current.next = node.next
            else:
                current = current.next
            
        return head

n1 = ListNode(1)
n2 = ListNode(1)
n3 = ListNode(2)
n4 = ListNode(2)
n5 = ListNode(3)

# connecting each node together
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

s = Solution()
next_node = s.removeDuplicates(n1)
while next_node:
    print(next_node.val)
    next_node = next_node.next

# work flow
# head:a1 -> [1|a2] -> [1|a3] -> [2|a4] -> [2|a5] -> [3|None] 

# Step 1:
# current.val = 1 , current.next.val = 1
#  n = current.next # a2   (next node address)
# current.next = n.next # a3

# Step 2:
# current.val = 1 , current.next.val = 2
# current = current.next  # [1|a3] -> [2|a4] -> [2|a5] -> [3|None]

# step 3:
# current.val = 2 , current.next.val = 2
#  n = current.next # a4   (next node address)
# current.next = n.next # a5

# Step 4:
# current.val = 2, current.next.val = 3
# current = current.next 

# Step 5:
# current.val = 3 , current.next.val = None
# while condition break

# final output: [1|a4] -> [2|a5] -> [3|None]
