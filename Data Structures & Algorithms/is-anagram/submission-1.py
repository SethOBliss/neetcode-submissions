class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        k=(list(i for i in s))
        k.sort()
        j =(list(i for i in t))
        j.sort()
        if k==j:
            return True
        return False
        