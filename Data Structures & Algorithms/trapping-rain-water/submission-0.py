class Solution:
    def trap(self, height: List[int]) -> int:
        #unoptimized solution

        #length = 10
        length = len(height)
        # maxLeft and maxRight = [0,0,0,0,0,0,0,0,0,0]
        maxLeft = [0] * length
        maxRight = [0] * length
        result = 0

        #main logic is min(left, right) - height[i] bc if the current val is
        #greater than both it's left and right side.. we can't put any water

        #leftmost will be whatever value is in height[0] bc max(0, height[0]) 
        #is height[0]

        maxLeft[0] = height[0]

        for i in range(1,length):
            maxLeft[i] = max(maxLeft[i-1], height[i])

        maxRight[len(height)-1] = height[-1]
        for i in range(len(height)-2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i])
        
        for i in range(length):
            if min(maxLeft[i], maxRight[i]) - height[i] > 0:
                result += min(maxLeft[i], maxRight[i]) - height[i]
                
        return result
