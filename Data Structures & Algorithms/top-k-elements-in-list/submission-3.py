class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fr = {}
        for i in nums:
            fr[i] = 1+fr.get(i, 0)
        d = dict(sorted(fr.items(), key =  lambda item: item[1], reverse=True))
        print(d)
        return (list(d.keys()))[:k]