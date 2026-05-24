from typing import Optional,List
class LinkedList:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

def detect_cycle_begins(head:Optional[LinkedList])-> Optional[LinkedList]:
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next #O(n)
        fast = fast.next.next #O(2n)
        # cycle detection
        if slow == fast:
            slow = head #resetting slow
            # slow -> moves linealy to reaches at entry point ofcycle
            # fast -> moves inside the looped
            # at the time both meets again at entry point
            while slow != fast: # O(n)
                slow = slow.next
                fast = fast.next
            return slow
        
    return None


# creating nodes
node1 = LinkedList(3)
node2 = LinkedList(2)
node3 = LinkedList(-1)
node4 = LinkedList(0)
node5 = LinkedList(4)

# connecting node together 
# node1 has store memory address of node2, node2 store node3 and so on
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3

res = detect_cycle_begins(node1)
for _ in range(4):
    print(res.val)
    res = res.next


