def minBoats(people, limit):
    people.sort()
    i, j = 0, len(people) - 1
    min_boats = 0
    
    while i <= j:
        carry = people[i] + people[j]
        if carry <= limit:
            i += 1
            
        min_boats += 1
        j -= 1
    
    return min_boats

people = [20,50,10,30,90,70]
limit = 90
print(minBoats(people, limit))


"""
DRY RUN:

i = 0, j = 5
carry = 20 + 70 = 90
90 <= limit (True)
min_boats = 1


i = 1, j = 4
carry = 50 + 90 = 140
140 <= limit (False)
min_boats = 2 [only one person carry by boat (from right)]


i = 1, j = 3
carry = 50 + 30 = 80
80 <= limit (True)
min_boats = 3


i = 2, j = 2
carry = 10 + 10 = 20  [here i and j meet together i.e. i == j, so only one people carry by a boat]
80 <= limit (True)
min_boats = 4


# Final result: people.sort = [10,20,30,50,70,90]
minimum boats = 4 [(90), (10, 70), (20, 50), (30)]

"""

"""
array.sort() -> O(n log n )
loop -> O(n)
Time Complexity: O(n log n ) + O(n) = O(n log n )
Space Complexity: O(n)

"""