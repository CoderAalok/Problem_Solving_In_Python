from typing import List
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # without deletion
        # or
        # with deletion subarray could be maximum
        
        nodelete = ans = arr[0]
        delete = 0
        
        for i in range(1, len(arr)):
            # calculate sum with deletion
            delete = max(nodelete, delete + arr[i])

            # calculate sum without deletion 
            nodelete = max(arr[i], arr[i] + nodelete)
            
            # result update
            ans = max(ans, nodelete, delete)
        
        return ans
            


arr = [2,-3,4,-5]
s = Solution()
print(s.maximumSum(arr))

# DRY RUN
"""
Initialize from 0 index: nodelete = 2, ans = 2, delete = 0 # previous one deletion sum
***************************************************************************************
Iteration: 1
-----------------------------------------------
expand_prev_del_sum = (delete + arr[1]) -> 0 + (-3) -> -3  # previous one deletion sum + curr

curr_delete_sum = nodelete -> 2 # one deletion (current element deletion -> one deletion sum)

delete = max(2, -3) -> 2 # after one deletion sum


nodelete_sum = nodelete + arr[1] -> 2 - 3 -> -1

curr_element = arr[1] -> -3

nodelete = max(-3, -1) -> -1 # nodelete sum

ans = max(2, -1, 2) -> 2 # max(ans, nodelete, delete)

Iteration: 2
-----------------------------------------------
expand_prev_del_sum = (delete + arr[2]) -> 2 + 4 -> 6  # previous one deletion sum + curr

curr_delete_sum = nodelete -> -1

delete = max(-1, 6) -> 6 # after one deletion sum


nodelete_sum = nodelete + arr[2] -> -1 + 4 -> 3

curr_element = arr[2] -> 4

nodelete = max(4, 3) -> 4

ans = max(2, 6, 6) -> 6

Iteration: 3
-----------------------------------------------
expand_prev_del_sum = (delete + arr[3]) -> 6 - 5 -> 1  # previous one deletion sum + curr

curr_delete_sum = nodelete -> 4

delete = max(4, 1) -> 4 # after one deletion sum

nodelete_sum = nodelete + arr[3] -> 4 - 5 -> -1

curr_element = arr[3] -> -5

nodelete = max(-5, -1) -> -1

ans = max(6, -1, 4) -> 6

------------------------
final result: 6 
------------------------
"""


# Alternative method:
"""
First write nodeletion code and then 
write with one deletion code and do compare both of them 
then we wil get exact answer
"""
# Working flow
# ------------

                                                    # [Two Cases]
                                                    #     |
                                                    #    / \
                                #      [Without]         or           [With]
                                #    (no deletion)                 (one deletion)
                                #          |                             |
                                #         / \                           / \
                                # (prev + curr) or (curr)      (expand_prev_del_sum)  or (one deletion)
                                #       |              \              |                         \
                                # (arr[i-1] + arr[i]) or arr[i]       \                         (no deletion)
                                #                                  (delete[i-1] + arr[i])
