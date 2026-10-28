
def fibonaaci(num: int):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else: 
        return fibonaaci(num - 1) + fibonaaci(num - 2)

num = int(input("Num: ").strip())
for n in range(num):
    print(fibonaaci(n), end=" ")


# DRY RUN
"""
Num = 5
-------------------
n = 0
output: 0

n = 1
output: 1

n = 2
               [2]
              /  \
            [1] + [0]  -> 1
output: 1

n = 3
               [3]
              /   \
            [2]  + [1]  -> 2
           /  \
        [1]  + [0] -> 1
output: 2

n = 4
                   [4]
               /          \
            [3]       +     [2]  ->  3
            /   \          /   \
        [2]  + [1] -> 2   [1]  +[0]  -> 1
        /  \
    [1]  + [0] -> 1

output: 3

FINAL OUTPUT: 0 1 1 2 3
"""