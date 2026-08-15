class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i,n in enumerate(nums):
            t = target - n
            if t in h:
                return [h[t], i]
            h[n] = i
            
        return []



        