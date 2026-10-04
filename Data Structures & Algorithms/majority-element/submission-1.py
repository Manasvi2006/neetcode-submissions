class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        result, maxCount = 0,0

        for n in nums:
            count[n] = 1 + count.get(n,0)
            if count[n] > maxCount:
                result = n
                maxCount = count[n]
        
        return result
        
        
        