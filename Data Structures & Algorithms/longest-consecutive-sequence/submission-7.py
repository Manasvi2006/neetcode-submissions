class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLength = 0

        for n in nums:
            #checks if n is the start of the longest sequence
            if (n-1) not in numSet:
                #thats the start so length is 1
                length = 1
                while (n+length) in numSet:
                    length += 1
                maxLength = max(length, maxLength)
        return maxLength