/*
 * @lc app=leetcode id=9 lang=javascript
 *
 * [9] Palindrome Number
 *
 * https://leetcode.com/problems/palindrome-number/description/
 *
 * algorithms
 * Easy (52.48%)
 * Likes:    6126
 * Dislikes: 2172
 * Total Accepted:    2.2M
 * Total Submissions: 4.1M
 * Testcase Example:  '121'
 *
 * Given an integer x, return true if x is palindrome integer.
 * 
 * An integer is a palindrome when it reads the same backward as forward.
 * 
 * 
 * For example, 121 is a palindrome while 123 is not.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: x = 121
 * Output: true
 * Explanation: 121 reads as 121 from left to right and from right to left.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: x = -121
 * Output: false
 * Explanation: From left to right, it reads -121. From right to left, it
 * becomes 121-. Therefore it is not a palindrome.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: x = 10
 * Output: false
 * Explanation: Reads 01 from right to left. Therefore it is not a
 * palindrome.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * -2^31 <= x <= 2^31 - 1
 * 
 * 
 * 
 * Follow up: Could you solve it without converting the integer to a string?
 */

// @lc code=start
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    
    if(x < 0) {
        return false;
    }
    let intString = x.toString();
   
    let l = 0;
    let r = intString.length - 1;
    while(l <= r) {
        if(intString[l] !== intString[r]){
            return false;
        }
        l += 1
        r -= 1
    }
    return true;

    // without converting to string
    // if(x < 0) {
    //     return false;
    // }
    // let reverse = 0;
    // for(let i = x; i > 0; i = Math.floor(i/10)) {
    //     reverse = reverse*10 + i%10
    // }
    // return reverse === x
    
};
// @lc code=end

