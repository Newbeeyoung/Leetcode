class Solution(object):
    def maxArea(self, height):
        l=0;
        r=len(height)-1;
        maxA=0;
        
        while r>l:
            maxA=max(maxA,min(height[l],height[r])*(r-l));
            if height[l]>height[r]:
                r-=1;
            else:
                l+=1;
        
        return maxA;
            
        
        """
        :type height: List[int]
        :rtype: int
        """
        