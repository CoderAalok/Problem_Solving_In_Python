from typing import List
def totalFactors(n: int) -> List[int]:
    factors = []
    for f in range(1, n + 1):
        if n % f == 0:
            factors.append(f)
    
    return factors
    
for i in totalFactors(12):
    print(i, end=" ")