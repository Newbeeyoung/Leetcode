class Solution(object):
    def longestPalindrome(self, s):
        o='';
        maxL=0;
        length=1;
        start=0;
        if len(s)<=1:
            return s;
        for i in range(0,len(s)-1):
                length,start=self.isPalindrome(s,i);
                if length>maxL:
                    maxL=length;
                    mark=i-start;
                    
        for i in range(maxL):
            o+=s[i+mark];
        
        return o;
                
    def isPalindrome(self,s,i):
        m=i;
        j=1;
        while m+1<len(s) and s[m]==s[m+1]:
            m+=1;
        
        while i-j>=0 and m+j+1<=len(s) and s[i-j]==s[m+j]:
            j+=1;
            
        leng=m-i+2*j-1;
        
        
        return leng,j-1;
            
        """
        :type s: str
        :rtype: str
        """
        
