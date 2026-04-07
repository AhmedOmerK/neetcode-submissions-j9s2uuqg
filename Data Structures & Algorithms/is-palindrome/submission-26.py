class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for c in s:
            if c.isalnum():        
                result += c.lower()
        i = 0
        j = len(result) - 1
        while i < j:
            if result[i] == result[j]:
                i += 1
                j -= 1
            else:
                return False
        return True