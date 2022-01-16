#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (29.18%)
# Likes:    15246
# Dislikes: 1473
# Total Accepted:    1.7M
# Total Submissions: 5.6M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
# 
# Notice that the solution set must not contain duplicate triplets.
# 
# 
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
# Input: nums = []
# Output: []
# Example 3:
# Input: nums = [0]
# Output: []
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] > 0: break
            l = i + 1
            r = n - 1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                if sum3 == 0:
                    result.append([nums[i],nums[l],nums[r]])
                    while l+1 < n and nums[l+1] == nums[l]: l += 1  # Skip duplicates nums[l]
                    l += 1
                    r -= 1
                elif sum3 < 0: l += 1
                else: r -= 1
            while i+1 < n and nums[i+1] == nums[i]: i += 1  # Skip duplicates nums[l]
            i += 1
        return result
# @lc code=end

