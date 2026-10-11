class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #given string s which has ONLY uppercase english characters
        #k is integer

        #can choose up to k characters and replace with any other uppercase 
        #in s

        #after performing at most k replacements return length of longest
        #substring that contains only ONE distinct char

        #so go through string, and need to replace with one of the characters in the string.

        count = {}
        result = 0

        left = 0 #only need to define left pointer
        for right in range(len(s)):
            #increment counts for the character at position right
            count[s[right]] = 1 + count.get(s[right], 0)
            while(right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1 #decrement count bc not in window anymore
                left += 1
            result = max(result, right - left + 1)
        return result

        