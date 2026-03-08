# # Return those elements which exactly match with frequency of k.
# So in this problem focueses on:
# first count frequenies of elements then match the element frequency with k frequency.

# # Method-I (Faster and more efficient) Time Complexity: O(n) and Space: O(n)

# def top_k_frequents(arr, k):
#     # Edge case
#     if not arr or len(arr) < 2 or k < 0:
#         return []
    
#     freq = {}
    
#     for x in arr:
#         if x not in freq:
#             freq[x] = 1
#         else:
#             freq[x] += 1
            
#     return [key for key, f in freq.items() if f == k]

# arr = [1,1,1,2,2,3,4,4]
# k = 2
# print(top_k_frequents(arr, k))



# # Method-II (Slightly good)
# def top_k_frequents(arr, k):
#     # Edge case
#     if not arr or len(arr) < 2 or k < 0:
#         return []
    
#     element_seen = set()
#     freq_elements = []
    
#     for x in arr:
#         if x not in element_seen:
#             freq = arr.count(x)  #count frequency (count one by one) so the time complexity O(n*2)
#             if freq == k:
#                 element_seen.add(x) #count k frequency of elements
#                 freq_elements.append(x)

#     return freq_elements

# arr = [1,1,1,2,2,3,4,4]
# k = 2
# print(top_k_frequents(arr, k))


