# Programming
# Question
"""
✅ Right Triangle Star Pattern

n = 5

*
**
***
****
*****
"""
"""
# Ans-

n = 5
store = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        store = i * '*'
    print(store)
"""
"""
✅ Palidrome of String

i / p = naman, nitin, level
o / p = true
i / p = pramod
o / p = false
"""

# ans

store = ""
pal = input("enter any word: ")

# for my_list in pal:
#     store = store + my_list
#     print(f"{my_list}", end=" ")
# print("\nThis is a normal", store)

new_pal = list(pal)
print("This is the normal string =", new_pal)

rev_list = reversed(new_pal)
for rev in rev_list:
    store = store + rev

new_store = list(store)
print("This is the reversed string =", new_store)


if new_pal == new_store:
    print("True")
else:
    print("false")

"""
✅ String Reverse 3 - 4 ways to do this in Python

✅ Count vowels and consonants in a String

✅ Anagrams

String
s1 = "silent";

String
s2 = "listen";

namo - mano - onam

An anagram is a word or phrase formed by rearranging the letters of a different
word or phrase
"""
