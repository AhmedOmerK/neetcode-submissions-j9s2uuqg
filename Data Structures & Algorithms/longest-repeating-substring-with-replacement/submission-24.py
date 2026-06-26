class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m = 0
        freq = {}
        l = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1 
            maxFreq = max(freq.values())
            while (r - l + 1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
            m = max(m, r - l + 1)
        return m

    
        