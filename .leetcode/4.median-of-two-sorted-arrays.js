/*
 * @lc app=leetcode id=4 lang=javascript
 *
 * [4] Median of Two Sorted Arrays
 *
 * https://leetcode.com/problems/median-of-two-sorted-arrays/description/
 *
 * algorithms
 * Hard (34.47%)
 * Likes:    17559
 * Dislikes: 2098
 * Total Accepted:    1.5M
 * Total Submissions: 4.2M
 * Testcase Example:  '[1,3]\n[2]'
 *
 * Given two sorted arrays nums1 and nums2 of size m and n respectively, return
 * the median of the two sorted arrays.
 * 
 * The overall run time complexity should be O(log (m+n)).
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums1 = [1,3], nums2 = [2]
 * Output: 2.00000
 * Explanation: merged array = [1,2,3] and median is 2.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums1 = [1,2], nums2 = [3,4]
 * Output: 2.50000
 * Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * nums1.length == m
 * nums2.length == n
 * 0 <= m <= 1000
 * 0 <= n <= 1000
 * 1 <= m + n <= 2000
 * -10^6 <= nums1[i], nums2[i] <= 10^6
 * 
 * 
 */

// @lc code=start
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    if(nums1.length > nums2.length) return findMedianSortedArrays(nums2, nums1)
    let x = nums1.length;
    let y = nums2.length;
    let low = 0, high = x;
    while(low <= high) {
        const partitionX = (high + low) >> 1;
        const partitionY = ((x + y + 1) >> 1) - partitionX;

        const maxX = partitionX === 0 ? Number.NEGATIVE_INFINITY : nums1[partitionX - 1];
        const maxY = partitionY === 0 ? Number.NEGATIVE_INFINITY : nums2[partitionY - 1];

        const minX = partitionX === nums1.length ? Number.POSITIVE_INFINITY : nums1[partitionX];
        const minY = partitionY === nums2.length ? Number.POSITIVE_INFINITY : nums2[partitionY];

        if(maxX <= minY && maxY <= minX) {
            const lowMax = Math.max(maxX, maxY)
            if( (x + y) % 2 === 1) {
                return lowMax;
            }
            return (lowMax + Math.min(minX, minY)) / 2;
        } else if(maxX < minY) {
            low = partitionX + 1;
        } else {
            high = partitionX - 1;
        }
    }
};
// @lc code=end

