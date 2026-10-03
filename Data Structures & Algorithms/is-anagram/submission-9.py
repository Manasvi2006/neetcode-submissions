class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash = {}
        tHash = {}

        for char in s:
            sHash[char] = sHash.get(char,0) + 1
        
        for char in t:
            tHash[char] = tHash.get(char,0) + 1

        return sHash == tHash

        