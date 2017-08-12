class Solution(object):
    def generateMatrix(self, n):
        matrix=[[ 0 for i in range(n)] for j in range(n)]
        nums=1
        for s in range(n/2):
            nums=self.sub(n,s,nums,matrix)
    
        if n%2==1:
            matrix[n/2][n/2]=n*n
        return matrix
        
    def sub(self,n,s,nums,matrix):
        for i in range(n-2*s-1):
            matrix[s][s+i]=nums
            nums+=1
        for i in range(n-2*s-1):
            matrix[s+i][n-s-1]=nums
            nums+=1
        for i in range(n-2*s-1):
            matrix[n-s-1][n-s-1-i]=nums
            nums+=1
        for i in range(n-2*s-1):
            matrix[n-s-1-i][s]=nums
            nums+=1
        return nums
        """
        :type n: int
        :rtype: List[List[int]]
        """
        