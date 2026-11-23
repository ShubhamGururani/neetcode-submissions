class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for i in s:
            if freq.get(i):
                freq[i]+=1
            else:
                freq[i]=1
        for i in t:
            if freq.get(i):
                freq[i]-=1
            else:
                return False
        for i in freq.keys():
            if freq[i]!=0:
                return False
        return True