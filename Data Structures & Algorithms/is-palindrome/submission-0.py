class Solution:
    def isPalindrome(self, s: str) -> bool:
        p= s.lower()
        k=''
        for i in p:
            if i.isalnum():
                k=i+k
        if k[::-1]==k:
            return True
        return False