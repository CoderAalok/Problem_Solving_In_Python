from typing import List
def maxCustomersSatisfied(customers: List[int], grumpy: List[int], minutes: int) -> int:
    
    # step 1: calculate those customers who are already satisfied
    n = len(customers)
    already_satisfied = 0
    for i in range(len(grumpy)):
        if grumpy[i] == 0:
            already_satisfied += customers[i]
    
    # step 2: find reset of customers who are not satisfied
    gain = [0]*n
    for i in range(len(customers)):
        gain[i] = customers[i] if grumpy[i] == 1 else 0
    
    # calculate customers when owner not grumpy for consecutive minutes
    window_customers = max_customers = 0
    for i in range(minutes):
        window_customers += gain[i]
    
    for right in range(minutes, n):
        window_customers += gain[right] - gain[right - minutes]
        max_customers = max(max_customers, window_customers)
    
    return already_satisfied + max_customers

customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3
print(maxCustomersSatisfied(customers, grumpy, minutes))


# Optimal version:
def maxSatisfied(customers: List[int], grumpy: List[int], minutes: int) -> int:
    n = len(customers)
    # step 1: calculate already satisfied customers
    satisfied =  sum(customers[i] for i in range(n) if grumpy[i] == 0) #O(n)
    
    # step 2: use technique that makes owner not grumpy
    unsatisfied = sum(customers[i] if grumpy[i] == 1 else 0 for i in range(minutes)) #O(n)
    max_customers = unsatisfied
    
    for i in range(minutes, n): # O(n)
        if grumpy[i] == 1:
            unsatisfied += customers[i]
        if grumpy[i-minutes] == 1:
            unsatisfied -= customers[i-minutes]
        
        max_customers = max(max_customers, unsatisfied)
        
    return (satisfied + max_customers)

customers = [7,3,4,5,9,1]
grumpy = [0,1,0,1,0,1]
minutes = 3

print(maxSatisfied(customers, grumpy, minutes))

"""
Explanation:
Key meanings: minutes -> length (1 <= minutes <= n)
              Consecutive minutes -> length of subarray 

According to this problem statement, return maximum no.of customers that can be statisfied
So, given integer array customers may be all satisfied, all unsatisfied or both
so the our possible answer is satisfied and extra satisfied applied techinque on unsatisfied
Now first we count all satisfied customers, then apply techinque
Actually, the technique is pretty intresting owner to remain not grumpy for consecutive mintues/length (fixed length of subarray)
so during not grumpy 'how many customers are satisfied', that exactly we calculate and then added on already satisfied
"""

"""
DRY RUN:
satisfied = [7,4,9] = 20
now apply techinque on remaining unsatified customers
unsatified = [0,3,0,5,0,1] (0 -> satisfied) 
unsatified = [0,3,0] = 3 (customers at minutes)
unsatified = [3,0,5] = 8 (customers at minutes)
unsatified = [0,5,0] = 5 (customers at minutes)
unsatified = [5,0,1] = 6 (customers at minutes)

max_customers = 8

# final answer: satisfied + max_customers = 20 + 8 = 28
"""

"""
Time Complexity: O(n)
Space Complexity: O(1)

"""