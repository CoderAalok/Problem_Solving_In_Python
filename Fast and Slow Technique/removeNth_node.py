class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
from typing import Optional
def revome_Nth_node(head:Optional[LinkedList], n:int) -> Optional[LinkedList]:
    # head = [1,2,3,4,5,4,2], n = 3
    # output = [1,2,4,5]
    
    # # Brute-force
    # def built_node(nums):
    #     dummy = ListNode(0)
    #     temp = dummy
    #     for num in nums:
    #         temp.next = ListNode(num)
    #         temp = temp.next
        
    #     return dummy.next
        
    # nums = []
    # node = head
    # while node:
    #     nums.append(node.val)
    #     node = node.next
    
    # nums.pop(-n)
    # return built_node(nums)
    
    
    # Optimal solution using slow and fast technique
    # n-1 and n+1 merge them together
    dummy = ListNode(0, head)
    slow = fast = dummy
    for _ in range(n+1):
        fast = fast.next
    
    while fast:
        fast = fast.next
        slow = slow.next
    
    slow.next = slow.next.next
    
    return dummy.next
    
    
# nodes
node1 = ListNode(10)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(0)
node5 = ListNode(6)

# connecting nodes together
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

n = 5

res = (revome_Nth_node(node1, n))
ans = []
while res:
    ans.append(res.val)
    res = res.next
print(ans)