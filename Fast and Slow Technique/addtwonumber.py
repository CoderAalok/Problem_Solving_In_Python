class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
from typing import Optional
class Solution:
    def addTwoNumber(self, l1:Optional[ListNode], l2:Optional[ListNode]):
        # l1 = [2,3,4], l2 = [7,9,5]
        
        def listNode(res):
            temp = None
            for i in range(len(res)-1, -1, -1):
                node = ListNode(res[i])
                node.next = temp
                temp = node
            return temp
        
        dummy = ListNode(0)
        current = dummy
        n1, n2 = l1, l2
        carry = 0
        res = []
        while n1 or n2 or carry:
            val1 = n1.val if n1 else 0
            val2 = n2.val if n2 else 0
            add_num = val1 + val2 + carry
                
            # carry = add_num // 10
            # if carry:
            #     add_num %= 10 # add_num = 13 % 10 = 3, carry = 1
            
            # OR
            
            carry, add_num = divmod(add_num, 10)
            # res.append(add_num)
            
            current.next = ListNode(add_num)
            current = current.next
            
            if n1:
                n1 = n1.next
            if n2:
                n2 = n2.next
        
        # if carry:
        #     res.append(carry)
            
        # return listNode(res)
        return dummy.next

# num1 = 245
# for list1
node1 = ListNode(3)
node2 = ListNode(9)
# node3 = ListNode(2)

# connecting list1
node1.next = node2
# node2.next = node3

# num2 = 178
# for list2
n1 = ListNode(7)
# n2 = ListNode(7)
# n3 = ListNode(1)

# connecting list2
# n1.next = n2
# n2.next = n3

s = Solution()

res = s.addTwoNumber(node1, n1)
while res:
    print(res.val)
    res = res.next