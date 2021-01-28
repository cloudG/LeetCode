"""
链接：https://leetcode-cn.com/problems/running-sum-of-1d-array
给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。
请返回 nums 的动态和。

示例1：
输入：nums = [1,2,3,4]
输出：[1,3,6,10]
解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。

示例2：
输入：nums = [1,1,1,1,1]
输出：[1,2,3,4,5]
解释：动态和计算过程为 [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1] 。

示例3：
输入：nums = [3,1,2,10,1]
输出：[3,4,6,16,17]
"""
from typing import List


def runningSum(nums: List[int]) -> List[int]:
    if not nums:
        return []
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i - 1]
    return nums
