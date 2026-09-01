class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        currMax = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            currMax = max(currMax, right - left + 1)
        return currMax

        # currMax = 0
        # count = 1

        # left, right = 0, 1

        # while right < len(s):
        #     if s[right] == s[left]:
        #         currMax = max(currMax, count)
        #         count = 1
        #         left = right
        #     else:
        #         count += 1
        #     right += 1

        # return currMax
