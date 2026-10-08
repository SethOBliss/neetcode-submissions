
class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 not in nums:
            a =[]
            p = 1
            for i in nums:
                p =p* i
            for i in nums:
                a.append(int(p/i))
            return a
        else:
            a=[]
            l = nums[:]
            if 0 in nums:
                l.remove(0)
                if 0 in l:
                    for i in nums:
                        a.append(0)
                    return a
                else:
                    p=1
                    a=[]
                    for i in l:
                        p = p*i
                    for i in nums:
                        if i==0:
                            a.append(p)
                        else:
                            a.append(0)
                    return a

        