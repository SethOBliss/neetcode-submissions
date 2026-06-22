class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        k={}
        p = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                else:
                    p=p*nums[j]
            k[i] = p
            p=1
        return list(k.values())