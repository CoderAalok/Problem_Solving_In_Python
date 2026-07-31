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
num1, num2 = 18, 20
s = Solution()
print(s.HCF(num1, num2))


"""
Let me explain this division equation logic:
First a fall HCF stands for Highest Common Factor (means which those a number that divisible by both number).

let suppose num1 > num2 
(why num1 > num2, while HCF is same either num1 > num2 or num1 < num2 and num1 == num2 in this case remainder is 0  so our HCF is num2)

num1 > num2 -> we have two possible cases that is  if num1 % num2 == 0 (perfect divisible so num2 our HCF) or 
num1 % num2 != 0 (non-perfect divisible it gives remainder + quotient)


num1 == num2 # In this case, HCF(num1,num2) = num1 (or num2)
let me how ?
if num1 % num2 == 0 # remainder = 0 and quotient = 1
num1 % num2 = num1 - num2 * (num1 // num2) 
num1 - num2 * (num1 // num2) = 0
num1 - num2 * 1 = 0 # (num1 // num2) -> quotient = 1

Therefore, num1 = num2  # so when num1 == num2, num2 is our HCF but we could also say num1 (just flip the process means num2 % num1 instead of num1 % num2)


# perfectly divisible
num1 = num2 * quotient + remainder
now see,  if num1 and num2 are perfectly divisible then
num1 % num2 = 0 # remainder = 0 but it has a quotient (Q)
num1 = num2 * Q + 0
so this is guaranteed that num2 is our HCF with one replacement num1 = num2 and num2 = num1 % num2


# non-perfect divisible
if num1 % num2 = R
-> So we know that num1 % num2 = R it also has a quotient (Q) but in this case we not ensure that num2 has guaranteed HCF (may be it has).
so for accurate HCF we need  further operation.
if num2 -> HCF generally we can assigne (num1 = num2)  (above mention in detailed)
so num1 = num2 and num2 = num1 % num2 then we repeate this process until remainder become 0, at the end we'll get HCF

Overall, num1 = num2 * Q + R 


FOR EXAMPLEs:
(perfect divisible)
num1 = 10, num2 = 5
num1 // num2 = 2 
num2 -> HCF

Algorithmic;
num1, num2 = 5, 10 % 5 = 0
condition (FALSE)
num1 -> HCF

(non-perfect divisible)
num1 = 15, num2 = 10
num1 // num2 = 15 // 10 = 3 // 2

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