class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        visited = []
        while (r>0 and l<len(numbers)):
            if r in visited:
                continue
            if numbers[l]+numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l]+numbers[r] < target:
                l+=1
            else:
                r-=1
        return []