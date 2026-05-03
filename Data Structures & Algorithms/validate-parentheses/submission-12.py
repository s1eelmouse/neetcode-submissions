class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rightToLeft = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
        }
        for i in s:
            if i in rightToLeft:
                if stack and stack[-1] == rightToLeft[i]:
                    stack.pop()
                else:
                    return False
                    break
            else:
                stack.append(i)
        return not stack

        