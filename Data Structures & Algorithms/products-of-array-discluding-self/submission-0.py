import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #first initialize an empty list
        res = [1] * len(nums)
        
        #initialize the prefix
        prefix = 1

        #loop through nums to add prefix products to res
        for i in range(len(nums)):
            #assign result at that index to the current prefix product
            res[i] = prefix
            prefix *= nums[i]

        #initialize postfix
        postfix = 1
        #loop backwards for postfix
        for i in range(len(nums)-1, -1, -1):
            #update the result at each index to be a product of the postfix
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
        