def intersection_arrays(arr1, arr2):
    if not arr1 or not arr2:
        return []
    
    # intersections = list({x for x in arr1 if x in arr2 }) #use set due to handle duplicate vaules
    
    intersection = set() # It handle duplicates
    for x in arr1:
        if x in arr2 and x not in intersection:
            intersection.add(x)
    
    return list(intersection)



li1 = [1,1,2,3,3,2]
li2 = [3,2,4,6,9,7]
print(intersection_arrays(li1, li2))