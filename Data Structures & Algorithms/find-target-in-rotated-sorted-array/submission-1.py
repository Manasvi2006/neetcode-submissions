class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #finding a target so use binary search
        originalNums = nums.copy()
        nums.sort()
        left, right = 0, len(nums)-1
        output = 0
        while left <= right:
            middle = left + (right-left)//2
            if nums[middle] == target:
                print(nums[middle])
                return originalNums.index(target)
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1
        