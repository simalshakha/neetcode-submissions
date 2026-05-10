class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum=0
        left=0
        m=set()
        count=0
        for right in range(len(s)): 
            while s[right] in m:
                m.remove(s[left])
                left+=1
            if right-left+1>maximum:
                maximum=right-left+1
            m.add(s[right])
        return maximum
