class Solution:
    def isPalindrome(self, s: str) -> bool:
        sNew = "".join(s.split()).lower()
        sFin = []
        for i in range(len(sNew)):
            if sNew[i].isalnum():
                sFin.append(sNew[i])
        return sFin == sFin[::-1]