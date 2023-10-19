class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq =  {}
        for i in s:
            freq[i]=0
        curmax = 0
        maxlen = 0
        j=0
        while(j<len(s)):
            freq[s[j]]+=1
            curmax += 1
            # print(curmax)
            # print(freq,i,j)
            if freq[s[j]]>1:
                curmax=0
                j-=1
                for k in freq:
                    freq[k]=0
            maxlen = max(maxlen,curmax)
            j = j+1
        return maxlen

sol = Solution()
print(sol.lengthOfLongestSubstring('aab'))
