class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    dummy = ListNode(0, head)  # 0 -> head
    prev = dummy # prev pointer always pointing to next node/pair
    
    while prev.next and prev.next.next: # check a full pair nodes exit before swap
        first = prev.next
        second = first.next
        
        prev.next = second 
        first.next = second.next # first node linked to third node
        second.next = first # swap pair
        
        # move to next node/pair
        prev = first
        
    return dummy.next # skip 0


# create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# connecting nodes and create head
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


swap_res = swapPairs(node1)
ans = ""
while swap_res:
    ans += str(swap_res.val)
    swap_res = swap_res.next

print("-> ".join(ans))


"""
DRY RUN:
head = [1,2,3,4,5]
NOTE: before we swap first we linked first_node to third_node (to keep hold future record)

dummy = 0 -> 1 -> 2 -> 3 -> 4 -> 5
prev = dummy

first = prev.next => 1 -> 2 -> 3 -> 4 -> 5
second = first.next => 2 -> 3 -> 4 -> 5

prev.next = second  => 0 -> 2 -> 3 -> 4 -> 5  # update in  dummy 
first.next = second.next => 1 -> 3 -> 4 -> 5 # first linked to third node
second.next = first => 2 -> 1 -> 3 -> 4 -> 5 # swaped

prev = first => 1 -> 3 -> 4 -> 5  # move to next node/pair of head


first = prev.next => 3 -> 4 -> 5
second = first.next => 4 -> 5

prev.next = second  => 0 -> 2 -> 1 -> 3 -> 4 -> 5  # pointing to next node (second node)
first.next = second.next => 3 -> 5 # first linked to third node
second.next = first => 2 -> 1 -> 4 -> 3 -> 5 # swaped

prev = first => 3 -> 5  # move to next node/pair of head

# prev.next and prev.next.next (False)

final result:
dummy.next = 2 -> 1 -> 4 -> 3 -> 5 

# NOTE: All pointers are internally updates and changes in dummy  

""" 