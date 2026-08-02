class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #finding a target so use binary search
        left, right = 0, len(nums)-1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            #now check where the rotation split could've been
            if nums[left] <= nums[middle]: #means left to middle are INCREASING
                #checking highest and lowest bounds to see if TARGET is in the range of left - middle. So if it is then thats the else. the main if condition is if target is DEF not in range
                if target < nums[left] or target > nums[middle]:
                    left = middle + 1
                #this means its in range!
                else:
                    right = middle - 1
            else:
                #checking is in range of middle - highest bounds if its not then make the bounds smaller by making highest be like this -> low high middle
                if target > nums[right] or target < nums[middle]:
                    right = middle - 1
                #this means its in range!
                else:
                    left = middle + 1
        #-1 means it doesnt exist
        return -1
        