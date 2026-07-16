class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for i in s:
            if not freq.get(i):
                freq[i]=1
                continue
            freq[i]+=1
        print(freq)
        for i in t:
            if not freq.get(i) or freq[i]<1:
                return False
            freq[i]-=1
        print(freq)
        for i in freq.keys():
            if freq[i]!=0:
                return False
        return True
        