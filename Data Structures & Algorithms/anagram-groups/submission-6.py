class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            sortedS = ''.join(sorted(string))
            anagrams[sortedS].append(string)
        
        return list(anagrams.values())

        
            

