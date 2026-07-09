class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True
    
# 3. Hash Table (Using Array)
# Intuition
# Since the problem guarantees lowercase English letters, we can use a fixed-size array of length 26 to count character frequencies instead of a hash map.
# As we iterate through both strings simultaneously, we increment the count for each character in s and decrement the count for each character in t.
# If the strings are anagrams, every increment will be matched by a corresponding decrement, and all values in the array will end at 0.
# This approach is efficient because it avoids hashing and uses constant space.

# Algorithm
# If the lengths of the strings differ, return false immediately.
# Create a frequency array count of size 26 initialized to 0.
# Iterate through both strings:
# Increment the count at the index corresponding to s[i].
# Decrement the count at the index corresponding to t[i].
# After processing both strings, scan through the count array:
# If any value is not 0, return false because the frequencies differ.
# If all values are 0, return true since the strings are anagrams.


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