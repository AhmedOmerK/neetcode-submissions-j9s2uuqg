class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        mineven = float('inf')
        maxodd = 0
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i],0) + 1
        
        for v in freq.values():
            if v % 2 == 0:
                mineven = min(mineven, v)
            else: 
                maxodd = max(maxodd, v)
        return maxodd - mineven

        