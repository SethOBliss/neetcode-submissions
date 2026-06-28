class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = nums
        l.sort()
        c = 1
        d=[]
        for i in range(1,len(l)):
            if l[i]==l[i-1]:
                continue          
            if l[i]-l[i-1]==1:
                c=c+1
            else:
                d.append(c)
                c=1
        d.append(c)
        d.sort()
        print(l,len(l))
        if len(l)==0:
            return 0
        else:
            return d[-1]
        