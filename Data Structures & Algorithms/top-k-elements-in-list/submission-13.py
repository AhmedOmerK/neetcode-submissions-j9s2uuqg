class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = []
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0) + 1
        
        for i in range(k):
            cmp = max(freq, key=freq.get)
            arr.append(cmp)
            del freq[cmp]

        return arr
            
        