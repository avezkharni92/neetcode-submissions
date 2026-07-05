class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

'''
1. Brute Force
Intuition
We can check every pair of different elements in the array and return the first pair that sums up to the target. This is the most intuitive approach but it's not the most efficient.

Algorithm
Iterate through the array with two nested loops using indices i and j to check every pair of different elements.
If the sum of the pair equals the target, return the indices of the pair.
If no such pair is found, return an empty array.
There is guaranteed to be exactly one solution, so we will never return an empty array.
Time & Space Complexity
Time complexity: 
O(n2)
Space complexity: 
O(1)
'''
        
