class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        start = 0
        end = 0
        result = 0
        for i in s:
            if i not in visited:
                visited.add(i)
                end+=1
            else:
                while (i in visited):
                    # print(start, end, visited)
                    visited.remove(s[start])
                    start+=1
                visited.add(i)
                end+=1
            result = max(result, end-start)
        return result

        