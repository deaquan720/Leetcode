class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans,best = nums[0],nums[0:1]   #ans:全局最大解；best:连乘至当前最右端的最大正和最小负的列表。
        for a in nums[1:]:
            best=sorted([a]+[b*a for b in best])[::len(best)]    #放弃前面所有连乘只取a，以及前面的最大和最小结果都乘a。排序后只取首末两个元素。
            ans=max(ans,best[-1])    #ans是全局历史最大乘积，要用当前最大乘积best[0]更新。
        return ans