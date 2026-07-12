class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        
        for i in freq:
            if freq[i] == 1:
                res.append(i)
        return res
        