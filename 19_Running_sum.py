# Problem-II
# Running sum of digits: Also called Cumulative sum of digits

def running_sum(arr):
    if not arr:
        return []
    
    cumulative_sum = 0
    result = []
    for x in arr:
        cumulative_sum += x
        result.append(cumulative_sum)
        
    return result

arr = [1,2,3,4,5]
print(running_sum(arr))