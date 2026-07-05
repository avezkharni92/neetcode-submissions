class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} #store value and index format
        for i, v in enumerate(nums):  #But in for loop you use index and value which is reverse of above value
            diff = target - v
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[v] = i        
