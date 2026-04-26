class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        goyda = {}
        for i in nums:
            goyda[i] = goyda.get(i, 0) + 1
        revList = sorted(list(goyda.items()), key=lambda x: x[1], reverse=True)[:k]
        return [x[0] for x in revList]