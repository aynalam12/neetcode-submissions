class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)- 1
        h = 0

        while r > l:
            h = nums[r] + nums[l]
            if h > target:
                r -= 1
            elif h < target:
                l += 1
            elif h == target:
                return [l+1,r+1]

        return []