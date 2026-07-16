class Solution:
    def create_freq_str(self, input_str: str)-> str:
        freq = {}
        for i in input_str:
            freq[i] =freq[i]+1 if freq.get(i) else 1
        final = "abcdefghijklmnopqrstuvwxyz"
        res = ""
        for i in final:
            res = res+i
            res = res + str(freq.get(i, 0))
        return res
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for i in strs:
            freq_str = self.create_freq_str(i)
            ans[freq_str].append(i)
        final_ans = list(ans.values())
        return final_ans

        