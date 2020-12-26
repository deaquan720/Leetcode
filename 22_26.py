class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in nums:
            i_nums = nums.count(i)
            while i_nums > 1:
                nums.remove(i)
                i_nums -= 1

