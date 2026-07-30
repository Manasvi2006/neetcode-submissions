class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #maps value to the i (index)

        for i, n in enumerate(nums): #i,n means index and number
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return