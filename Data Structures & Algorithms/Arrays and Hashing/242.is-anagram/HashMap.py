class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        #here we are using hashmap
        #initiate the empty hashmap/dictionary for both the strings
        countS, countT = {}, {}
        #use the get function of dictionary to give a value of a key
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) #get function check for the value of a key in dictionary. here key is the character
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

# 2. Hash Map
# Intuition
# If two strings are anagrams, they must use the same characters with the same frequencies.
# Instead of sorting, we can count how many times each character appears in both strings.
# By using two hash maps (or dictionaries), we track the frequency of every character in each string.
# If both frequency maps match exactly, then the strings contain the same characters with same frequencies, meaning they are anagrams.

# Algorithm
# If the two strings have different lengths, return false immediately.
# Create two hash maps to store character frequencies for each string.
# Iterate through both strings at the same time:
# Increase the character count for s[i] in the first map.
# Increase the character count for t[i] in the second map.
# After building both maps, compare them:
# If the maps are equal, return true.
# Otherwise, return false.

# Time & Space Complexity
# Time complexity: 
# O
# (
# n
# +
# m
# )
# O(n+m)
# Space complexity: 
# O
# (
# 1
# )
# O(1) since we have at most 
# 26
# 26 different characters.
# Where 
# n
# n is the length of string 
# s
# s and 
# m
# m is the length of string 
# t
# t.