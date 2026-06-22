
class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math
        res=[]
        for i in range(len(nums)):
            l=nums[:i]
            l1 = math.prod(l)
            l=math.prod(nums[i+1:])
            res.append(l1*l)
        return res