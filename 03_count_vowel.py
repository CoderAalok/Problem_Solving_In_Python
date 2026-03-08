# # The problem is how many vowels occur each word.

# def count_vowels(text):
#     text = text.strip().lower()  #normalized the text
#     if text == "":
#         return None
    
#     # Pre-defined vowels
#     vowels = "aeiou"
#     count_vowels = {} #count number of vowels each words.
#     text = text.split()
    
#     for word in text:
#         count = sum(1 for w in word if w in vowels)
#         count_vowels[word] = count

#     return count_vowels

# text = "Problem solving skill most impotant for machine learning. Looping "
# print(count_vowels(text))

n = [1,2]
m = [2]
s = (len(n))
t = sum(n+m)
print(t/s)