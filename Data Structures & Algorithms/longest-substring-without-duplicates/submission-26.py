class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        freq = {}
        sub = ''
        long = 0
        curr = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            while freq[s[r]] > 1:
                freq[s[left]] -= 1
                left += 1
            long = max(long, (r - left) + 1)
        return long


