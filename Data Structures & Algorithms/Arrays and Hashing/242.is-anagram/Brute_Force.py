class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t) #sorted can be used in return only
    
# 1. Sorting
# Intuition
# If two strings are anagrams, they must contain exactly the same characters with the same frequencies.
# By sorting both strings, all characters will be arranged in a consistent order.
# If the two sorted strings are identical, then every character and its count match, which means the strings are anagrams.

# Algorithm
# If the lengths of the two strings differ, return false immediately because they cannot be anagrams.
# Sort both strings.
# Compare the sorted versions of the strings:
# If they are equal, return true.
# Otherwise, return false.

# Time & Space Complexity
# Time complexity: 
# O
# (
# n
# log
# ⁡
# n
# +
# m
# log
# ⁡
# m
# )
# O(nlogn+mlogm)
# Space complexity: 
# O
# (
# 1
# )
# O(1) or 
# O
# (
# n
# +
# m
# )
# O(n+m) depending on the sorting algorithm.
        