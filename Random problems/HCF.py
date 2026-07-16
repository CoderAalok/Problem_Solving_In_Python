# Fine for smaller numbers (but it slow if larger numbers)
def HCF(num1: int, num2: int) -> int:
    if num1 < 1 or num2 < 1:
        return 0 # no HCF
    
    hcf = x = 1
    while x <= num1 and x <= num2:
        if num1 % x == 0 and num2 % x == 0:
            hcf = x
        x += 1
    return hcf
    

# much faster than first one
class Solution:
    def HCF(self, num1: int, num2: int) -> int:
        if num1 < 1 or num2 < 1:
            return 0 # no HCF
        
        while num2:
            num1, num2 = num2, num1 % num2
        # return HCF
        return num1

# only positive integers
num1, num2 = 36, 2
s = Solution()
print(s.HCF(num1, num2))


"""
Let me explain you;
First a fall HCF stands for Highest Common Factor (means which one factor that divisible by both number).

let suppose num1 > num2 
(why num1 > num2, while HCF is same either num1 > num2 or num2 > num1 and num1 == num2 in this case remainder is 0  so our HCF is num2)

num1 > num2 -> we have two possible cases that is  if num1 % num2 == 0 (perfect divisible so num2 our HCF) or num1 % num2 != 0 (non-perfect divisible it gives remainder)

and one more thing, 

num1 = num2 * quotient + remainder
now see  if num1 % num2 == 0
num1 = num2 * quotient + 0
so this is guranteed that num2 is factor of num1 (i.e. num2 is our HCF)

As we can see if num1 % num2 == 0 (in this case num2 is our HCF)
but if num1 % num2 != 0
in this case also num2 is our HCF repeadtly replacing (num1, num2) with (num2, remainder) until num2 become 0
num1 replace with num2 and num2 replace with its remainder 

FOR EXAMPLE:
(perfect divisible)
num1 = 10, num2 = 5
num1 / num2 = 2 
num2 -> HCF

Algorithmic;
num1, num2 = 5, 10 % 5 = 0
condition (FALSE)
num1 -> HCF

(non-perfect divisible)
num1 = 15, num2 = 10
num1 / num2 = 15 / 10 = 3 / 2

Algorithmic;
num1, num2 = 10, 15 % 10 = 5
num1, num2 = 5, 10 % 5 = 0
condition (FALSE)
num1 -> HCF

"""

"""
Time Complexity : log (min(num1, num2))
Space Compexity : O(1)
"""