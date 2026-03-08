# Method-I: For vertical scanning

def longest_prefix(arr):
    longestPrefix = ""

    for prefix in arr[0]:
        prefix = longestPrefix + prefix
        check = True
        
        for word in arr:
            if not word.startswith(prefix):
                check = False
                break
        if check:
            longestPrefix = prefix
        else:
            break
    return longestPrefix
print(longest_prefix(['flower','flower','flower']))