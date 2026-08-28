class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        l = 1
        r = len(nums)-1
        result = []
        for idx, i in enumerate(nums):
            if i > 0:
                break
            l=idx+1
            r=len(nums)-1
            while(l<r):
                sumOfThree = i + nums[l] + nums[r]
                if (sumOfThree == 0):
                    if([i,nums[l],nums[r]] not in result):
                        result.append([i,nums[l],nums[r]])
                    l+=1
                    r-=1
                    pass
                elif (sumOfThree > 0):
                    r-=1
                else:
                    l+=1
        return result