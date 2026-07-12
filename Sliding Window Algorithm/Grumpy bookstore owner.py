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