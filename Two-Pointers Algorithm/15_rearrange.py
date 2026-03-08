def rearrange_arrary(arr):
    if not arr:
        return []
    
    left = 0
    right = len(arr)-1
    
    while (left < right):
        if arr[left] == 1 and arr[right] == 0:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1

        elif arr[left] == 0 and arr[right] == 0:
            left += 1
        elif arr[left] == 1 and arr[right] == 1:
            right -= 1
        
        else:
            left += 1
            right -= 1
    
    return arr

print(rearrange_arrary([0,1,0,1,0,1]))
            


