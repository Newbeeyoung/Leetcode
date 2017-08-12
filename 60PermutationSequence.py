class Solution(object):
    def getPermutation(self, n, k):
        s=[0,1,2,3,4,5,6,7,8,9]
        result=""
        
        for i in range(n):
            num=(k-1)/self.f(n-i-1)+1
            result+=str(s[num])
            s.pop(num)
            k=k-(num-1)*self.f(n-i-1)
        return result
    
    def f(self,n):
        if n == 0:
            return 1
        else:
            return n * self.f(n-1)

            
            
            
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        