class Solution:

    def encode(self, strs: List[str]) -> str:
        k=""
        for i in strs:
            k= k+"9nwfunf3949f38f9n9"+i
        return k



    def decode(self, s: str) -> List[str]:
        res = []
        for i in s.split("9nwfunf3949f38f9n9"):
            res.append(i)
        return res[1:]

