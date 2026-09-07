class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        di = {}
        for i in nums:
            if i in di:
                return True
            else:
                di[i]=di.get(i,1)
        return False
