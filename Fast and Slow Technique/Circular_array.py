def circularArrayLoop(nums):
    # nums = [2,-1,1,2,2], index: 0 -> 2, 1 -> -1, 2 -> 1, 3 -> 2, 4 -> 2
    n = len(nums)
    def get_next(i):
        return (i + nums[i]) % n
    
    for i in range(n):
        # skip zero
        if nums[i] == 0: 
            continue
        slow = fast = i
        direction = nums[i] > 0 # forward -> True /backward -> False
        
        while True:
            # Edge case
            if (nums[slow] > 0) != direction or\
                (nums[fast] > 0) != direction:
                break
             
            # Floyd's cycle detection
            next_slow = get_next(slow)
            next_fast1 = get_next(fast)
            
            # direction validity check
            if (nums[next_slow] > 0) != direction or\
                (nums[next_fast1] > 0) != direction:
                break
            
            # twice move 
            next_fast2 = get_next(next_fast1)
            if (nums[next_fast2] > 0) != direction:
                break
            
            slow = next_slow
            fast = next_fast2
            
            if slow == fast:
                # avoid unit cycle
                if slow == get_next(slow):
                    break
                return True
            
        # pruning
        j = i
        while nums[j] != 0 and (nums[j] > 0 )== direction:
            next_j = get_next(j)
            nums[j] = 0
            j = next_j
            
    return False
        
# nums = [1,-1,2,3,-2]
nums = [2,-1,1,2,2]
# nums = [1,-1,0,1,-2]
print(circularArrayLoop(nums))