class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sortedNums = sorted(nums)
        print(sortedNums)
        prev = sortedNums[0]
        count = 1
        maxVal = 0
        for num in sortedNums:
            if num == prev + 1:
                prev = num
                count += 1
            elif num == prev:
                prev = num
                continue
            else:
                if count > maxVal:
                    maxVal = count
                count = 1
                prev = num
        
        return max(maxVal,count)