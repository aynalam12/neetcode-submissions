class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = 0
        l = len(s) - 1

        while f < l:
            if(not s[f].isalnum()):
                f+=1
                continue
            if(not s[l].isalnum()):
                l-=1
                continue

            if(s[f].lower() != s[l].lower()):
                return False
            else:
                f = f+1
                l = l-1
        return True
        


        