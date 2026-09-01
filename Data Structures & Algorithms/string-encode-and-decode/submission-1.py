class Solution:

    def encode(self, strs: List[str]) -> str:
        #want to use len of the current string and # as the delimeters
        #so that we know we have to only get length amount of characters starting from pound in decode

        #make a string to append allll the strings to
        res = ""
        for s in strs:
            #we want to add the length of s, a pound, then the string itself
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        #now we want to return an array and keep track of where the prefix starts
        res = []
        prefixStart = 0

        #we need to iterate character by character to get prefix
        while prefixStart < len(s):
            #now we need to keep track of where the pound is
            pound = prefixStart
            #so while pound is not equal to pount keep going up by one so it stops at the index pound is at.
            while s[pound] != "#":
                pound += 1
            #now we know that the length is from prefixStart to pound
            length = int(s[prefixStart:pound])
            #we need to append the characters from pound + 1 to that length
            res.append(s[pound + 1: pound + 1 + length])

            #then make prefixStart to 1 + the length of where the current pound is at
            prefixStart = pound + 1 + length
        return res
