from typing import Optional 
class LinkedNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Optimal approach
# class Solution:
    # def isPalindrome(self, head:Optional[ListNode]) -> bool:
    #     slow = fast = head
    #     # step 1: find middle
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next
        
    #     # odd case handling
    #     if fast:
    #         slow = slow.next
        
    #     # step 2: reversed order of nodes
    #     prev = None
    #     while slow:
    #         temp = slow.next # keep hold next node address
    #         slow.next = prev # current node linked new address
    #         prev = slow # preserved current node address
    #         slow = temp # move to next node
        
    #     # step 3: matching left half and right half(reversed part)
    #     left, right = head, prev
    #     # check left half and right half(reversed)
    #     while right:
    #         if left.val != right.val:
    #             return False
    #         left = left.next
    #         right = right.next
    #     return True
# Time Complexity: O(n)
# Space Complexity: O(1)

# Using stack to approch this problem
class Solution:
    def isPalindrome(self, head:Optional[ListNode]) -> bool:
        stack = []
        slow = head
        # first stores all value bottom-top
        while slow:
            stack.append(slow.val)
            slow = slow.next
        # matching top-bottom
        slow = head
        while slow:
            if slow.val != stack[-1]:
                return False
            stack.pop(-1)
            slow = slow.next
        return True
    
# nodes creates
n1 = LinkedNode(1)
n2 = LinkedNode(2)
n3 = LinkedNode(2)
n4 = LinkedNode(2)
n5 = LinkedNode(1)

# connecting nodes together
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

s = Solution()
print(s.isPalindrome(n1))