class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differencesMap = {} #adds number to their index

        for i, num in enumerate(nums):
            difference = target - num
            if difference in differencesMap:
                return [differencesMap[difference], i]
            else:
                differencesMap[num] = i
        return 0


    