class Solution:
    def isPalindrome(self, s: str) -> bool:
        sFin = ''
        for i in s.lower():
            if i.isalnum():
                sFin += i
        return sFin == sFin[::-1]