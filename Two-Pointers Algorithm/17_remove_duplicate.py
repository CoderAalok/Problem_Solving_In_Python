# For string

def remove_duplicates(words):
    if not words:
        return []
    
    seen = set()  # for checking same at once but list cannot because of python scanning each element one by one
    count = [] # order preserved
    
    for word in words:
        if word not in seen:
            seen.add(word)
            count.append(word)
    
    return count

li = ['ball', 'cat', 'apple', 'toy', 'cat', 'ball']
print(remove_duplicates(li))