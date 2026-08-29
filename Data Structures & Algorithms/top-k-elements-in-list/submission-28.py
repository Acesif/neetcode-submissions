class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        
        for i in nums:
            map[i] += 1

        res = map.items()
        arr = []
        gg = sorted(res, key=lambda x: x[1], reverse=True)
        nice = [i[0] for i in gg]
        
        return nice[:k]
        