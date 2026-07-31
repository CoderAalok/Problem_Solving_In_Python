def LCM(a: int, b: int) -> int:
    """To calculate Least Common Multiple(LCM): Multiply a and b then divide by HCF(or GCF)."""
    # check negative
    if a < 0 or b < 0:
        return 0
        
    # calculate HCF
    x, y = a, b
    while y:
        x, y = y, x % y
    
    # calculate LCM
    lcm = (a * b) //  x # HCF(a, b) -> x
    
    return lcm

# test
a, b = 60, 90
print(LCM(a, b))