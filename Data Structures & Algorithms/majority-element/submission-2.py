class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        result = 0
        count = 0

        for n in nums:
            if count == 0:
                result = n

            if n == result:
                count += 1
            else:
                count -= 1
        return result
            

        # count = {}
        # result, maxCount = 0,0

        # for n in nums:
        #     count[n] = 1 + count.get(n,0)
        #     if count[n] > maxCount:
        #         result = n
        #         maxCount = count[n]
        
        # return result
        
        
        