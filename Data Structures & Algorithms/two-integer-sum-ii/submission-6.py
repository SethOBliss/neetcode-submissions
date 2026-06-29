class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(numbers)):
            if target-numbers[i] in numbers:
                res.append(i+1)
                res.append(len(numbers)-(numbers[::-1]).index(target-numbers[i]))
                break
        return res
        