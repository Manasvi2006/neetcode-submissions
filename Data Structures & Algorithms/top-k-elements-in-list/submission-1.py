import collections
# import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create an empty list to append to for the return
        #use a hashmap to get the counts
        #
        output = []
        counts = collections.Counter(nums)

        # sortedVals = sorted(counts.values(), reverse=True)
        # sortedKeys = sorted(counts.keys(), reverse=True)
        mostCommon = counts.most_common(k)

        #i = 0
        # while i < k:
        #     output.append()
        #     i += 1
        # return output
        for i in range(k):
            output.append(mostCommon[i][0])

        return output


        

        