class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        right = 0

        currMax = 0

        while right < len(s):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            
            charSet.add(s[right])
            currMax = max(right - left + 1, currMax)
            right += 1
        return currMax


