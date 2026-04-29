class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in range(len(strs)):
            s += str(len(strs[i])) + "#" + strs[i]
        return s


    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            srez = s.find('#', i)
            lenght = int(s[i:srez])
            start= srez + 1
            strs.append(s[start: start + lenght])
            i = start + lenght
        return strs
        