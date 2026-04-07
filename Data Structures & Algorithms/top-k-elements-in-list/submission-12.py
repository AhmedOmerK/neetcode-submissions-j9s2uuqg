class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        great = []
        freq = {}

        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        for _ in range(k):
            max_key = max(freq, key=freq.get)
            great.append(max_key)
            del freq[max_key]

        return great


        
        

        