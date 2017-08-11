class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dic={};
        start=-1;
        maxL=0;
        for i in range(len(s)):
            if s[i] in dic and start<dic[s[i]]:
                start=dic[s[i]];
            else:
                maxL=max(maxL,i-start);
            dic[s[i]]=i;
        return maxL;
