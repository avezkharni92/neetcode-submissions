class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        #for i, v in enumerate(nums):
        for v in nums:
            if v in hashset:
                return True
            hashset.add(v)
        return False

#Here Hashset is used because in set we cannot add duplicate values
#enumerate is for going through the element and value together

    
        
        