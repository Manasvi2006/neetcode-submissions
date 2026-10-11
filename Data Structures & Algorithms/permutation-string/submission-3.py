class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if len(s1) > len(s2):
        #     return false

        # left = 0
        # right = len(s1) - 1
        # # left _ right
        # while right < len(s2):


        #use sort, and compare every 3 letter in a sliding window way.
        #confused on the length part? like string1 can be 4 length 3 length

        if len(s1) > len(s2):
            return False

        #can use arrays as well bc fixed values
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)  

        left = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: 
                return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1    

            index = ord(s2[left]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1    
            left += 1
        return matches == 26



            

        
        