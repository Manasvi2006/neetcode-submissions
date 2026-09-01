class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #initialize left = 0, right 4
        left = 0
        right = len(numbers) - 1

        while left < right:
            #currentSum = 1 + 2 = 3
            currentSum = numbers[left] + numbers[right]
            if currentSum == target:
                # [1, 2]
                return [left + 1, right + 1]
            
            #right = 1
            elif currentSum > target:
                right -= 1
            elif currentSum < target:
                left += 1
            else:
                right -= 1
                left += 1