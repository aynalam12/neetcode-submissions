class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        size = 0
        a = set(nums)
        for n in a:
            longest = []
            if (n - 1) not in a:
                longest.append(n)
                while (n + 1) in a:
                    longest.append(n+1)
                    n += 1
                size = max(size, len(longest))
        return size
            

            

        