class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #initiate a hashmap (dict)
        for key in nums:
            count[key] = 1 + count.get(key, 0) #get function get the value  of dictionary key Key

        arr = [] #initiate an array with list of key and its corresponding cnt to traverse together
        for key, cnt in count.items(): #we need array because we cannot sort dictionary as it is not in order and also keep cnt as first as we need to sort them based on value
                                    # count.items return key - value pair
            arr.append([cnt, key]) # arr[[cnt, key]] #note inside bracket we have [] inside that key and value because append takes only 1 value
        arr.sort() #sorting function works lexographically.. usually 0th index if both are equal then 1st index

        res = []
        while len(res) < k: #as we keep poping the len of  result array increases by 1
            res.append(arr.pop()[1]) # arr.pop() return the key value pair and [1] give the first index value
        return res
             



        