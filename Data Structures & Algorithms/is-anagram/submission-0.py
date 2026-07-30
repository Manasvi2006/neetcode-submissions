class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        #a more optimized solution:
        return Counter(s) == Counter(t)

        
        sCount = {}
        tCount = {}

        for i in range(len(s)):
            #if this key value doesn't exist in the hashmap then the default value becomes 0
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            tCount[t[i]] = 1 + tCount.get(t[i], 0)

        return sCount == tCount


        