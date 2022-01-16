#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (31.13%)
# Likes:    15223
# Dislikes: 895
# Total Accepted:    1.6M
# Total Submissions: 5.2M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
# 
# 
# Example 1:
# 
# 
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: s = "cbbd"
# Output: "bb"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #palindroms read the same forward and backwards
        result = ''
        for i in range(len(s)):
            #check for odds e.g aba
            temp = self.palindrome_check(s, i, i)
            if len(result) < len(temp):
                result = temp
            #check for evens e.g abba
            temp = self.palindrome_check(s, i, i+1)
            if len(result) < len(temp):
                result = temp
        return result
    def palindrome_check(self, s, start, end):
        #loop through string from specified index
        #check that start and end of each slice are same
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return s[start+1:end]
        
# @lc code=end

