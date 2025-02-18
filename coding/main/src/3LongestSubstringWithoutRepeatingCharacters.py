class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        def findSub(s):
            if len(s)==1:
                return 1
            tmp = []
            for i in range(0,len(s)):
                print(i)
                if s[i] not in tmp:
                    tmp.append(s[i])
                    print(tmp)
                else:
                    break
            s = s[i:]
            result = max(result,len(tmp))
            if len(s)>=1:
                findSub(s)
        findSub(s)
        return result
        
