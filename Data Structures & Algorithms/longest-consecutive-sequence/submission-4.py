class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        size = 0
        a = set(nums)
        for n in a:
            longest = 0
            if (n - 1) not in a:
                longest = 1
                while (longest + n) in a:
                    longest += 1
                size = max(size, (longest))
        return size
            

            

        