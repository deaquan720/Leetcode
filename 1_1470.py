class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return sum(zip(nums[:n], nums[n:]), ())
