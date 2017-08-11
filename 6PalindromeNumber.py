class Solution(object):
    def isPalindrome(self, x):
        
        i=0;
        if x<0:
            return False;
        else:
            while x/(10**i)!=0:
                i+=1;
            
            j=i/2;
            for count in range(j):
                if x/(10**(i-1))==x%10:
                    x=x%(10**(i-1));
                    x=x/10;
                    i=i-2;
                else:
                    return False;
                
            return True;
        """
        :type x: int
        :rtype: bool
        """
        