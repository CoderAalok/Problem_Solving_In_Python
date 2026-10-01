def partition_labels(s: str) -> list[int]:
    # calculate each character position
    end_position = {}
    for i in range(len(s)):
        end_position[s[i]] = i
    
    start = end = 0
    size = []
    # calculate part of size
    for i in range(len(s)):
        end = max(end, end_position[s[i]])
        if i == end:
            size.append(end - start + 1)
            start = i + 1
    
    return size


# test
# s = "aabbacc"
# s = "ababcbacadefegdehijhklij"
# print(partition_labels(s))


"""
Problem simply is that divide the string into as many parts as possible so that each character in at most one part (distinct part).
Each character must occur in at most one partition.
"""

"""Algorithmic: start and end always from begining of string(i.e. start = 0 and end = 0), if character end position extend then it will be update, start position will update when first part complete."""

"""DRY RUN:

s = "aabbacc"
end_position = a -> 4, b -> 3, c -> 6

start = 0, end = 0
i = 0, end = 4
i != end 

i = 1, end = 4
i != end

i = 2, end = 4
i != end

i = 3, end = 4
i != end
i = 4, end = 4
i == end, size = end - start + 1, [5]

start = i + 1, end = 4
i = 5, end = 6
i != end

i = 6, end = 6
i == end, size = end - start + 1, [5, 2]

final result: [5, 2]
"""