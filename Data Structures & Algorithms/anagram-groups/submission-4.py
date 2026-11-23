class Solution:
    def get_freq_str(self, s: str)-> str:
        freq_arr = [0]* 26
        for i in s:
            freq_arr[ord(i)- ord('a')]+=1
        ans = ''
        for i in range(26):
            ans+= str(str(i+ord('a'))+ str(freq_arr[i]))
        return ans

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i in strs:
            freq_str = self.get_freq_str(i)
            if ans.get(freq_str):
                ans[freq_str].append(i)
            else:
                ans[freq_str] = [i]
        ret = list(ans.values())
        return ret
        