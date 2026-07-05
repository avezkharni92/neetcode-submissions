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