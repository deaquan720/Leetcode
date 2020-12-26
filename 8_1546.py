class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        size = len(nums)
        ret = 0
        i = 0
        while i < size:
            s = {0}
            total = 0
            while i < size:
                total += nums[i]
                if total - target in s:
                    ret += 1
                    break
                else:
                    s.add(total)
                    i += 1
            i += 1
        return ret

