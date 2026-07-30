class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setNums = set(nums)
        return not (len(setNums) == len(nums))
        