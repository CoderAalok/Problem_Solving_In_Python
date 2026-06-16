"""
In this problem we are find square root of x ( x >= 0).

How can think to solve this problem?
we are find square root of x ( x >= 0) right so here
y = sqrt(x)
or y*y = x
or y = x / y

for eg;
x = 9 (has perfect square of 3)
[ 3*3 = 9 ]  or [ 3 = 9 / 3 ]
    |
[ (4-1)*(4-1) = 9 ] 

- but problem comes if x non-perfect square, so in this case we take closest value
for eg;
x = 20 (non-perfect square)
- in general we know that sqrt of 16 is 4
- here also 20 has closest sqrt is 4

- but how can we get this
- either perfect or non-perfect square root
- the value always come under its range (0, x).
- so here applied linear approach

5*5 == 20 (No)
4*4 == 20 (Yes) sqrt of x rounded it, it become 4

so, y*y <= x                or y <= x / y
so if y*y > x               or y > x / y
        |                          |
(y-1)*(y-1) <= x           (y-1) <= x / (y-1)

so, our answer that is sqrt of x (either perfect or non-perfect)
-> (y-1)
--------------------------------------------------------------------------------------------

And other hand we also think like this
x(input) |  y(output)
-------- | ----------
    0            0
    1            1
    4            2
    9            3
    .            .
    .            .
    .            .
    x            y
    
Here observe that both x and y are sorted order
so here we can think about Binary Search ( because Binary Search apply on sorted input)
and this is quite efficient than linear approch.

"""
# Solution-I (Linear search)
# def mySqrt(x:int)-> int:
#     # edge case
#     if x < 2: # [0, 1]
#         return x
    
#     for y in range(2, x+1):
#         # if y*y > x:
#         #     return (y-1)
#         # or
#         if y > x // y:
#             return (y-1)


# Solution-II (Binary Search)
def mySqrt(x:int)-> int:
    # edge case
    if x < 2: #[0, 1]
        return x
    
    low, high = 0, x
    while low <= high:
        mid = (low + high) // 2
        y = mid
        if y == x // y:
            return y
        elif y > x // y:
            high = y - 1
        else:
            low = y + 1

    return high

# test
print(mySqrt(20))
print(mySqrt(81))

# DRY Run
"""x = 12
low = 0, high = 12
mid = (0 + 12) // 2 = 6
6 == 12 // 6 = 2 (No)
6 > 2 (Yes)
high = 6-1 = 5

low = 0, high = 5
mid = (0 + 5) // 2 = 2
2 == 12 // 2 = 6 (No)
2 < 6 (Yes)
low = 2+1 = 3

low = 3, high = 5
mid = (3 + 5) // 2 = 4
4 == 12 // 4 = 3 (No)
4 > 3 (Yes)
high = 4-1 = 3

low = 3, high = 3
mid = (3 + 3) // 2 = 3
3 == 12 // 3 = 4 (No)
3 < 4 (Yes)
low = 3+1 = 4

low = 4, high = 3
low <= high (No)

sqrt(12) ~= 3
return high # this is our answer

"""
