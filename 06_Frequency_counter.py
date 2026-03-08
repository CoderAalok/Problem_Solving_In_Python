# Problem-I: Return a dictionary of value and frequency
def frequency_counter(arr):
    if not arr:
        return {}
    
    count = {}
    for f in arr:
        if f not in count:
            count[f] = 1
        else:
            count[f] += 1
    
    return count

arr = [1,1,1,2,2,2,3,4]
print(frequency_counter(arr))

# def frequency_counter(arr):
#     if not arr:
#         return []
    
#     count = {}
#     for f in arr:
#         if f not in count:
#             count[f] = 1
#         else:
#             count[f] += 1
#     return list(count.values())

# arr = [1,1,1,2,2,2,3,4]
# print(frequency_counter(arr))
