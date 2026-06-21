class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word={}
        p=[]
        for s in strs:
            k=(list(i for i in s))
            k.sort()
            word[tuple(k)] = []
        for s in strs:
            k=(list(i for i in s))
            k.sort()
            if tuple(k) in word.keys():
                word.get(tuple(k)).append(s)
        return(list(word.values()))
