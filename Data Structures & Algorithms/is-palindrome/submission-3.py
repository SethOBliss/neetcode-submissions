class Solution:
    def isPalindrome(self, s: str) -> bool:
        p= s.lower()
        k=''
        q=''
        for i in p:
            if i.isalnum():
                k=k+i
                q=i+q
        print(k,q)
        if k==q:
            return True
        return False