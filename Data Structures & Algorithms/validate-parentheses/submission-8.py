class Solution:
    def isValid(self, s: str) -> bool:
        theLen = len(s)
        leftToRight = {
            "(" : ")",
            "[" : "]",
            "{" : "}",
        }
        if theLen % 2 == 0:
            while s != "":
                if s[0] in leftToRight.keys():
                    if leftToRight[s[0]] != s[-1]:
                        if leftToRight[s[0]] != s[1]:
                            return False
                            break
                        else:
                            s = s[2::]                
                    else:
                        s = s[1:-1]
                else:
                    return False
                    break
            return True
        return False


        