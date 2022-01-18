#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (26.09%)
# Likes:    6340
# Dislikes: 9101
# Total Accepted:    1.9M
# Total Submissions: 7.2M
# Testcase Example:  '123'
#
# Given a signed 32-bit integer x, return x with its digits reversed. If
# reversing x causes the value to go outside the signed 32-bit integer range
# [-2^31, 2^31 - 1], then return 0.
# 
# Assume the environment does not allow you to store 64-bit integers (signed or
# unsigned).
# 
# 
# Example 1:
# 
# 
# Input: x = 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: x = -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: x = 120
# Output: 21
# 
# 
# 
# Constraints:
# 
# 
# -2^31 <= x <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        if x < 0:
            flag = -1
            x = -x
        else:
            flag = 1

        while x:
            result = result * 10 + x % 10
            x //= 10
            
        #max 32-bit is (2^31 - 1)
        #if x > max return 0
        return 0 if result > pow(2, 31) else result * flag
        
# @lc code=end

