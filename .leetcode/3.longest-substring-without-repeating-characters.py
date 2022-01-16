#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (32.06%)
# Likes:    20189
# Dislikes: 916
# Total Accepted:    2.8M
# Total Submissions: 8.7M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# 
# 
# Example 2:
# 
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# Example 3:
# 
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        max_substring_length = 0
        for i in range(len(s)):
            # If s[i] not in seen, we can keep increasing the window size by moving right pointer
            if s[i] not in seen:
                seen[s[i]] = i
                if max_substring_length < i-left+1:
                    max_substring_length = i-left+1
            else:
                # There are two cases if s[i] in seen:
                # case1: s[i] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
                # case2: s[i] is not inside the current window, we can keep increase the window
                if seen[s[i]] < left:
                    if max_substring_length < i-left+1:
                        max_substring_length = i-left+1
                else:
                    left = seen[s[i]] + 1
            seen[s[i]] = i
        return max_substring_length
        
# @lc code=end

