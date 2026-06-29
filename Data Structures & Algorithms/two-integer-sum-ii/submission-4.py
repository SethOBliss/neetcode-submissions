class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(numbers)):
            if target-numbers[i] in numbers:
                res.append(i+1)
                res.append([d for d,x in enumerate(numbers) if x == target-numbers[i]][-1]+1)
                break
        return res
        