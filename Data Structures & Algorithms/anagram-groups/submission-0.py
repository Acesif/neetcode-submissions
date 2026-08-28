class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            mapAlpha = [0] * 26

            for i in s:
                mapAlpha[ord(i) - ord("a")] += 1
            res[tuple(mapAlpha)].append(s)

        return list(res.values())
