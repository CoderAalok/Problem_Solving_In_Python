from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotate_list(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """ rotate list to the right by k places """
    """ [1|a1] -> [2|a2] -> [3|a3] -> [4|a4] -> [5|None] """
    
    if not head or not head.next:
        return head
    
    n = 1
    tail = head
    # calculate length
    while tail.next:
        tail = tail.next
        n += 1
    
    # make temporary cycle: tail -> head
    tail.next = head
    
    # find new postion of head
    k %= n
    steps = n - k # from old tail to new tail
    for _ in range(steps):
       tail = tail.next
    
    # new head
    new_head = tail.next
    tail.next = None
    
    return new_head


# create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# connecting nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

k = 3
result = rotate_list(node1, k)
ans = []
while result:
    ans.append(str(result.val))
    result = result.next

print(" -> ".join(ans))

"""
Observation is enough for this problem,
So let's visualize

# [1|a2] -> [2|a3] -> [3|a4] -> [4|a5] -> [5|None]
    |                                         |
  [head]                                    [tail]
    |
   [a1]
   
# tail -> head

# [1|a2] -> [2|a3] -> [3|a4] -> [4|a5] -> [5|a1]
    |                                        | \
    \________________________________________/  [old tail]
    
suppose, k = 3,  len = 5 - k = 2 (after (n-k) steps new head )
# [1|a2] -> [2|a3] -> [3|a4] -> [4|a5] -> [5|a1]
             /      |     \
    [new tail]   [break] [new head]   

# [4|a5] -> [5|a1] -> [1|a2] -> [2|a3] -> [3|None] 

"""

"""
Time Complexity: O(N)
Space Complexity: O(1)

"""