class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
from typing import Optional
class Solution:
    def addTwoNumber(self, l1:Optional[ListNode], l2:Optional[ListNode]):
        # sample: l1 = [2,3,4], l2 = [7,9,8], num1 = 432 and num2 = 897, sum = 1329
        
        def listNode(res):
            temp = None
            for i in range(len(res)-1, -1, -1):
                node = ListNode(res[i])
                node.next = temp
                temp = node
            return temp
        
        # # Approach - I Using extra space 
        # n1, n2 = l1, l2
        # carry = 0
        # res = []
        # while n1 or n2:
        #     val1 = n1.val if n1 else 0
        #     val2 = n2.val if n2 else 0
        #     add_num = val1 + val2 + carry
            
        #     # carry = add_num // 10
        #     # if carry:
        #     #     add_num %= 10 # add_num = 13 % 10 = 3, carry = 1
            
        #     # OR
        #     carry, add_num = divmod(add_num, 10)
        #     res.append(add_num) # [9,2,3]
            
        #     if n1:
        #         n1 = n1.next
        #     if n2:
        #         n2 = n2.next
                
        # if carry:
        #     res.append(carry) # [9,2,3,1]
            
        # return listNode(res)
        
        # Approach - II (Using dummy node, this make convenient for Linked List problem)
        # head
        dummy = ListNode(0)
        current = dummy
        n1, n2 = l1, l2
        carry = 0

        while n1 or n2 or carry:
            val1 = n1.val if n1 else 0
            val2 = n2.val if n2 else 0
            add_num = val1 + val2 + carry
                
            carry, add_num = divmod(add_num, 10)
            current.next = ListNode(add_num)
            current = current.next
            
            if n1:
                n1 = n1.next
            if n2:
                n2 = n2.next
        
        return dummy
        
# Output
# num1 = 293
# for list1
node1 = ListNode(1)
node2 = ListNode(9)
node3 = ListNode(0)

# connecting list1
node1.next = node2
node2.next = node3

# num2 = 177
# for list2
n1 = ListNode(7)
n2 = ListNode(7)
# n3 = ListNode(1)

# connecting list2
n1.next = n2
# n2.next = n3

# sum = 293 + 177 = 470
s = Solution()

res = s.addTwoNumber(node1, n1)
ans = ""
while res:
    ans += str(res.val)
    res = res.next

print(int(ans[::-1]))