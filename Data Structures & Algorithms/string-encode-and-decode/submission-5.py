class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in range(len(strs)):
            s += str(len(strs[i])) + "gooolsuka" + strs[i]
        return s


    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            srez = s.find("gooolsuka", i)
            length = int(s[i:srez])
            start = srez + 9
            strs.append(s[start : start + length])
            i = start + length
        return strs