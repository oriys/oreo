/*
 * @lc app=leetcode id=628 lang=javascript
 *
 * [628] Maximum Product of Three Numbers
 */
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumProduct = function (nums) {
    const n = nums.length;
    nums.sort((x, y) => y - x);
    return Math.max(nums[0] * nums[1] * nums[2], nums[0] * nums[n - 1] * nums[n - 2]);
};

