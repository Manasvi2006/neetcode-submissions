class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        #do two pointer for every value
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue

            left, right = i+1, len(nums)-1
            while left < right:
                threeSum = n + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([n, nums[left], nums[right]])
                    #bc the duplicates happen when left and right are the same as before
                    #however just checking for left duplicates is enough
                    left += 1
                    while(nums[left] == nums[left-1] and left < right):
                        left += 1
                    
                    

        return result  

    